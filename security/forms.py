from django import forms
from django.forms import modelformset_factory, formset_factory
from django.db.models.fields import BLANK_CHOICE_DASH
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from .models import *


class CustomUserCreationForm(UserCreationForm):
    SEX = (
        ("M", "Male"),
        ("F", "Female"),
    )

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Username",
            }
        ),
    )
    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter First Name",
            }
        ),
    )
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(attrs={"placeholder": "Enter Last Name"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter Email"})
    )

    phone_number = forms.CharField(
        label="Phone Number",
        widget=forms.TextInput(attrs={"placeholder": "Enter Phone Number"}),
    )

    position = forms.CharField(
        label="Position in Office/Organization",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Position in Office/Organization",
            }
        ),
    )

    sex = forms.ChoiceField(
        label="Sex", choices=SEX, widget=forms.Select(attrs={"class": "form-control"})
    )

    birth_date = forms.DateField(
        label="Date of Birth", widget=forms.widgets.DateInput(attrs={"type": "date"})
    )

    organization_name = forms.CharField(
        label="Organization Name",
        widget=forms.TextInput(attrs={"placeholder": "Enter Organization Name"}),
    )

    organization_address = forms.CharField(
        label="Organization Address",
        widget=forms.TextInput(attrs={"placeholder": "Enter Organization Address"}),
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter Password"}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}),
    )

    class Meta(UserCreationForm):
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "birth_date",
            "organization_name",
            "organization_address",
            "sex",
            "position",
        ]


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ["username", "first_name", "last_name", "birth_date", "phone_number"]


class ContractForm(forms.ModelForm):

    start_date = forms.DateField(
        label="Contract Start Date (dd/mm/yyyy)",
        widget=forms.widgets.DateInput(attrs={"type": "date", "class": "form-control"}),
    )

    daily_wage = forms.FloatField(
        label="Daily Wage",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter Daily Wage"}
        ),
    )

    years = forms.IntegerField(
        label="Years",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Number of Years",
            }
        ),
        required=False,
    )

    months = forms.IntegerField(
        label="Months",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter Number of Months"}
        ),
        required=False,
    )

    class Meta:
        model = Contract
        exclude = [
            "issued_date",
            "is_final",
            "client",
            "link",
            "is_finished",
            "is_approved",
            "status",
        ]


class LocationForm(forms.ModelForm):

    name = forms.CharField(
        label="Location Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    address = forms.CharField(
        label="Address", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Location
        exclude = ["owner", "contract"]


class GetLocationForm(forms.Form):
    locations = forms.ModelChoiceField(
        widget=forms.Select(attrs={"class": "form-control"}),
        queryset=None,
        label="Location",
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(GetLocationForm, self).__init__(*args, **kwargs)
        self.fields["locations"].queryset = Location.objects.filter(
            owner=user, include=False, contract=None
        )


CHOICE = (
    (8, "8 Hours"),
    (12, "12 Hours"),
)


def default_time():
    return timedelta(hours=8)


DAYS = (
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday"),
)


class QuickShiftTypeForm(forms.Form):

    day_start = forms.ChoiceField(
        initial=1,
        label="Day Start",
        widget=forms.Select(attrs={"class": "form-control"}),
        choices=DAYS,
    )

    day_end = forms.ChoiceField(
        initial=7,
        label="Day End",
        widget=forms.Select(attrs={"class": "form-control"}),
        choices=DAYS,
    )

    number_of_shifts = forms.IntegerField(
        initial=2,
        label="Number of Shifts",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "min": 1,
                "max": 3,
            }
        ),
    )

    working_hours = forms.ChoiceField(
        label="Working Hours(select one)",
        choices=CHOICE,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    rotation_start = forms.IntegerField(
        initial=8,
        label="Rotation Start (Values of 1-12)",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "min": "1",
                "max": "12",
            }
        ),
    )

    number_of_guards = forms.IntegerField(
        initial=1,
        label="Number of Guards Per Shift",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    def clean(self):
        super().clean()
        shifts = self.cleaned_data.get("number_of_shifts")
        hours = self.cleaned_data.get("working_hours")

        day_start = int(self.cleaned_data.get("day_start"))
        day_end = int(self.cleaned_data.get("day_end"))

        if int(shifts) == 3 and int(hours) == 12:
            raise ValidationError(
                "Total working hours (shifts * hours) should not exceed 24 hours"
            )

        if day_end < day_start:
            raise ValidationError("Well thats not how it works lol :P")


class ShiftTypeForm(forms.Form):
    number_of_shifts = forms.IntegerField(
        initial=2,
        label="Number of Shifts",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "min": 1,
                "max": 3,
            }
        ),
    )

    working_hours = forms.ChoiceField(
        label="Working Hours(select one)",
        choices=CHOICE,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    rotation_start = forms.IntegerField(
        initial=8,
        label="Rotation Start (Values of 1-12)",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "min": "1",
                "max": "12",
            }
        ),
    )

    def clean(self):
        super().clean()
        shifts = self.cleaned_data.get("number_of_shifts")
        hours = self.cleaned_data.get("working_hours")
        print(type(shifts))
        print(type(hours))

        if int(shifts) == 3 and int(hours) == 12:
            raise ValidationError(
                "Total working hours (shifts * hours) should not exceed 24 hours"
            )


