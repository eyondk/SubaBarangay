from django.urls import path
from . import views

urlpatterns = [
    path("member/", views.index, name="index"),
    path("", views.index, name="index"),
    path("treasurer/dashboard/", views.treasurer_dashboard_view, name="Tdashboard"),
    path("treasurer/residents/", views.treasurer_resident_view, name="Tresidents"),
    path("treasurer/logs/", views.treasurer_logs_view, name="Tlogs"),
    path("treasurer/users/", views.treasurer_users_view, name="Tusers"),
    #path("treasurer/resident/<int:resident_id>/", views.treasurer_view_resident, name="view_resident")  
    path("treasurer/resident/view/details", views.treasurer_resident_details_view, name="Tresident_details"),
    path("treasurer/resident/view/husband", views.treasurer_resident_husband_view, name="Tresident_husband"),
    path("treasurer/resident/view/children", views.treasurer_resident_children_view, name= "Tresident_children"),
    path("treasurer/resident/view/parents", views.treasurer_resident_parents_view, name= "Tresident_parents")

]