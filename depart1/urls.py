from django.urls import path
from . import views

urlpatterns = [
    path("member/", views.index, name="index"),
    path("", views.index, name="index"),
    path("treasurer/dashboard/", views.treasurer_dashboard_view, name="Tdashboard"),
    path("treasurer/residents/", views.treasurer_resident_view, name="Tresidents"),
    path("treasurer/logs/", views.treasurer_logs_view, name="Tlogs"),
    path("treasurer/users/", views.treasurer_users_view, name="Tusers")

]