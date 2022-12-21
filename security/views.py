from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from django.forms import modelformset_factory
from django.views.generic import View, DetailView
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from django.views.generic.edit import UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.db.models import Q

from .forms import *
from .models import *

from datetime import datetime, timedelta, time


class LandingView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:

            if request.user.is_superuser:

                return redirect("contract-requests")
            return redirect("home")

        return render(request, "security/landing.html", {})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect("contract-requests")

            return redirect("home")

        return render(request, "security/login.html", {})

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(user)

            login(request, user)

            if request.user.is_superuser:
                return redirect("contract-requests")

            return redirect("home")
        else:
            messages.info(request, "Email or Password incorrect")

        return render(request, "security/login.html", {})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("landing")


class SignupView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")

        form = CustomUserCreationForm

        context = {
            "form": form,
        }
        return render(request, "security/signup.html", context)

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            print("Error encountered")

        context = {
            "form": form,
        }

        return render(request, "security/signup.html", context)


class ContractLocationsGet(View):
    def get(self, request, *args, **kwargs):
        form = GetLocationForm(user=request.user)
        context = {
            "form": form,
        }

        return render(request, "security/contract-locations-get.html", context)

    def post(self, request, *args, **kwargs):
        form = GetLocationForm(request.POST, user=request.user)

        if form.is_valid():
            location = form.cleaned_data["locations"]
            location.include = True
            location.save()

            return redirect("contract-locations")

        context = {
            "form": form,
        }

        return render(request, "security/contract-locations-get.html", context)


class ContractPostQuickAssignView(View):
    def get(self, request, location_pk, pk, *args, **kwargs):
        location = Location.objects.get(id=location_pk)
        post = Post.objects.get(id=pk)
        form = QuickShiftTypeForm

        context = {
            "location": location,
            "post": post,
            "form": form,
        }
        return render(request, "security/contract-post-quick.html", context)

    def post(self, request, location_pk, pk, *args, **kwargs):
        location = Location.objects.get(id=location_pk)
        post = Post.objects.get(id=pk)
        form = QuickShiftTypeForm(request.POST)

        if form.is_valid():
            day_start = int(form.cleaned_data.get("day_start"))
            day_end = int(form.cleaned_data.get("day_end"))
            number_of_shifts = form.cleaned_data.get("number_of_shifts")
            working_hours = int(form.cleaned_data.get("working_hours"))
            start_time = form.cleaned_data.get("rotation_start")
            number_of_guards = form.cleaned_data.get("number_of_guards")

            proceed = True

            for day in range(day_start, day_end + 1):
                shifts = Shift.objects.filter(day=day)

                if Instruction.objects.filter(post=post, shift__in=shifts):
                    proceed = False
                    break

            print(proceed)
            if proceed:
                for day in range(day_start, day_end + 1):
                    start = start_time
                    for i in range(number_of_shifts):
                        end = (start + working_hours) % 24
                        shift = Shift.objects.create(
                            day=day,
                            start_time=time(hour=start),
                            end_time=time(hour=end),
                        )

                        start = end
                        shift.save()
                        instruction = Instruction.objects.create(
                            shift=shift, post=post, number_of_guards=number_of_guards
                        )
                        instruction.save()

            return redirect("contract-post-schedule", location.id, post.id)

        context = {
            "location": location,
            "post": post,
            "form": form,
        }
        return render(request, "security/contract-post-quick.html", context)


class ContractPostQuickDeassignView(View):
    def post(self, request, location_pk, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)

        Instruction.objects.filter(post=post).delete()

        next = request.POST.get("next", "/")
        return HttpResponseRedirect(next)


# do this
class ContractLocationsEditView(UpdateView):
    form_class = LocationForm
    model = Location
    template_name = "security/contract-locations-add.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.include = True
        self.object.save()
        return super(ContractLocationsEditView, self).form_valid(form)

    def get_success_url(self):
        return reverse("contract-locations")


class ResetSchedule(View):
    def post(self, request, pk, *args, **kwargs):
        location = Location.objects.get(id=pk)
        shifts = Shift.objects.filter(location=location)
        shifts.delete()

        next = request.POST.get("next", "/")
        return HttpResponseRedirect(next)


class ResetDaySchedule(View):
    def post(self, request, pk, day, *args, **kwargs):
        post = Post.objects.get(id=pk)
        instructions = Instruction.objects.filter(post=post, shift__day=day)

        for i in instructions:
            shift = i.shift
            print("Delete")
            shift.delete()
            i.delete()

        next = request.POST.get("next", "/")
        return HttpResponseRedirect(next)


