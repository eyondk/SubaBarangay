from django.urls import path
from . import views

urlpatterns = [
    path("member/", views.index, name="index"),
    path("", views.index, name="index"),
    path("login/", views.index, name="login"),

    path("treasurer/dashboard/", views.treasurer_dashboard_view, name="Tdashboard"),
    path("treasurer/residents/", views.treasurer_resident_view, name="Tresidents"),
    path("treasurer/logs/", views.treasurer_logs_view, name="Tlogs"),
    path("treasurer/users/", views.treasurer_users_view, name="Tusers"),    
    path("treasurer/payments/", views.treasurer_payments_view, name="Tpayments"),
    path("treasurer/organizations/", views.treasurer_organization_view, name="Torganization"),
    path("treasurer/resident/view/details", views.treasurer_resident_details_view, name="Tresident_details"),
    path("treasurer/resident/view/children", views.treasurer_resident_children_view, name= "Tresident_children"),
    path("treasurer/resident/view/parents", views.treasurer_resident_parents_view, name= "Tresident_parents"),
    path("treasurer/resident/view/husband", views.treasurer_resident_husband_view, name="Tresident_husband"),

    path("treasurer/resident/add/details", views.treasurer_add_resident_view, name="TaddResident_details"),
    path("treasurer/resident/add/husband", views.treasurer_add_husband_details_view, name="TaddHusband_details"),
    path("treasurer/resident/add/parents", views.treasurer_add_parents_details_view, name="TaddParents_details"),
    path("treasurer/resident/add/educ", views.treasurer_add_educ_details_view, name="TaddEduc_details"),

    path("treasurer/resident/update/details", views.treasurer_update_resident_details_view, name="Tresident_update"),
    path("treasurer/resident/update/educ", views.treasurer_update_resident_educ_view, name="Tresident_update_educ"),






    #path("treasurer/resident/<int:resident_id>/", views.treasurer_view_resident, name="view_resident")  
    path("resident/view/details", views.resident_details_view, name="resident_details"),
    path("resident/view/husband", views.resident_husband_view, name="resident_husband"),    
    path("resident/view/children", views.resident_children_view, name= "resident_children"),
    path("resident/view/parents", views.resident_parents_view, name= "resident_parents"),

    # user path
    path("user/view/details", views.user_details_view, name="user_details"),
    path("user/edit/<int:user_id>/", views.update_user, name="update_user"),
    path("account", views.account_user_view, name="account_view"),

    path("captain/dashboard/", views.captain_dashboard_view, name="Cdashboard"),
    path("captain/resident/", views.captain_resident_view, name="Cresidents"),
    path("captain/logs/", views.captain_logs_view, name="Clogs"),
    path("captain/resident/view/details", views.captain_resident_details_view, name= "Cresident_details"),
    path("captain/resident/view/children", views.captain_resident_children_view, name= "Cresident_children"),
    path("captain/resident/view/parents", views.captain_resident_parents_view, name= "Cresident_parents"),
    path("captain/resident/view/husband", views.captain_resident_husband_view, name="Cresident_husband"),


    path("secretary/dashboard", views.secretary_dashboard_view, name="Sdashboard"),
    path("secretary/resident", views.secretary_resident_view, name="Sresident"),
    path("secretary/logs", views.secretary_logs_view, name="Slogs"),
    path("secretary/resident/view/details", views.secretary_resident_details_view, name="Sresident_details"),
    path("secretary/resident/view/husband", views.secretary_resident_husband_view, name="Sresident_husband"),
    path("secretary/resident/view/children", views.secretary_resident_children_view, name="Sresident_children"),
    path("secretary/resident/view/parents", views.secretary_resident_parents_view, name="Sresident_parents"),

    path("secretary/resident/add/details", views.secretary_resident_add_resident_view, name="SaddResident_details"),
    path("secretary/resident/add/educ", views.secretary_resident_add_educ_view, name="SaddEduc_details"),
    path("secretary/resident/update/details", views.secretary_update_resident_details_view, name="Sresident_update"),
    path("secretary/resident/update/educ", views.secretary_update_resident_educ_view, name="Sresident_update_educ"),






    path("BHW/dashboard/", views.bhw_dashboard_view, name="Bdashboard"),
    path("BHW/resident/", views.bhw_resident_view, name="Bresident"),
    # path("BHW/resident/view/details", views.bhw_resident_details_view, name="Bresident_details"),
    # path("BHW/resident/view/husband", views.bhw_resident_husband_view, name="Bresident_husband"),
    # path("BHW/resident/view/children", views.bhw_resident_children_view, name="Bresident_children"),
    # path("BHW/resident/view/parents", views.bhw_resident_parents_view, name="Bresident_parents"),
    path("BHW/add/resident/pg1", views.bhw_add_resident_1, name="bhw_add_resident1"),
    path("BHW/add/resident/pg2", views.bhw_add_resident_2, name="bhw_add_resident2"),
    path("BHW/add/resident/pg3", views.bhw_add_resident_3, name="bhw_add_resident3"),
    path("BHW/add/resident/pg4", views.bhw_add_resident_4, name="bhw_add_resident4"),
    path("BHW/add/resident/pg5", views.bhw_add_resident_5, name="bhw_add_resident5"),
    path("BHW/add/resident/pg6", views.bhw_add_resident_6, name="bhw_add_resident6"),
    path("BHW/add/resident/pg7", views.bhw_add_resident_7, name="bhw_add_resident7"),
    

    path("staff/dashboard", views.staff_dashboard_view, name="STdashboard"),
    path("staff/resident", views.staff_resident_view, name="STresident"),
    path("staff/resident/views/details", views.staff_resident_details_view, name="STresident_details"),
    path("staff/resident/views/husband", views.staff_resident_husband_view, name="STresident_husband"),
    path("staff/resident/views/children", views.staff_resident_children_view, name="STresident_children"),
    path("staff/resident/view/parents", views.staff_resident_parents_view, name="STresident_parents")
]