class ShiftForm(forms.ModelForm):
    start_time = forms.TimeField(
        label="Start Time",
        widget=forms.widgets.TimeInput(attrs={"type": "time", "class": "form-control"}),
    )

    class Meta:
        model = Shift
        exclude = ["location", "working_hours", "day"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["start_time"].required = True


ShiftFormSet = modelformset_factory(Shift, extra=0, form=ShiftForm)


class GuardDesignationTypeForm(forms.ModelForm):
    designation_type = forms.IntegerField(
        label="Designation Type",
        widget=forms.Select(choices=DESIGNATION_TYPE, attrs={"class": "form-control"}),
    )

    class Meta:
        model = Guard
        fields = ["designation_type"]


class PostForm(forms.ModelForm):
    place = forms.CharField(
        label="Place of Duty", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    is_armed = forms.BooleanField(
        label="Require Armed Security Guards",
        widget=forms.CheckboxInput(attrs={"class": "checkbox"}),
        required=False,
    )

    class Meta:
        model = Post
        exclude = ["shifts", "location"]


class InstructionForm(forms.ModelForm):

    number_of_guards = forms.IntegerField(
        label="Number of Guards",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = Instruction
        fields = ["number_of_guards"]


SEX = [
    ("", ""),
    ("M", "Male"),
    ("F", "Female"),
]


class PostAssignmentForm(forms.ModelForm):
    post = forms.ModelChoiceField(
        widget=forms.Select(attrs={"class": "form-control"}),
        queryset=None,
        label="Post",
    )

    number_of_guards = forms.IntegerField(
        label="Number of Guards",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "min": 1,
            }
        ),
    )

    class Meta:
        model = Instruction
        exclude = ["shift"]

    def __init__(self, *args, **kwargs):
        location_id = kwargs.pop("location_id", None)
        shift_id = kwargs.pop("shift_id", None)

        location = Location.objects.get(id=location_id)
        posts = Post.objects.filter(location=location)
        shift = Shift.objects.get(id=shift_id)

        super(PostAssignmentForm, self).__init__(*args, **kwargs)
        self.fields["post"].queryset = Post.objects.filter(location=location)


class GuardForm(forms.ModelForm):
    EDUCATION = [
        (1, "College Graduate"),
        (2, "College Undergraduate"),
        (3, "High School Graduate"),
    ]

    first_name = forms.CharField(
        label="First Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    last_name = forms.CharField(
        label="Last Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    birth_date = forms.DateField(
        label="Date of Birth",
        widget=forms.widgets.DateInput(attrs={"type": "date", "class": "form-control"}),
    )

    sss = forms.CharField(
        label="SSS",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "xx-xxxxxx-x"}
        ),
    )

    agency_affiliation = forms.DateField(
        label="Agency Affiliation Date",
        widget=forms.widgets.DateInput(attrs={"type": "date", "class": "form-control"}),
    )

    sex = forms.ChoiceField(
        label="Sex", choices=SEX, widget=forms.Select(attrs={"class": "form-control"})
    )

    highest_education = forms.ChoiceField(
        label="Highest Educational Attainment",
        widget=forms.Select(attrs={"class": "form-control"}),
        choices=EDUCATION,
    )

    nbi_clearance_id = forms.CharField(
        label="NBI Clearance ID",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "xxxxxxxxxx-xxxxxxxxxx",
            }
        ),
    )

    nbi_issued_date = forms.DateField(
        label="NBI Clearance Issued Date",
        widget=forms.widgets.DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
            }
        ),
    )

    phone_number = forms.CharField(
        label="Phone Number", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    residence_address = forms.CharField(
        label="Residence Address",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    lesp_issued_date = forms.DateField(
        label="License to Execute Security Profession Issued Date",
        widget=forms.widgets.DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
            }
        ),
    )

    class Meta:
        model = Guard
        fields = "__all__"


