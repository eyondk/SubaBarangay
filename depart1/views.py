from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request,"secretary/secretary.html")

def treasurer_dashboard_view(request):
    return render(request, "treasurer/Tdashboard.html")

def treasurer_resident_view(request):
    return render(request, "treasurer/Tresident.html")
