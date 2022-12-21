from django.db import models
from django.conf import settings
from django.utils import timezone
from django.forms import ValidationError
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.urls import reverse
from django.db.models import Q, Count
from django.db.models.signals import post_save

from django.dispatch import receiver

from datetime import timedelta, datetime, time, date
from dateutil.relativedelta import relativedelta

import math


class CustomUser(AbstractUser):
    SEX = (
        ("M", "Male"),
        ("F", "Female"),
    )

    phone_number = models.CharField(
        max_length=11,
        unique=True,
        null=True,
    )
    birth_date = models.DateField(blank=True, null=True)

    sex = models.CharField(choices=SEX, max_length=1, default="M")

    organization_name = models.CharField(max_length=150, null=True)
    organization_address = models.CharField(max_length=150, null=True)
    position = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.get_full_name()

    @property
    def get_age(self):
        birth_date = self.birth_date
        now = datetime.now().date()
        return (
            now.year
            - birth_date.year
            - ((now.month, now.day) > (birth_date.month, birth_date.day))
        )


def start_time():
    return datetime.now().date()


# class AgencyInformation(models.Model):
# 	fa_validity = models.DateField()


class Contract(models.Model):
    STATUS = (
        (1, "Pending Request"),
        (2, "Contract Proposed"),
        (3, "Proposal Approved"),
    )

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="contracts",
    )
    issued_date = models.DateField(default=start_time)
    start_date = models.DateField(null=True)
    years = models.IntegerField(null=True)
    months = models.IntegerField(null=True)
    daily_wage = models.FloatField(null=True)
    is_finished = models.BooleanField(default=False)
    status = models.IntegerField(default=1, choices=STATUS)
    link = models.URLField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.client.username

    @property
    def is_active(self):
        now = datetime.now().date()

        return self.start_date <= now and now <= self.contract_expiry

    @property
    def contract_expiry(self):
        years = self.years
        months = self.months

        if years and months:
            return self.start_date + relativedelta(years=years, months=months)
        elif months:
            return self.start_date + relativedelta(months=months)
        else:
            return self.start_date + relativedelta(years=years)

    class Meta:
        ordering = ["-id"]

    @property
    def num_of_locations(self):
        return Location.objects.filter(contract=self).count()

    @property
    def num_of_guards(self):
        guards = 0

        for location in self.locations.all():
            guards += location.number_of_guards

        return guards

    @property
    def get_latest_ddo(self):
        ddo = None
        try:
            ddos = DDO.objects.filter(is_finished=True)

            for ddo in ddos:
                if ddo.is_active:
                    return ddo

        except:
            pass

        return ddo

    @property
    def previous_draft(self):
        previous = None

        try:
            previous = DDO.objects.filter(location=self, ddo__is_finished=False)[0]
            print(previous)
        except:
            pass

        return previous


