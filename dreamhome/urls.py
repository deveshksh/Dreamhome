from django.urls import path
from .views import *
urlpatterns = [
    path("branch/", BranchView.as_view(), name = "branch list"), #BRANCH-FORM
    path("branch/<str:id>/", BranchDetail.as_view(), name = "branch detail"),
    
    path("staff/", StaffList.as_view(), name = "staff list"), #STAFF-FORM
    path("staff/<str:id>", StaffDetail.as_view(), name = "staff detail"),
    path("stafflisting/<str:branch_no>/", StaffByBranch.as_view(), name = "staff by branch"), #USE IN LISTING

    path("privateOwner/", PrivateOwnerList.as_view()), #OWNER-FORM
    path("privateOwner/<str:id>/", PrivateOwnerDetail.as_view()),

    path("client/", ClientView.as_view(), name = "client list"), #CLIENT-FORM
    path("client/<str:id>/", ClientDetail.as_view(), name = "client detail"),
    
    path('properties/', PropertyforrentView.as_view(), name='property_list'), #PROPERTY-FORM
    path('properties/<str:id>/', PropertyforrentDetail.as_view(), name='property_detail'),
    path("propertieslisting/<str:branch_no>/", PropertyByBranch.as_view()), #USE IN LISTING

    path("propertyreport/", ViewPropertyReport.as_view()),
    path("propertyreportlisting/<str:property_no>/", ViewPropertyReportListing.as_view()),

    path("propertymatch/<str:propertyno>/", MatchProperty.as_view()),

    path("preferences/", PreferenceList.as_view()),

    path("lease/", LeaseView.as_view()),
    path("lease/<str:leaseno>/", LeaseDetail.as_view()),
    path("leasebyactive/", LeaseViewByActiveStatus.as_view()), #USE IN LEASE LISTING(SORT BY ACTIVE)

    path("branch/search", BranchSearchView.as_view()),
    path("staff/<str:branch_no>/search", StaffSearchView.as_view()),
    path("client/<str:branch_no>/search", ClientSearchView.as_view()),
    path("property/<str:branch_no>/search", PropertySearchView.as_view()),
    path("owner/<str:branch_no>/search", OwnerSearchView.as_view()),

    path("supervisor/<str:branch_no>/", SupervisorByBranchView.as_view()),


]