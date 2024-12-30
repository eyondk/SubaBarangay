from django.urls import path
from . import views

urlpatterns = [
    path("member/", views.index, name="index"),
    path("", views.index, name="index"),

    path("treasurer/dashboard/", views.treasurer_dashboard_view, name="Tdashboard"),
    path("treasurer/residents/", views.treasurer_resident_view, name="Tresidents"),
    path("treasurer/logs/", views.treasurer_logs_view, name="Tlogs"),
    path("treasurer/users/", views.treasurer_users_view, name="Tusers"),    
    path("treasurer/resident/view/details", views.treasurer_resident_details_view, name="Tresident_details"),
    path("treasurer/resident/view/children", views.treasurer_resident_children_view, name= "Tresident_children"),
    path("treasurer/resident/view/parents", views.treasurer_resident_parents_view, name= "Tresident_parents"),
    path("treasurer/resident/view/husband", views.treasurer_resident_husband_view, name="Tresident_husband"),

    #path("treasurer/resident/<int:resident_id>/", views.treasurer_view_resident, name="view_resident")  
    path("resident/view/details", views.resident_details_view, name="resident_details"),
    path("resident/view/husband", views.resident_husband_view, name="resident_husband"),
    path("resident/view/children", views.resident_children_view, name= "resident_children"),
    path("resident/view/parents", views.resident_parents_view, name= "resident_parents"),

    path("captain/dashboard/", views.captain_dashboard_view, name="Cdashboard"),
    path("captain/resident/", views.captain_resident_view, name="Cresidents"),
    path("captain/logs/", views.captain_logs_view, name="Clogs"),
    path("captain/resident/view/details", views.captain_resident_details_view, name= "Cresident_details"),
    path("captain/resident/view/children", views.captain_resident_children_view, name= "Cresident_children"),
    path("captain/resident/view/parents", views.captain_resident_parents_view, name= "Cresident_parents"),
    path("captain/resident/view/husband", views.captain_resident_husband_view, name="Cresident_husband")

]