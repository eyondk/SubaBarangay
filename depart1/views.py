from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request,"secretary/secretary.html")

def treasurer_dashboard_view(request):
    return render(request, "treasurer/Tdashboard.html")

def treasurer_resident_view(request):
    return render(request, "treasurer/Tresident.html")

def treasurer_logs_view(request):
    return render(request, "treasurer/Tlogs.html")

def treasurer_users_view(request):
    return render(request, "treasurer/Tusers.html")

def treasurer_resident_details_view(request): #, resident_id):
    # Fetch resident data by ID from PostgreSQL
    # try:
    #     resident = Resident.objects.get(id=resident_id)
    # except Resident.DoesNotExist:
    #     resident = None  # Handle non-existent resident gracefully
    #return render(request, "treasurer/Tview_resident.html", {"resident": resident})
    return render(request, "treasurer/Tresident_details.html")

def treasurer_resident_husband_view(request):
    return render(request, "treasurer/Tresident_husband.html")

def treasurer_resident_children_view(request):
    return render(request, "treasurer/Tresident_children.html")

def treasurer_resident_parents_view(request):
    return render(request, "treasurer/Tresident_parents.html")