class ContractLocationFinalize(View):
    def post(self, request, *args, **kwargs):

        final = True
        for x in Location.objects.filter(include=True, contract=None):
            if not x.has_schedule:
                final = False
                break

        if final:
            print("Should be good to go")
        else:
            print("Some schedules are unset")

        next = request.POST.get("next", "/")
        return HttpResponseRedirect(next)


class RemovePostView(View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        post.delete()

        next = request.POST.get("next", "/")
        return HttpResponseRedirect(next)


class ContractPostGuardsView(View):
    def get(self, request, location_pk, post_pk, pk, *args, **kwargs):
        location = Location.objects.get(id=location_pk)
        post = Post.objects.get(id=post_pk)
        shift = Shift.objects.get(id=pk)
        instruction = Instruction.objects.get(shift__id=pk, post__id=pk)
        form = InstructionForm(instance=instruction)

        context = {
            "location": location,
            "post": post,
            "form": form,
            "instruction": instruction,
        }
        return render(request, "security/contract-post-guards.html", context)

    def post(self, request, location_pk, post_pk, pk, *args, **kwargs):
        location = Location.objects.get(id=location_pk)
        post = Post.objects.get(id=post_pk)
        shift = Shift.objects.get(id=pk)
        instruction = Instruction.objects.get(shift=shift, post=post)
        form = InstructionForm(request.POST, instance=instruction)

        if form.is_valid():
            x = form.save()

            return redirect("contract-post-schedule", location.id, post.id)

        context = {"location": location, "form": form, "instruction": instruction}
        return render(request, "security/contract-post-guards.html", context)


class AccountDetailsView(View):
    def get(self, request, *args, **kwargs):

        context = {}
        return render(request, "security/account-details.html", context)


class HomeView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request, *args, **kwargs):
        pending = Contract.objects.filter(status=1, client=request.user)
        active = Contract.objects.filter(status=3, client=request.user)

        context = {
            "pending": pending,
            "active": active,
        }
        return render(request, "security/home.html", context)


class ServicesView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:

            if request.user.is_superuser:

                return redirect("contract-requests")
            return redirect("home")

        return render(request, "security/services.html", {})


class ContractRequestsView(View):
    def get(self, request, *args, **kwargs):
        contracts = Contract.objects.filter(status=1, is_finished=False)

        context = {
            "contracts": contracts,
        }

        return render(request, "security/contract-requests.html", context)


class ContractFullDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(id=pk)
        locations = contract.locations.all()
        previous = request.META.get("HTTP_REFERER")

        context = {
            "locations": locations,
            "contract": contract,
            "previous": previous,
        }

        return render(request, "security/contract-details.html", context)


class ApproveContractView(View):
    def post(self, request, pk, *args, **kwargs):
        print("Should go here")
        contract = Contract.objects.get(id=pk)
        contract.status = 3
        contract.save()

        if request.user.is_superuser:
            return redirect("active-contracts")
        else:
            return redirect("home")


class DenyContractView(View):
    pass


class ActiveContractsView(View):
    def get(self, request, *args, **kwargs):
        contracts = Contract.objects.filter(status=3)
        context = {
            "contracts": contracts,
        }
        return render(request, "security/active-contracts.html", context)


class AddSecurityGuardView(View):
    def get(self, request, *args, **kwargs):
        form = GuardForm

        context = {
            "form": form,
        }
        return render(request, "security/add-security.html", context)

    def post(self, request, *args, **kwargs):
        form = GuardForm(request.POST)
        print("Supposedly here")

        if form.is_valid():
            guard = form.save(commit=False)
            guard.save()

            return redirect("add-guard")

        context = {
            "form": form,
        }
        return render(request, "security/add-security.html", context)


class SecurityGuardListView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request, *args, **kwargs):
        guards = Guard.objects.all()

        paginator = Paginator(guards, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            "page_obj": page_obj,
        }
        return render(request, "security/guard-list.html", context)


class SearchFirearmView(View):
    def get(self, request, ddo_pk, pk, *args, **kwargs):
        serial_number = int(request.GET.get("serial_number"))

        ddo = DDO.objects.get(id=ddo_pk)
        post = Post.objects.get(id=pk)

        fa_list = FirearmAssignment.objects.get(ddo=ddo, post=post)

        if fa_list.firearms.all().count() < post.location.max_firearms:
            try:
                fa = Firearm.objects.get(serial_number=serial_number)

                fa_list.firearms.add(fa)
            except:
                print("Firearm Does not exist")

        next = request.GET.get("next", "/")
        return HttpResponseRedirect(next)


class GuardDetailView(DetailView):
    model = Guard
    template_name = "security/guard-detail.html"


class DDOListView(View):
    def get(self, request, *args, **kwargs):
        contracts = Contract.objects.filter(status=3)

        context = {
            "contracts": contracts,
        }
        return render(request, "security/ddo-list.html", context)