class Location(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    contracts = models.ManyToManyField(Contract, blank=True, related_name="locations")
    name = models.CharField(max_length=255, null=True, unique=True)
    address = models.CharField(max_length=255, null=True, unique=True)
    include = models.BooleanField(default=False)

    @property
    def get_active_contract(self):
        for contract in self.contracts.all():
            if contract.is_active:
                return contract

    @property
    def number_of_guards(self):
        guards = 0
        for post in Post.objects.filter(location=self):
            guards += post.guards

        return guards

    @property
    def previous_draft(self):
        previous = None
        try:
            previous = DDO.objects.filter(location=self, is_finished=False)[0]
        except:
            pass

        return previous

    @property
    def max_firearms(self):
        posts = Post.objects.filter(location=self, is_armed=True)
        max_firearms = 0

        for post in posts:
            max_firearms += math.floor(post.guards / 2)

        return max_firearms

    @property
    def complete(self):

        for day in range(1, 8):
            shifts = Shift.objects.filter(location=self, day=day)

            if shifts.count() == 0:
                return False

            for shift in shifts:
                # a shift must be occupied by at least one guard
                instructions = Instruction.objects.filter(shift=shift)
                if instructions.count() == 0:
                    return False

                for instruction in instructions:
                    if (
                        instruction.number_of_guards == None
                        or instruction.number_of_guards == 0
                    ):
                        return False

        return True

    @property
    def post_children(self):
        return Post.objects.filter(location=self)

    def __str__(self):
        return self.name


class DDO(models.Model):
    date_issued = models.DateTimeField(auto_now=True, null=True)
    start_date = models.DateField(null=True)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, related_name="ddos", blank=True
    )
    operations_manager = models.CharField(
        max_length=50, default=settings.ISSUING_OFFICER, blank=True
    )
    validity = models.IntegerField(default=0)
    link = models.URLField(max_length=250, null=True, blank=True)

    is_finished = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]

    def on_day(self, post, day):
        instructions = Instruction.objects.filter(post=post, shift__day=day)
        instruction_map = {}

        for instruction in instructions:
            if instruction.shift.start_time not in instruction_map:
                instruction_map[instruction.shift.start_time.strftime("%I:%M %p")] = []

            for designation in self.designations.all():
                if instruction in designation.instructions.all():
                    instruction_map[
                        instruction.shift.start_time.strftime("%I:%M %p")
                    ].append(str(designation.guard))

        return instruction_map

    @property
    def previous_ddo(self):
        previous = DDO.objects.filter(location=self.location, is_finished=True).exclude(
            id=self.id
        )

        if previous:
            return previous[0]

        return None

    @property
    def previous_draft(self):
        previous = None
        try:
            previous = DDO.objects.filter(location=self.location, is_finished=False)[0]
        except:
            pass

        return previous

    @property
    def end_date(self):
        return self.start_date + relativedelta(days=self.validity)

    @property
    def status(self):
        # 2 - Future, 1 = Active (Present) 0 - Done

        now = datetime.now().date()
        if self.end_date < now:
            return 2

        if self.start_date <= now and now <= self.end_date:
            return 1

        return 0

    @property
    def is_active(self):
        now = datetime.now().date()

        if self.start_date <= now and now <= self.end_date:
            return True

        return False


