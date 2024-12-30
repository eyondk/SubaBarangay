from django.shortcuts import render

from django.shortcuts import render



def index(request):
    return render(request,"secretary/secretary.html")

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

def treasurer_resident_details_view(request):
    return render(request, "treasurer/Tresident_details.html")

def treasurer_resident_children_view(request):
    return render(request, "treasurer/Tresident_children.html")

def treasurer_resident_parents_view(request):
    return render(request, "treasurer/Tresident_parents.html")

def treasurer_resident_husband_view(request):
    return render(request, "treasurer/Tresident_husband.html")

# ==========CAPTAIN==============
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