def AssignFirearms(request, location_pk, pk):
    location = Location.objects.get(id=location_pk)
    post = Post.objects.get(id=pk)

    context = {
        "location": location,
        "post": post,
    }
    return render(request, "security/assign-firearms.html", context)


class DDODetailView(View):
    def get(self, request, pk, *args, **kwargs):
        ddo = DDO.objects.get(id=pk)
        previous = request.META.get("HTTP_REFERER")
        print(request.get_full_path)
        print(previous)
        validity = date(2023, 1, 12)
        agency_name = settings.AGENCY_NAME
        agency_address = settings.AGENCY_ADDRESS

        try:
            fa_list = FirearmAssignment.objects.get(ddo=ddo)
            print(fa_list)
        except Exception as z:
            print(z)
            fa_list = None

        context = {
            "previous": previous,
            "ddo": ddo,
            "fa_list": fa_list,
            "agency_name": agency_name,
            "agency_address": agency_address,
            "validity": validity,
        }
        return render(request, "security/ddo-detail.html", context)


class DDOHistoryView(View):
    def get(self, request, pk, *args, **kwargs):
        location = Location.objects.get(id=pk)
        previous = request.META.get("HTTP_REFERER")
        ddos = location.ddos.filter(is_finished=True).order_by("-id")
        context = {
            "previous": previous,
            "location": location,
            "ddos": ddos,
        }
        return render(request, "security/ddo-history.html", context)


class DDOScheduleDetailView(View):
    def get(self, request, ddo_pk, pk, *args, **kwargs):
        ddo = DDO.objects.get(id=ddo_pk)
        post = Post.objects.get(id=pk)

        previous = request.META.get("HTTP_REFERER")

        monday = ddo.on_day(post, 1)
        tuesday = ddo.on_day(post, 2)
        wednesday = ddo.on_day(post, 3)
        thursday = ddo.on_day(post, 4)
        friday = ddo.on_day(post, 5)
        saturday = ddo.on_day(post, 6)
        sunday = ddo.on_day(post, 7)

        context = {
            "previous": previous,
            "post": post,
            "ddo": ddo,
            "monday": monday,
            "tuesday": tuesday,
            "wednesday": wednesday,
            "thursday": thursday,
            "friday": friday,
            "saturday": saturday,
            "sunday": sunday,
        }
        return render(request, "security/ddo-schedule.html", context)


class DDODraftsView(View):
    def get(self, request, pk, *args, **kwargs):
        location = Location.objects.get(id=pk)
        ddos = DDO.objects.filter(is_finished=False, location=location)

        context = {
            "ddos": ddos,
        }
        return render(request, "security/ddo-drafts.html", context)


class DDODeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        ddo = DDO.objects.get(id=pk)
        ddo.delete()

        next = request.POST.get("next", "/")
        return HttpResponseRedirect(next)


