from django.urls import path
from . import views

urlpatterns = [
    path("member/", views.index, name="index"),
    path("", views.index, name="index"),
    path("treasurer/", views.treasurer_view, name="treasurer")
]