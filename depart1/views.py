from django.shortcuts import render
from django.shortcuts import render



def index(request):
    return render(request,"shared/login_page.html")

#----------------RESIDENT----------------

def resident_details_view(request): #, resident_id):
    # Fetch resident data by ID from PostgreSQL
    # try:
    #     resident = Resident.objects.get(id=resident_id)
    # except Resident.DoesNotExist:
    #     resident = None  # Handle non-existent resident gracefully
    #return render(request, "treasurer/Tview_resident.html", {"resident": resident})
    return render(request, "shared/resident_details.html")

def resident_husband_view(request):
    return render(request, "shared/resident_husband.html")

def resident_children_view(request):
    return render(request, "shared/resident_children.html")

def resident_parents_view(request):
    return render(request, "shared/resident_parents.html")


#------------TREASURER--------
def treasurer_dashboard_view(request):
    return render(request, "treasurer/Tdashboard.html")

def treasurer_resident_view(request):
    return render(request, "treasurer/Tresident.html")

def treasurer_logs_view(request):
    return render(request, "treasurer/Tlogs.html")

def treasurer_users_view(request):
    return render(request, "treasurer/Tusers.html")

def treasurer_payments_view(request):
    return render(request, "treasurer/Tpayments.html")
    
def treasurer_organization_view(request):
    return render(request, "treasurer/Torganization.html")
    

def treasurer_resident_details_view(request):
    return render(request, "treasurer/Tresident_details.html")

def treasurer_resident_children_view(request):
    return render(request, "treasurer/Tresident_children.html")

def treasurer_resident_parents_view(request):
    return render(request, "treasurer/Tresident_parents.html")

def treasurer_resident_husband_view(request):
    return render(request, "treasurer/Tresident_husband.html")


def treasurer_add_resident_view(request):
    return render(request, "treasurer/TaddResident_details.html")

def treasurer_add_husband_details_view(request):
    return render(request, "treasurer/TaddHusband_details.html")

def treasurer_add_parents_details_view(request):
    return render(request, "treasurer/TaddParents_details.html")

def treasurer_add_educ_details_view(request):
    return render(request, "treasurer/TaddEduc_details.html")


def treasurer_update_resident_details_view(request):
    return render(request, "treasurer/Tresident_update.html")

def treasurer_update_resident_educ_view(request):
    return render(request, "treasurer/Tresident_update_educ.html")


#------------CAPTAIN--------
def captain_dashboard_view(request):
    return render(request, "captain/Cdashboard.html")

def captain_resident_view(request):
    return render(request, "captain/Cresident.html")

def captain_logs_view(request):
    return render(request, "captain/Clogs.html")

def captain_resident_details_view(request):
    return render(request, "captain/Cresident_details.html")

def captain_resident_children_view(request):
    return render(request, "captain/Cresident_children.html")

def captain_resident_parents_view(request):
    return render(request, "captain/Cresident_parents.html")

def captain_resident_husband_view(request):
    return render(request, "captain/Cresident_husband.html")

#----------------SECRETARY----------------
def secretary_dashboard_view(request):
    return render(request, "secretary/Sdashboard.html")

def secretary_resident_view(request):
    return render(request, "secretary/Sresident.html")

def secretary_logs_view(request):
    return render(request, "secretary/Slogs.html")

def secretary_resident_details_view(request):
    return render(request, "secretary/Sresident_details.html")

def secretary_resident_husband_view(request):
    return render(request, "secretary/Sresident_husband.html")

def secretary_resident_children_view(request):
    return render(request, "secretary/Sresident_children.html")

def secretary_resident_parents_view(request):
    return render(request, "secretary/Sresident_parents.html")


#----------------BHW----------------
def bhw_dashboard_view(request):
    return render(request, "BHW/Bdashboard.html")

def bhw_resident_view(request):
    return render(request, "BHW/Bresident.html")

def bhw_resident_details_view(request):
    return render(request, "BHW/Bresident_details.html")

def bhw_resident_husband_view(request):
    return render(request, "BHW/Bresident_husband.html")

def bhw_resident_children_view(request):
    return render(request, "BHW/Bresident_children.html")

def bhw_resident_parents_view(request):
    return render(request, "BHW/Bresident_parents.html")


#----------------STAFF----------------
def staff_dashboard_view(request):
    return render(request, "staff/STdashboard.html")

def staff_resident_view(request):
    return render(request, "staff/STresident.html")

def staff_resident_details_view(request):
    return render(request, "staff/STresident_details.html")

def staff_resident_husband_view(request):
    return render(request, "staff/STresident_husband.html")

def staff_resident_children_view(request):
    return render(request, "staff/STresident_children.html")

def staff_resident_parents_view(request):
    return render(request, "staff/STresident_parents.html")