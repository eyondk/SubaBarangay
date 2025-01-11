from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlencode
from django.db import connection
import logging

logger = logging.getLogger('depart1')



def index(request):
    return render(request,"shared/login_page.html")


from django.db import connection
import logging

logger = logging.getLogger(__name__)

from django.db import connection
import logging

logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            with connection.cursor() as cursor:
                # Call the stored procedure
                cursor.execute("CALL LOGIN_ACCOUNT(%s, %s, %s);", [username, password, 'role_name'])

                # Fetch the result from the OUT parameter
                role_name = cursor.fetchone()[0]  # Fetch the first result from the OUT parameter

                if not role_name:
                    return render(request, 'shared/login_page.html', {'error': 'Failed to retrieve role name.'})
                
                # Store role name in session
                request.session['role_name'] = role_name
                request.session['username'] = username 

                # Redirect based on role
                if role_name == 'Treasurer':
                     query_params = urlencode({'username': username, 'role_name': role_name})
                     return HttpResponseRedirect(f'{reverse("Tdashboard")}?{query_params}')
                elif role_name == 'Barangay Captain':
                    
                    query_params = urlencode({'username': username, 'role_name': role_name})
                    return HttpResponseRedirect(f'{reverse("Cdashboard")}?{query_params}')
                
                elif role_name == 'Secretary':
                    query_params = urlencode({'username': username, 'role_name': role_name})
                    return HttpResponseRedirect(f'{reverse("Sdashboard")}?{query_params}')
                elif role_name == 'Barangay Health Worker':
                     query_params = urlencode({'username': username, 'role_name': role_name})
                     return HttpResponseRedirect(f'{reverse("Bdashboard")}?{query_params}')
                elif role_name == 'Staff':
                     query_params = urlencode({'username': username, 'role_name': role_name})
                     return HttpResponseRedirect(f'{reverse("STdashboard")}?{query_params}')
                else:
                     return HttpResponseRedirect(f'{reverse("Cdashboard")}?{query_params}')

        except Exception as e:
            return render(request, 'shared/login_page.html', {'error': str(e)})

    return render(request, "shared/login_page.html")


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


#------------CAPTAIN--------
def captain_dashboard_view(request):
    username = request.GET.get('username')
    role_name = request.GET.get('role_name')
    
    return render(request, "captain/Cdashboard.html",{'username': username, 'role_name': role_name})

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



