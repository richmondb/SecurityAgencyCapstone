from django.urls import path

from .views import *

urlpatterns = [
    path("", LandingView.as_view(), name="landing"),
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("account/", AccountDetailsView.as_view(), name="account"),
    path("home/", HomeView.as_view(), name="home"),
    path("services/", ServicesView.as_view(), name="services"),
    path(
        "contract/<int:pk>/full",
        ContractFullDetailView.as_view(),
        name="contract-full-detail",
    ),
    path("active/", ActiveContractsView.as_view(), name="active-contracts"),
    path("add-security/", AddSecurityGuardView.as_view(), name="add-guard"),
    path("guard-list/", SecurityGuardListView.as_view(), name="guard-list"),
    path("guard/<int:pk>/", GuardDetailView.as_view(), name="guard-view"),
    path("ddo/", DDOListView.as_view(), name="ddo-list"),
    path("ddo/<int:pk>/detail/", DDODetailView.as_view(), name="ddo-detail"),
    path(
        "ddo/<int:ddo_pk>/schedule/<int:pk>/",
        DDOScheduleDetailView.as_view(),
        name="ddo-schedule",
    ),
    path("ddo/<int:pk>/history/", DDOHistoryView.as_view(), name="ddo-history"),
    path(
        "contract/locations/get/",
        ContractLocationsGet.as_view(),
        name="contract-locations-get",
    ),
    path(
        "contract/locations/<int:pk>/edit/",
        ContractLocationsEditView.as_view(),
        name="contract-locations-edit",
    ),
    path(
        "contract/post/<int:pk>/day/<int:day>/reset/",
        ResetDaySchedule.as_view(),
        name="reset-day-schedule",
    ),
    path(
        "contract/locations/<int:location_pk>/posts/<int:pk>/schedule/quick-assign/",
        ContractPostQuickAssignView.as_view(),
        name="contract-post-assign",
    ),
    path(
        "contract/locations/<int:location_pk>/posts/<int:pk>/schedule/quick-deassign/",
        ContractPostQuickDeassignView.as_view(),
        name="contract-post-deassign",
    ),
    path(
        "contract/locations/<int:location_pk>/posts/<int:post_pk>/shift/<int:pk>/",
        ContractPostGuardsView.as_view(),
        name="contract-post-guards",
    ),
    # --------------------------- might be unusable ----------------------------------------------------
    path(
        "contract/locations/<int:pk>/schedule/reset/",
        ResetSchedule.as_view(),
        name="reset-schedule",
    ),
    path(
        "contract/locations/finalize/",
        ContractLocationFinalize.as_view(),
        name="location-finalize",
    ),
    path(
        "contract/requests/", ContractRequestsView.as_view(), name="contract-requests"
    ),
    path("contract/<int:pk>/", ContractDetailView.as_view(), name="contract-detail"),
    path(
        "contract/<int:pk>/approve/",
        ApproveContractView.as_view(),
        name="approve-contract",
    ),
    path("contract/<int:pk>/deny/", DenyContractView.as_view(), name="deny"),
    path("ddo/<int:pk>/drafts/", DDODraftsView.as_view(), name="ddo-drafts"),
    path(
        "ddo/<int:ddo_pk>/assign-firearms/post/<int:pk>/",
        DDOAssignFirearmsView.as_view(),
        name="ddo-assign-firearms",
    ),
    path("ddo/<int:pk>/delete/", DDODeleteView.as_view(), name="ddo-delete"),
    path(
        "ddo/<int:ddo_pk>/assign-security/post/<int:pk>/",
        DDOSearchSecurityView.as_view(),
        name="ddo-search-security",
    ),
    path(
        "ddo/<int:ddo_pk>/assign-security/post/<int:post_pk>/guard/<int:pk>/",
        DDOAssignSecurityView.as_view(),
        name="ddo-assign-security",
    ),
    path(
        "ddo/<int:ddo_pk>/assign-reliever/post/<int:pk>/",
        DDOSearchRelieverView.as_view(),
        name="ddo-search-reliever",
    ),
    path(
        "ddo/<int:ddo_pk>/assign-reliever/post/<int:post_pk>/guard/<int:pk>/",
        DDOAssignRelieverView.as_view(),
        name="ddo-assign-reliever",
    ),
    path(
        "remove/<int:pk>/designation/",
        RemoveDesignationView.as_view(),
        name="remove-designation",
    ),
    path(
        "remove/<int:falist_pk>/fa-list/<int:pk>/firearm",
        RemoveFirearmsView.as_view(),
        name="remove-firearms",
    ),
    path(
        "search/<int:ddo_pk>/fa_list/<int:pk>/firearm/",
        SearchFirearmView.as_view(),
        name="search-fa",
    ),
    path(
        "ddo/<int:location_pk>/post/<int:pk>/create/",
        DDOCreateView.as_view(),
        name="ddo-create",
    ),
    path(
        "ddo/<int:ddo_pk>/post/<int:pk>/initial/",
        DDOInitialView.as_view(),
        name="ddo-initial",
    ),
    path(
        "ddo/<int:ddo_pk>/post/<int:pk>/assign/",
        DDOAssignView.as_view(),
        name="ddo-assign",
    ),
    path(
        "ddo/<int:ddo_pk>/post/<int:pk>/finalize/", DDOFinalizeView, name="ddo-finalize"
    ),
    path("contract/", ContractView.as_view(), name="contract"),
    path(
        "contract/<int:pk>/locations/",
        ContractLocationView.as_view(),
        name="contract-location",
    ),
    path(
        "contract/<int:contract_pk>/location/<int:pk>/posts/",
        ContractLocationPostsView.as_view(),
        name="contract-location-post",
    ),
    path(
        "contract/<int:contract_pk>/location/<int:location_pk>/post/<int:pk>/schedule/",
        ContractLocationPostScheduleView.as_view(),
        name="contract-post-schedule",
    ),
    path(
        "contract/<int:contract_pk>/location/<int:location_pk>/post/<int:pk>/schedule/quick",
        ContractPostQuickAssignView.as_view(),
        name="contract-schedule-quick",
    ),
    path(
        "contract/<int:contract_pk>/location/<int:location_pk>/post/<int:post_pk>/schedule/<int:pk>/",
        ContractEditInstructionView.as_view(),
        name="contract-edit-instruction",
    ),
    path(
        "contract/<int:pk>/job-request/",
        ContractJobRequestCreateView.as_view(),
        name="contract-job-request",
    ),
    path(
        "contract/<int:pk>/job-detail/",
        ContractJobDetailView.as_view(),
        name="contract-job-detail",
    ),
    path(
        "contract/<int:contract_pk>/review/",
        ContractReview.as_view(),
        name="contract-review",
    ),
    path(
        "contract/<int:contract_pk>/finalize/",
        ContractRemakeFinalizeView.as_view(),
        name="contract-remake-finalize",
    ),
    path("contract/<int:pk>/deny/", DenyJobRequest.as_view(), name="deny-job"),
    path("contract/<int:pk>/approve/", ApproveJobRequest.as_view(), name="approve-job"),
    path("requests/", JobRequestListView.as_view(), name="job-request-list"),
    path("remove/post/<int:pk>/", RemovePostView.as_view(), name="remove-post"),
    path(
        "remove/<int:contract_pk>/location/<int:pk>/",
        RemoveLocationView.as_view(),
        name="remove-location",
    ),
]