class DDOSearchSecurityView(View):
    def get(self, request, ddo_pk, pk, *args, **kwargs):
        ddo = DDO.objects.get(id=ddo_pk)
        post = Post.objects.get(id=pk)
        guard_list = []

        finished_ddos = DDO.objects.filter(is_finished=True)

        for i in finished_ddos:
            # if the duty happens in the future
            if i.start_date <= ddo.start_date and ddo.start_date <= i.end_date:
                for designation in i.designations.all():
                    guard_list.append(designation.guard.id)

        for designation in ddo.designations.all():
            guard_list.append(designation.guard.id)

        print(guard_list)

        qs = Guard.objects.exclude(id__in=guard_list)

        fname = request.GET.get("guard_fname")
        lname = request.GET.get("guard_lname")

        if fname and lname:
            qs = qs.filter(
                Q(first_name__startswith=fname) | Q(last_name__startswith=lname)
            )

        elif fname:
            qs = qs.filter(Q(first_name__startswith=fname))

        elif lname:
            qs = qs.filter(Q(last_name__startswith=lname))

        paginator = Paginator(qs, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        monday = ddo.on_day(post, 1)
        tuesday = ddo.on_day(post, 2)
        wednesday = ddo.on_day(post, 3)
        thursday = ddo.on_day(post, 4)
        friday = ddo.on_day(post, 5)
        saturday = ddo.on_day(post, 6)
        sunday = ddo.on_day(post, 7)

        context = {
            "monday": monday,
            "tuesday": tuesday,
            "wednesday": wednesday,
            "thursday": thursday,
            "friday": friday,
            "saturday": saturday,
            "sunday": sunday,
            "page_obj": page_obj,
            "post": post,
            "ddo": ddo,
        }
        return render(request, "security/ddo-search-security.html", context)


class DDOSearchRelieverView(View):
    def get(self, request, ddo_pk, pk, *args, **kwargs):
        ddo = DDO.objects.get(id=ddo_pk)
        post = Post.objects.get(id=pk)
        guard_list = []
        finished_ddos = DDO.objects.filter(is_finished=True)

        for i in finished_ddos:
            if i.start_date <= ddo.start_date and ddo.start_date <= i.end_date:
                for designation in i.designations.all():
                    guard_list.append(designation.guard.id)

        print(guard_list)

        for designation in ddo.designations.all():
            guard_list.append(designation.guard.id)

        qs = Guard.objects.all()
        print(len(qs))
        qs = qs.exclude(id__in=guard_list)
        print(len(qs))

        fname = request.GET.get("guard_fname")
        lname = request.GET.get("guard_lname")

        if fname and lname:
            qs = qs.filter(
                Q(first_name__startswith=fname) | Q(last_name__startswith=lname)
            )

        elif fname:
            qs = qs.filter(Q(first_name__startswith=fname))

        elif lname:
            qs = qs.filter(Q(last_name__startswith=lname))

        paginator = Paginator(qs, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        monday = ddo.on_day(post, 1)
        tuesday = ddo.on_day(post, 2)
        wednesday = ddo.on_day(post, 3)
        thursday = ddo.on_day(post, 4)
        friday = ddo.on_day(post, 5)
        saturday = ddo.on_day(post, 6)
        sunday = ddo.on_day(post, 7)

        context = {
            "monday": monday,
            "tuesday": tuesday,
            "wednesday": wednesday,
            "thursday": thursday,
            "friday": friday,
            "saturday": saturday,
            "sunday": sunday,
            "page_obj": page_obj,
            "post": post,
            "ddo": ddo,
        }
        return render(request, "security/ddo-search-reliever.html", context)


class DDOAssignSecurityView(View):
    def get(self, request, ddo_pk, post_pk, pk, *args, **kwargs):
        ddo = DDO.objects.get(id=ddo_pk)
        post = Post.objects.get(id=post_pk)
        guard = Guard.objects.get(id=pk)
        form = Remake2AddSecurityForm(ddo_pk=ddo_pk, post_pk=post_pk, guard_pk=pk)

        if ddo.designations.count() == post.guards:
            print("Hey about time to redirect boss")

        designation = None
        try:
            designation = Designation.objects.get(ddo=ddo, guard=guard)
        except:
            pass

        monday = ddo.on_day(post, 1)
        tuesday = ddo.on_day(post, 2)
        wednesday = ddo.on_day(post, 3)
        thursday = ddo.on_day(post, 4)
        friday = ddo.on_day(post, 5)
        saturday = ddo.on_day(post, 6)
        sunday = ddo.on_day(post, 7)

        context = {
            "monday": monday,
            "tuesday": tuesday,
            "wednesday": wednesday,
            "thursday": thursday,
            "friday": friday,
            "saturday": saturday,
            "sunday": sunday,
            "guard": guard,
            "ddo": ddo,
            "post": post,
            "form": form,
            "designation": designation,
        }
        return render(request, "security/ddo-assign-security.html", context)

    def post(self, request, ddo_pk, post_pk, pk, *args, **kwargs):
        ddo = DDO.objects.get(id=ddo_pk)
        post = Post.objects.get(id=post_pk)
        guard = Guard.objects.get(id=pk)
        form = Remake2AddSecurityForm(
            request.POST, ddo_pk=ddo_pk, post_pk=post_pk, guard_pk=pk
        )

        designation = None

        try:
            designation = Designation.objects.get(ddo=ddo, guard=guard)
        except:
            pass

        designation_count = ddo.designations.count()

        if form.is_valid():
            start_time = form.cleaned_data.get("shift")
            day_off = form.cleaned_data.get("day_off")
            print(start_time, day_off)

            start_time = start_time.split(":")
            start = time(hour=int(start_time[0]))

            current_designations = ddo.designations.all()

            instruction_map = {}

            instructions = Instruction.objects.filter(
                shift__start_time=start, post=post
            )

            for instruction in instructions:
                instruction_map[instruction] = int(instruction.number_of_guards)

            for designation in current_designations:
                if designation.day_off and designation.day_off in instruction_map:
                    instruction_map[designation.day_off] -= 1

                for instruction in designation.instructions.all():
                    if instruction in instructions:
                        instruction_map[instruction] -= 1

            for instruction in instructions:
                if instruction_map[instruction] == 0:
                    instruction_map.pop(instruction)

            if len(instruction_map) != 0:
                if day_off == 0:
                    day_off = None
                else:
                    try:
                        day_off = Instruction.objects.get(
                            shift__start_time=start, shift__day=day_off, post=post
                        )

                        designation = Designation.objects.create(
                            guard=guard, ddo=ddo, day_off=day_off
                        )
                    except:
                        designation = Designation.objects.create(guard=guard, ddo=ddo)

                for instruction in instruction_map:
                    if instruction == designation.day_off:
                        continue

                    designation.instructions.add(instruction)

                if ddo.designations.count() == post.guards:
                    return redirect("ddo-search-reliever", ddo.id, post.id)

                return redirect("ddo-search-security", ddo.id, post.id)

            return redirect("ddo-assign-security", ddo.id, post.id, guard.id)

        context = {
            "guard": guard,
            "ddo": ddo,
            "post": post,
            "form": form,
            "designation": designation,
        }
        return render(request, "security/ddo-assign-security.html", context)


class DDOAssignRelieverView(View):
    def get(self, request, ddo_pk, post_pk, pk, *args, **kwargs):
        ddo = DDO.objects.get(id=ddo_pk)
        post = Post.objects.get(id=post_pk)
        guard = Guard.objects.get(id=pk)
        form = RemakeAddRelieverForm(ddo_pk=ddo_pk, post_pk=post_pk, guard_pk=pk)

        designation = None
        try:
            designation = Designation.objects.get(
                ddo=ddo, guard=guard, designation_type=2
            )
        except:
            pass

        monday = ddo.on_day(post, 1)
        tuesday = ddo.on_day(post, 2)
        wednesday = ddo.on_day(post, 3)
        thursday = ddo.on_day(post, 4)
        friday = ddo.on_day(post, 5)
        saturday = ddo.on_day(post, 6)
        sunday = ddo.on_day(post, 7)

        context = {
            "monday": monday,
            "tuesday": tuesday,
            "wednesday": wednesday,
            "thursday": thursday,
            "friday": friday,
            "saturday": saturday,
            "sunday": sunday,
            "ddo": ddo,
            "guard": guard,
            "form": form,
            "post": post,
            "designation": designation,
        }
        return render(request, "security/ddo-assign-reliever.html", context)

    def post(self, request, ddo_pk, post_pk, pk, *args, **kwargs):
        ddo = DDO.objects.get(id=ddo_pk)
        post = Post.objects.get(id=post_pk)
        guard = Guard.objects.get(id=pk)
        form = RemakeAddRelieverForm(
            request.POST, ddo_pk=ddo_pk, post_pk=post_pk, guard_pk=pk
        )

        designation = None
        try:
            designation = Designation.objects.get(ddo=ddo, guard=guard)
        except:
            pass

        if form.is_valid():
            instructions = form.cleaned_data.get("instruction")

            if not designation:
                designation = Designation.objects.create(
                    ddo=ddo, guard=guard, designation_type=2
                )

            for instruction in instructions:
                designation.instructions.add(instruction)

            return redirect("ddo-assign-reliever", ddo.id, post.id, guard.id)

        context = {
            "ddo": ddo,
            "guard": guard,
            "form": form,
            "post": post,
            "designation": designation,
        }
        return render(request, "security/ddo-assign-reliever.html", context)


class DDOAssignFirearmsView(View):
    def get(self, request, ddo_pk, pk, *args, **kwargs):
        ddo = DDO.objects.get(id=ddo_pk)
        post = Post.objects.get(id=pk)
        fa_list = FirearmAssignment.objects.get(ddo=ddo, post=post)
        validity = datetime.date(2023, 1, 12)
        context = {"ddo": ddo, "post": post, "fa_list": fa_list, "validity": validity}
        return render(request, "security/ddo-search-firearm.html", context)


def DDOFinalizeView(request, ddo_pk, pk):
    ddo = DDO.objects.get(id=ddo_pk)
    post = Post.objects.get(id=pk)
    firearm_list = None

    if post.is_armed:
        firearm_list = FirearmAssignment.objects.get(ddo=ddo, post=post)

    validity = date(2023, 1, 12)

    if request.method == "POST":
        confirm = request.POST.get("agree")
        if confirm == "save":
            ddo.is_finished = True
            print("Should have saved though?")
            link = reverse("ddo-detail", kwargs={"pk": ddo_pk})
            ddo.link = link

            print(link)
            ddo.save()

            return redirect("ddo-list")

    context = {
        "ddo": ddo,
        "post": post,
        "firearm_list": firearm_list,
        "validity": validity,
    }
    return render(request, "security/ddo-finalize.html", context)


class RemoveDesignationView(View):
    def post(self, request, pk, *args, **kwargs):
        designation = Designation.objects.get(id=pk)
        designation.delete()

        next = request.POST.get("next", "/")
        return HttpResponseRedirect(next)


class RemoveFirearmsView(View):
    def post(self, request, falist_pk, pk, *args, **kwargs):
        fa_list = FirearmAssignment.objects.get(id=falist_pk)
        fa = Firearm.objects.get(serial_number=pk)

        fa_list.firearms.remove(fa)
        next = request.POST.get("next", "/")
        return HttpResponseRedirect(next)


class DDOCreateView(View):
    def post(self, request, location_pk, pk, *args, **kwargs):
        location = Location.objects.get(id=location_pk)
        post = Post.objects.get(id=pk)
        ddo = DDO.objects.create(location=location)
        ddo.link = reverse("ddo-initial", kwargs={"ddo_pk": ddo.id, "pk": pk})
        ddo.save()

        if post.is_armed:
            assignment = FirearmAssignment.objects.create(ddo=ddo, post=post)
            assignment.save()

        return redirect("ddo-initial", ddo.id, post.id)


class DDOInitialView(View):
    def get(self, request, ddo_pk, pk, *args, **kwargs):
        ddo = DDO.objects.get(id=ddo_pk)
        post = Post.objects.get(id=pk)
        form = DDOForm(instance=ddo)

        print(ddo.previous_draft)
        context = {
            "ddo": ddo,
            "post": post,
            "form": form,
        }
        return render(request, "security/ddo-initial.html", context)

    def post(self, request, ddo_pk, pk, *args, **kwargs):
        ddo = DDO.objects.get(id=ddo_pk)
        post = Post.objects.get(id=pk)
        form = DDOForm(request.POST, instance=ddo)

        if form.is_valid():
            validity = form.cleaned_data.get("validity")
            print(validity)

            new_ddo = form.save(commit=False)
            path = reverse("ddo-assign", kwargs={"ddo_pk": ddo_pk, "pk": pk})
            new_ddo.link = path
            new_ddo.save()

            return HttpResponseRedirect(path)

        else:
            print(form.errors)

        context = {
            "ddo": ddo,
            "post": post,
            "form": form,
        }
        return render(request, "security/ddo-initial.html", context)


class DDOAssignView(View):
    def get(self, request, ddo_pk, pk, *args, **kwargs):
        ddo = DDO.objects.get(id=ddo_pk)
        post = Post.objects.get(id=pk)

        monday = ddo.on_day(post, 1)
        tuesday = ddo.on_day(post, 2)
        wednesday = ddo.on_day(post, 3)
        thursday = ddo.on_day(post, 4)
        friday = ddo.on_day(post, 5)
        saturday = ddo.on_day(post, 6)
        sunday = ddo.on_day(post, 7)

        context = {
            "monday": monday,
            "tuesday": tuesday,
            "wednesday": wednesday,
            "thursday": thursday,
            "friday": friday,
            "saturday": saturday,
            "sunday": sunday,
            "ddo": ddo,
            "post": post,
        }
        return render(request, "security/ddo-assign.html", context)

    def post(self, request, ddo_pk, pk, *args, **kwargs):
        ddo = DDO.objects.get(id=ddo_pk)
        post = Post.objects.get(id=pk)

        proceed = True
        instruction_map = {}

        designations = ddo.designations.all()
        instructions = Instruction.objects.filter(post=post)

        if post.is_armed == True:
            fa_list = FirearmAssignment.objects.get(ddo=ddo, post=post)
            if fa_list.firearms.all().count() == 0:
                proceed = False

        for instruction in instructions:
            instruction_map[instruction] = 0

        for designation in designations:
            for instruction in designation.instructions.all():

                if instruction in instruction_map:
                    instruction_map[instruction] += 1

        for instruction in instructions:
            if instruction_map[instruction] == instruction.number_of_guards:
                instruction_map.pop(instruction)

        if len(instruction_map) != 0:
            proceed = False
        print(proceed)

        if proceed:
            return redirect("ddo-finalize", ddo.id, post.id)

        monday = ddo.on_day(post, 1)
        tuesday = ddo.on_day(post, 2)
        wednesday = ddo.on_day(post, 3)
        thursday = ddo.on_day(post, 4)
        friday = ddo.on_day(post, 5)
        saturday = ddo.on_day(post, 6)
        sunday = ddo.on_day(post, 7)

        context = {
            "monday": monday,
            "tuesday": tuesday,
            "wednesday": wednesday,
            "thursday": thursday,
            "friday": friday,
            "saturday": saturday,
            "sunday": sunday,
            "ddo": ddo,
            "post": post,
        }
        return render(request, "security/ddo-assign.html", context)


class ContractDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(id=pk)
        context = {
            "contract": contract,
        }
        return render(request, "security/contract-detail.html", context)


class ContractView(View):
    def get(self, request, *args, **kwargs):

        contract = None
        try:
            contract = Contract.objects.get(client=request.user, is_finished=False)
        except Exception as z:
            print(z)

        pending_list = Contract.objects.filter(
            client=request.user, is_finished=True
        ).exclude(status=3)

        context = {
            "contract": contract,
            "pending_list": pending_list,
        }

        return render(request, "security/contract.html", context)

    def post(self, request, *args, **kwargs):
        contract = Contract.objects.create(client=request.user)
        contract.link = reverse("contract-location", kwargs={"pk": contract.id})
        contract.save()

        return redirect("contract-location", contract.id)


class ContractLocationView(View):
    def get(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(id=pk)
        form = LocationForm()
        context = {
            "contract": contract,
            "form": form,
        }
        return render(request, "security/contract-location.html", context)

    def post(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(id=pk)
        form = LocationForm(request.POST)

        if form.is_valid():
            location = form.save(commit=False)
            location.owner = request.user
            location.save()
            contract.locations.add(location)

            return redirect("contract-location-post", contract.id, location.id)

        context = {
            "contract": contract,
            "form": form,
        }
        return render(request, "security/contract-location.html", context)


class ContractLocationPostsView(View):
    def get(self, request, contract_pk, pk, *args, **kwargs):
        contract = Contract.objects.get(id=contract_pk)
        location = Location.objects.get(id=pk)
        form = PostForm
        context = {
            "form": form,
            "contract": contract,
            "location": location,
        }
        return render(request, "security/contract-location-post.html", context)

    def post(self, request, contract_pk, pk, *args, **kwargs):
        contract = Contract.objects.get(id=contract_pk)
        location = Location.objects.get(id=pk)
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.location = location
            post.save()

            return redirect("contract-post-schedule", contract.id, location.id, post.id)

        context = {
            "form": form,
            "contract": contract,
            "location": location,
        }
        return render(request, "security/contract-location-post.html", context)


class ContractLocationPostScheduleView(View):
    def get(self, request, contract_pk, location_pk, pk, *args, **kwargs):
        contract = Contract.objects.get(id=contract_pk)
        location = Location.objects.get(id=location_pk)
        post = Post.objects.get(id=pk)
        context = {
            "contract": contract,
            "post": post,
            "location": location,
        }
        return render(request, "security/contract-post-schedule.html", context)


class ContractPostQuickAssignView(View):
    def get(self, request, contract_pk, location_pk, pk, *args, **kwargs):
        contract = Contract.objects.get(id=contract_pk)
        location = Location.objects.get(id=location_pk)
        post = Post.objects.get(id=pk)

        form = QuickShiftTypeForm

        context = {
            "contract": contract,
            "location": location,
            "post": post,
            "form": form,
        }
        return render(request, "security/contract-post-schedule-quick.html", context)

    def post(self, request, contract_pk, location_pk, pk, *args, **kwargs):
        contract = Contract.objects.get(id=contract_pk)
        location = Location.objects.get(id=location_pk)
        post = Post.objects.get(id=pk)
        form = QuickShiftTypeForm(request.POST)

        if form.is_valid():
            day_start = int(form.cleaned_data.get("day_start"))
            day_end = int(form.cleaned_data.get("day_end"))
            number_of_shifts = form.cleaned_data.get("number_of_shifts")
            working_hours = int(form.cleaned_data.get("working_hours"))
            start_time = form.cleaned_data.get("rotation_start")
            number_of_guards = form.cleaned_data.get("number_of_guards")

            proceed = True

            for day in range(day_start, day_end + 1):
                shifts = Shift.objects.filter(day=day)

                if Instruction.objects.filter(post=post, shift__in=shifts):
                    proceed = False
                    break

            print(proceed)
            if proceed:
                for day in range(day_start, day_end + 1):
                    start = start_time
                    for i in range(number_of_shifts):
                        end = (start + working_hours) % 24
                        shift = Shift.objects.create(
                            day=day,
                            start_time=time(hour=start),
                            end_time=time(hour=end),
                        )

                        start = end
                        shift.save()
                        instruction = Instruction.objects.create(
                            shift=shift, post=post, number_of_guards=number_of_guards
                        )
                        instruction.save()

            return redirect("contract-post-schedule", contract.id, location.id, post.id)

        context = {
            "location": location,
            "post": post,
            "form": form,
        }
        return render(request, "security/contract-post-schedule-quick.html", context)


class ContractEditInstructionView(View):
    def get(self, request, contract_pk, location_pk, post_pk, pk, *args, **kwargs):
        contract = Contract.objects.get(id=contract_pk)
        location = Location.objects.get(id=location_pk)
        post = Post.objects.get(id=post_pk)
        shift = Shift.objects.get(id=pk)
        instruction = Instruction.objects.get(post=post, shift=shift)

        form = InstructionForm(instance=instruction)

        context = {
            "form": form,
            "contract": contract,
            "location": location,
            "post": post,
            "shift": shift,
        }
        return render(request, "security/contract-edit-instruction.html", context)

    def post(self, request, contract_pk, location_pk, post_pk, pk, *args, **kwargs):
        contract = Contract.objects.get(id=contract_pk)
        location = Location.objects.get(id=location_pk)
        post = Post.objects.get(id=post_pk)
        shift = Shift.objects.get(id=pk)
        instruction = Instruction.objects.get(post=post, shift=shift)

        form = InstructionForm(request.POST, instance=instruction)

        if form.is_valid():
            x = form.save()

            return redirect("contract-post-schedule", contract.id, location.id, post.id)

        context = {
            "form": form,
            "contract": contract,
            "location": location,
            "post": post,
            "shift": shift,
        }
        return render(request, "security/contract-edit-instruction.html", context)


class ContractReview(View):
    def get(self, request, contract_pk, *args, **kwargs):
        contract = Contract.objects.get(id=contract_pk)
        locations = contract.locations.all()

        context = {
            "contract": contract,
            "locations": locations,
        }
        return render(request, "security/contract-review.html", context)

    def post(self, request, contract_pk, *args, **kwargs):
        contract = Contract.objects.get(id=contract_pk)
        contract.is_finished = True
        contract.link = reverse("contract-full-detail", kwargs={"pk": contract.id})
        contract.save()

        return redirect("home")


class RemoveLocationView(View):
    def post(self, request, contract_pk, pk, *args, **kwargs):
        contract = Contract.objects.get(id=contract_pk)
        location = Location.objects.get(id=pk)
        contract.locations.remove(location)

        next = request.POST.get("next", "/")
        return HttpResponseRedirect(next)


class ContractJobRequestCreateView(View):
    def get(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(id=pk)
        user = contract.client
        form = ContractForm(instance=contract)
        context = {
            "user": user,
            "contract": contract,
            "form": form,
        }
        return render(request, "security/contract-job-request.html", context)

    def post(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(id=pk)
        user = contract.client
        form = ContractForm(request.POST, instance=contract)

        if form.is_valid():

            contract = form.save()
            contract.link = reverse("contract-job-detail", kwargs={"pk": contract.id})
            contract.is_finished = True
            contract.save()

            return redirect("contract-job-detail", contract.id)
        else:
            print(form.errors)

        context = {
            "user": user,
            "contract": contract,
            "form": form,
        }
        return render(request, "security/contract-job-request.html", context)


class DenyJobRequest(View):
    def post(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(id=pk)

        next = request.POST.get("next", "/")
        return HttpResponseRedirect(next)


class ApproveJobRequest(View):
    def post(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(id=pk)

        next = request.POST.get("next")
        return HttpResponseRedirect(next)


class JobRequestListView(View):
    def get(self, request, *args, **kwargs):
        contracts = Contract.objects.filter(is_finished=True).exclude(status=3)

        context = {
            "contracts": contracts,
        }
        return render(request, "security/job-request-list.html", context)


class ContractJobDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(id=pk)
        context = {
            "contract": contract,
        }
        return render(request, "security/contract-job-detail.html", context)

    def post(self, request, pk, *args, **kwargs):
        print("hello")
        contract = Contract.objects.get(id=pk)
        contract.is_finished = True
        contract.status = 2
        contract.link = reverse("contract-full-detail", kwargs={"pk": contract.id})
        contract.save()

        return redirect("job-request-list")


class ContractRemakeFinalizeView(View):
    def post(self, request, contract_pk, *args, **kwargs):
        contract = Contract.objects.get(id=contract_pk)
        next = request.POST.get("next", "/")

        if contract.locations.count() == 0:
            messages.add_message(
                request,
                messages.INFO,
                "You must specify at least one location and one post connected to it",
            )
            return HttpResponseRedirect(next)

        for location in contract.locations.all():
            if location.posts.count() == 0:
                messages.add_message(request, messages.INFO, "No GuardPosts Found")
                return HttpResponseRedirect(next)

            for post in location.posts.all():
                instructions = Instruction.objects.filter(post=post)

                for instruction in instructions:
                    if instruction.number_of_guards == 0:
                        messages.add_message(
                            request,
                            messages.INFO,
                            "When an instruction is specified, the minimum number of guards should be at least 1",
                        )
                        return HttpResponseRedirect(next)

        return redirect("contract-review", contract.id)