class Shift(models.Model):
    DAYS = (
        ("", ""),
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    )

    day = models.IntegerField(choices=DAYS, null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    @property
    def working_hours(self):
        return timedelta(
            hours=self.end_time.hour,
            minutes=self.end_time.minute,
            seconds=self.end_time.second,
        ) - timedelta(
            hours=self.start_time.hour,
            minutes=self.end_time.minute,
            seconds=self.end_time.second,
        )

    @property
    def time_range(self):
        start = self.start_time.strftime("%I:%M %p")
        end = self.end_time.strftime("%I:%M %p")
        return start + " - " + end

    @property
    def guards_assigned(self):
        guards = 0
        instructions = Instruction.objects.filter(shift=self)

        for item in instructions:
            guards += item.number_of_guards

        return guards

    def __str__(self):
        return f"{self.get_day_display()} - {self.start_time}"

    class Meta:
        ordering = ["day"]


DESIGNATION_TYPE = [
    (1, "Security Guard"),
    (2, "Reliever Guard"),
]


class Guard(models.Model):
    EDUCATION = [
        (1, "College Graduate"),
        (2, "College Undergraduate"),
        (3, "High School Graduate"),
    ]

    SEX = [
        ("", ""),
        ("M", "Male"),
        ("F", "Female"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    sex = models.CharField(max_length=100, choices=SEX, null=True)
    residence_address = models.CharField(
        max_length=150, default="02 Javier St., Poblacion, San Juan, Batangas"
    )
    nbi_clearance_id = models.CharField(max_length=21)
    nbi_issued_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=11, blank=True)
    highest_education = models.IntegerField(choices=EDUCATION, default=1)
    lesp_issued_date = models.DateField(null=True)
    sss = models.CharField(
        max_length=14,
        # this validates the form
        validators=[
            RegexValidator(regex="\d{2}-\d{7}-\d", message="Format doesn't match")
        ],
        null=True,
    )
    agency_affiliation = models.DateField(null=True)

    class Meta:
        ordering = ["last_name"]

    @property
    def get_age(self):
        now = datetime.now().date()

        return (
            now.year
            - self.birth_date.year
            - ((now.month, now.day) < (self.birth_date.month, self.birth_date.day))
        )

    @property
    def hours_worked(self):
        pass

    @property
    def active_days(self):
        pass

    @property
    def active_assignment(self):
        print(self.designations.all())

    @property
    def assigned_post(self):
        designation = self.designations.all().latest("id")
        if designation.is_active:
            post = designation.instructions.all()[0].post
            print(post)
            return post

        return None

    @property
    def get_full_name(self):
        return f"{self.last_name}, {self.first_name} "

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def has_duty(self):
        """
        I bet this has a bug
        """
        now = date.today()
        day = now.isoweekday()

        for designation in self.designations.filter(ddo__is_finished=True):
            if designation.is_active:
                for instruction in designation.instructions.all():
                    if instruction.shift.day == day:
                        return "On Duty"

                return "Day Off"

        return "Floating"


class Post(models.Model):
    location = models.ForeignKey(
        Location, related_name="posts", on_delete=models.CASCADE, null=True
    )
    shifts = models.ManyToManyField(Shift, through="Instruction", related_name="posts")
    place = models.CharField(max_length=50, null=True)
    remarks = models.CharField(max_length=100, null=True, blank=True)
    is_armed = models.BooleanField(default=True)

    def __str__(self):
        value = " "
        if self.is_armed:
            value = "Armed"
        else:
            value = "Unarmed"

        return f"{self.place} - {value}"

    @property
    def get_active_contract(self):
        for contract in self.location.contracts.all():
            if contract.is_active:
                return contract.id

    @property
    def get_recent(self):
        ddos = DDO.objects.filter(location=self.location, is_finished=True)
        instructions = Instruction.objects.all()

        for ddo in ddos:
            if not ddo.is_active:
                continue
            for instruction in instructions:
                for designation in ddo.designations.all():
                    if instruction in designation.instructions.all():
                        return ddo

        return None

    @property
    def get_recent_ddo(self):
        instruction = self.instructions.all()[0]

        for designation in instruction.designations.all():
            if designation.is_active:
                return designation.ddo.id

    @property
    def status(self):
        ddos = DDO.objects.filter(location=self.location, is_finished=True)
        instruction = Instruction.objects.filter(post=self)[0]
        status = 0

        for ddo in ddos:

            if not ddo.is_active:
                continue

            for designation in ddo.designations.all():
                if instruction in designation.instructions.all():
                    status = ddo.status

                    if status == 2:
                        continue

                    if status == 1:
                        return status

                    if status == 0:
                        return 0

        if not status or status == 2:
            return 0

    @property
    def guards(self):

        max_guards = 0
        for i in range(1, 8):
            guards = 0
            shifts = list(Shift.objects.filter(day=i))
            instructions = Instruction.objects.filter(shift__in=shifts, post=self)

            for instruction in instructions:
                guards += instruction.number_of_guards

            max_guards = max(guards, max_guards)

        return max_guards

    @property
    def on_monday(self):
        shifts = list(Shift.objects.filter(day=1))
        instructions = Instruction.objects.filter(post=self, shift__in=shifts)

        return instructions

    @property
    def on_tuesday(self):
        shifts = list(Shift.objects.filter(day=2))
        instructions = Instruction.objects.filter(post=self, shift__in=shifts)

        return instructions

    @property
    def on_wednesday(self):
        shifts = list(Shift.objects.filter(day=3))
        instructions = Instruction.objects.filter(post=self, shift__in=shifts)

        return instructions

    @property
    def on_thursday(self):
        shifts = list(Shift.objects.filter(day=4))
        instructions = Instruction.objects.filter(post=self, shift__in=shifts)

        return instructions

    @property
    def on_friday(self):
        shifts = list(Shift.objects.filter(day=5))
        instructions = Instruction.objects.filter(post=self, shift__in=shifts)

        return instructions

    @property
    def on_saturday(self):
        shifts = list(Shift.objects.filter(day=6))
        instructions = Instruction.objects.filter(post=self, shift__in=shifts)

        return instructions

    @property
    def on_sunday(self):
        shifts = list(Shift.objects.filter(day=7))
        instructions = Instruction.objects.filter(post=self, shift__in=shifts)

        return instructions

    @property
    def complete(self):
        instructions = self.instructions.all()

        for instruction in instructions:
            if instruction.number_of_guards == 0:
                return False

        return True


class Firearm(models.Model):
    KIND = (
        (1, "Pistol"),
        (2, "Shotgun"),
    )

    serial_number = models.CharField(max_length=20, primary_key=True)
    make = models.CharField(max_length=20, default="ARMSCOR")
    kind = models.IntegerField(choices=KIND, default=1)
    caliber = models.CharField(max_length=20, default=" ", blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.kind == 1:
            self.caliber = "9mm"
        elif self.kind == 2:
            self.caliber = "45mm"

        super(Firearm, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.serial_number


class FirearmAssignment(models.Model):
    ddo = models.ForeignKey(
        DDO, on_delete=models.CASCADE, null=True, blank=True, related_name="fa_list"
    )
    post = models.ForeignKey(
        Post, on_delete=models.SET_NULL, related_name="fa_list", null=True
    )
    firearms = models.ManyToManyField(Firearm, related_name="assignments", blank=True)


class Designation(models.Model):

    DES_TYPE = (
        (1, "Security Guard"),
        (2, "Reliever Guard"),
    )

    ddo = models.ForeignKey(
        DDO,
        on_delete=models.CASCADE,
        null=True,
        related_name="designations",
        blank=True,
    )
    guard = models.ForeignKey(
        Guard, on_delete=models.CASCADE, related_name="designations", null=True
    )
    designation_type = models.IntegerField(default=1, choices=DES_TYPE)
    day_off = models.ForeignKey(
        "Instruction", blank=True, null=True, on_delete=models.CASCADE
    )

    @property
    def is_active(self):
        return self.ddo.is_active

    @property
    def on_monday(self):
        instruction = self.instructions.get(shift__day=1)
        return instruction.shift.time_range

    @property
    def on_tuesday(self):
        instruction = self.instructions.get(shift__day=2)
        return instruction.shift.time_range

    @property
    def on_wednesday(self):
        instruction = self.instructions.get(shift__day=3)
        return instruction.shift.time_range

    @property
    def on_thursday(self):
        instruction = self.instructions.get(shift__day=4)
        return instruction.shift.time_range

    @property
    def on_friday(self):
        instruction = self.instructions.get(shift__day=5)
        return instruction.shift.time_range

    @property
    def on_saturday(self):
        instruction = self.instructions.get(shift__day=6)
        return instruction.shift.time_range

    @property
    def on_sunday(self):
        instruction = self.instructions.get(shift__day=7)
        return instruction.shift.time_range

    class Meta:
        ordering = ["-id"]


class Instruction(models.Model):
    designations = models.ManyToManyField(Designation, related_name="instructions")
    shift = models.ForeignKey(
        Shift, on_delete=models.CASCADE, related_name="instructions"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="instructions"
    )
    number_of_guards = models.IntegerField(default=0)

    @property
    def is_active(self):

        return designation.is_active()

    @property
    def guards_needed(self):
        guard_list = []
        designations = self.designations.all()

        for designation in designations:
            if designation.guard in guard_list:
                continue

            guard_list.append(designation.guard)

        return self.number_of_guards - len(guard_list)

    @property
    def guards_on_duty(self):
        designations = self.designations.all()
        guard_list = []
        for designation in designations:
            if designation.guard in guard_list:
                continue

            guard_list.append(designation.guard)

        return guard_list

    def __str__(self):
        return f"{self.post.place} - {self.shift}"
