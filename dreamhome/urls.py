from django.urls import path
from .views import *
urlpatterns = [
    path("branch/", BranchView.as_view(), name = "branch list"),
    path("branch/<str:id>/", BranchDetail.as_view(), name = "branch detail"),
    path("staff/", StaffList.as_view(), name = "staff list"),
    path("staff/<str:branch_no>", StaffList.as_view(), name = "staff list by branch"),
    path("stafflisting/<str:branch_no>/", StaffByBranch.as_view(), name = "staff by branch"), #USE IN LISTING
    path("privateOwner/", PrivateOwnerList.as_view()),
    path("client/", ClientView.as_view(), name = "client list"),
    path("client/<str:id>/", ClientDetail.as_view(), name = "client detail"),


]