class DDOForm(forms.ModelForm):

    start_date = forms.DateField(
        label="Start Date",
        widget=forms.widgets.DateInput(attrs={"type": "date", "class": "form-control"}),
    )

    validity = forms.IntegerField(
        label="Effective Number of Days",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "min": 1,
                "max": 30,
            }
        ),
    )

    class Meta:
        model = DDO
        exclude = ["date_issued", "is_finished", "location", "link"]


class DesignationForm(forms.Form):
    guard = forms.CharField()

    designation_type = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-control"})
    )

    firearms = forms.ModelChoiceField(
        widget=forms.Select(attrs={"class": "form-control"}), queryset=None
    )


class Remake2AddSecurityForm(forms.Form):
    DAYS = (
        (0, ""),
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    )

    shift = forms.ChoiceField(
        label="Shift",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    day_off = forms.ChoiceField(
        label="Day Off",
        choices=DAYS,
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        ),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        ddo_pk = kwargs.pop("ddo_pk", None)
        post_pk = kwargs.pop("post_pk", None)
        guard_pk = kwargs.pop("guard_pk", None)

        ddo = DDO.objects.get(id=ddo_pk)
        post = Post.objects.get(id=post_pk)
        guard = Guard.objects.get(id=guard_pk)

        designations = ddo.designations.all()
        instructions = Instruction.objects.filter(post=post)
        shift_list = []

        day_map = {
            1: "Mon/",
            2: "Tue/",
            3: "Wed/",
            4: "Thu/",
            5: "Fri/",
            6: "Sat/",
            7: "Sun/",
        }

        for instruction in instructions:
            start_time = instruction.shift.start_time
            if start_time in shift_list:
                continue

            shift_list.append(start_time)

        SHIFTS = []

        for shift in shift_list:
            SHIFTS.append((shift, shift))

        super(Remake2AddSecurityForm, self).__init__(*args, **kwargs)
        self.fields["shift"].choices = SHIFTS


class RemakeAddSecurityForm(forms.Form):

    instruction = forms.ModelChoiceField(
        label="Instructions",
        widget=forms.Select(attrs={"class": "form-control"}),
        queryset=None,
    )

    def __init__(self, *args, **kwargs):
        ddo_id = kwargs.pop("ddo_pk", None)
        post_pk = kwargs.pop("post_pk", None)
        guard_pk = kwargs.pop("guard_pk", None)

        ddo = DDO.objects.get(id=ddo_id)
        post = Post.objects.get(id=post_pk)
        guard = Guard.objects.get(id=guard_pk)
        designation_list = Designation.objects.filter(ddo=ddo)

        hide_instruction_list = []

        try:
            same_day = []
            designation = Designation.objects.get(guard=guard, ddo=ddo)

            for instruction in designation.instructions.all():
                day = instruction.shift.day

                avoid_list = [
                    x.id for x in Instruction.objects.filter(post=post, shift__day=day)
                ]

                same_day.extend(avoid_list)

        except Exception as z:
            print("Hello?", z)

        instructions = list(Instruction.objects.filter(post=post))

        instruction_map = {}

        # get all instructions related to a post, roughly 10 - 24 max?

        for instruction in instructions:
            # get all designations related to current instructions that contain designations attached to
            # current ddo

            # initialize every instruction object and map them to an integer with value 0
            if not instruction in instruction_map:
                instruction_map[instruction.id] = 0

            for designation in instruction.designations.all():
                if designation in designation_list:
                    # increase by 1 every time we have already seen the designation appear in list
                    instruction_map[instruction.id] += 1

        for instruction in instructions:
            # if full, you can no longer fill guards for the slot
            if instruction_map[instruction.id] == instruction.number_of_guards:
                instruction_map.pop(instruction.id)

        super(RemakeAddSecurityForm, self).__init__(*args, **kwargs)
        self.fields["instruction"].queryset = Instruction.objects.exclude(
            id__in=same_day
        ).filter(id__in=instruction_map)


class RemakeAddRelieverForm(forms.Form):
    instruction = forms.ModelMultipleChoiceField(
        label="Instruction",
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        queryset=Instruction.objects.none(),
    )

    def __init__(self, *args, **kwargs):
        ddo_pk = kwargs.pop("ddo_pk", None)
        post_pk = kwargs.pop("post_pk", None)
        guard_pk = kwargs.pop("guard_pk", None)

        ddo = DDO.objects.get(id=ddo_pk)
        post = Post.objects.get(id=post_pk)
        guard = Guard.objects.get(id=guard_pk)
        designation_list = ddo.designations.filter(designation_type=1)

        day_off_list = [x.day_off.id for x in designation_list]

        super(RemakeAddRelieverForm, self).__init__(*args, **kwargs)
        self.fields["instruction"].queryset = Instruction.objects.filter(
            id__in=day_off_list
        )
