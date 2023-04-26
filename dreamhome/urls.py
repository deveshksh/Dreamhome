from django.urls import path
from .views import *
urlpatterns = [
    path("branch/", BranchView.as_view(), name = "branch list"),
    path("branch/<str:id>/", BranchDetail.as_view(), name = "branch detail"),
    path("staff/", StaffList.as_view(), name = "staff list"),
]