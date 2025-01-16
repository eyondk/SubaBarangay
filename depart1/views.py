from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlencode
from django.db import connection
from django.contrib import messages
from django.db.models import Count, Case, When
from .models import Resident
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from django.utils.timezone import now
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import redirect
from django.contrib.auth import logout


logger = logging.getLogger('depart1')



def index(request):
    return render(request,"shared/login_page.html")

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

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


#-----------USER--------------
def user_details_view(request):
    return render(request, "shared/user_details.html")

#not using
def update_user(request, user_id):
    # Simulate user data (normally fetched from a database)
    user_data = {
        "id": user_id,
        "lname": "PADILLA",
        "fname": "YRON",
        "mname": "IGOT",
        "username": "YRONIE",
        "status": "active"
    }

    if request.method == 'POST':
        print("Updated Data:", request.POST)
        return render(request, 'treasurer/Tusers.html')  # Use a template to show success

    return render(request, 'treasurer/Tusers.html', {"user": user_data})


#------------TREASURER--------
def treasurer_dashboard_view(request):
        username = request.GET.get('username')
        role_name = request.GET.get('role_name')
        with connection.cursor() as cursor:
            # Execute the stored procedure and fetch results
            cursor.execute("SELECT * FROM get_resident_analytics()")
            result = cursor.fetchone()

            # Map the result to context variables
            resident_data = {
                'women': result[0],
                'erpat': result[1],
                'senior_citizen': result[2],
                'pwd': result[3],
                'lgbtq': result[4],
                'children': result[5],
            }

            # Historical data for predictive analysis (example data; replace with real historical data)
            historical_data = {
                'women': [200, 210, 220, 230, 240],
                'erpat': [150, 155, 160, 165, 170],
                'senior_citizen': [120, 125, 130, 135, 140],
                'pwd': [50, 55, 60, 65, 70],
                'lgbtq': [80, 85, 90, 95, 100],
                'children': [300, 310, 320, 330, 340],
            }

            future_predictions = {}
            current_time = now()

            # Perform predictive analysis for each category
            for category, data in historical_data.items():
                # Create X (years) and y (counts)
                years = np.array(range(1, len(data) + 1)).reshape(-1, 1)
                counts = np.array(data)

                # Train a linear regression model
                model = LinearRegression()
                model.fit(years, counts)

                # Predict for the next year
                next_year = np.array([[len(data) + 1]])
                future_count = model.predict(next_year)

                # Store the predicted value
                future_predictions[category] = int(future_count[0])

            # Add both resident data and predictions to the context
            context = {
                'resident_data': resident_data,
                'predictions': future_predictions,
                'current_time': current_time,
                'username': username,
                'role_name': role_name,
            }

        return render(request, "treasurer/Tdashboard.html", context)

  


    


def treasurer_resident_view(request):
    search_query = request.GET.get('search', None)
    org_filter = request.GET.get('org', None)
    
    residents = []
    total_residents = 0

    try:
        with connection.cursor() as cursor:
            # Fetch filtered residents
            cursor.execute(
                "SELECT * FROM GetResidents(%s, %s)",
                [search_query, org_filter]
            )
            rows = cursor.fetchall()
            
            for row in rows:
                residents.append({
                    'id': row[0],
                    'last_name': row[1],
                    'first_name': row[2],
                    'middle_name': row[3],
                    'organization': row[4],
                })
            
            # Fetch total residents count
            cursor.execute("SELECT COUNT(*) FROM RESIDENT")
            total_residents = cursor.fetchone()[0]
            
            print(f"Total residents: {total_residents}")  # Debugging line
    except Exception as e:
        print(f"Error fetching data: {e}")  # Debugging line for exceptions

    return render(request, "treasurer/Tresident.html", {
        'residents': residents,
        'total_residents': total_residents,
    })

def treasurer_logs_view(request):
    return render(request, "treasurer/Tlogs.html")



def treasurer_users_view(request):
    return render(request, "treasurer/Tusers.html")

def add_user(request):
    if request.method == 'POST':
        # Retrieve form data
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        role_name = request.POST.get('role')

        # Log incoming data (sensitive data like passwords are intentionally omitted)
        logger.info(f"Received form data: last_name={last_name}, first_name={first_name}, middle_name={middle_name}, username={username}, role={role_name}")

        try:
            # Execute stored procedure
            with connection.cursor() as cursor:
                cursor.execute(
                    "CALL add_user(%s, %s, %s, %s, %s, %s);",
                    [last_name, first_name, middle_name, username, password, role_name]
                )
            logger.info(f"User '{username}' added successfully with role '{role_name}'.")
            messages.success(request, "User added successfully!")
            return redirect('Tusers')

        except Exception as e:
            # Log the error
            logger.error(f"Error occurred while adding user '{username}': {str(e)}")
            messages.error(request, f"Error adding user: {str(e)}")
            return render(request, 'treasurer/Tusers.html')

    # Log access to the form
    logger.info("Rendering the add user form.")
    return render(request, 'treasurer/Tusers.html')


def treasurer_payments_view(request):
    return render(request, "treasurer/Tpayments.html")
    
def treasurer_organization_view(request):
    return render(request, "treasurer/Torganization.html")



def treasurer_resident_details_view(request):
    return render(request, "treasurer/Tresident_details.html")

@csrf_exempt
def save_resident_data(request):
    if request.method == 'POST':
        try:
            # Parse incoming JSON data
            data = json.loads(request.body)

            # Transform flat address fields into a nested structure if needed
            if 'address' not in data:
                data['address'] = {
                    'block': data.get('block'),
                    'street': data.get('street'),
                    'houseNumber': data.get('houseNumber')
                }

            address = data['address']

            # Validate required address fields
            if not address['block'] or not address['street'] or not address['houseNumber']:
                return JsonResponse({'success': False, 'error': "Address fields ('block', 'street', 'houseNumber') are required."})

            # Organization and religion mappings (with trapping)
            organization_map = {
                "Children": 1,
                "Erpats (Father's Association)": 2,
                "LGBTQ": 3,
                "Person with Disabilities": 4,
                "Senior Citizens": 5,
                "Women's": 6,
                "Erpat": 2  # Add shorthand mapping
            }

            # Map organization input to ID
            data['organization'] = organization_map.get(data['organization'])
            if data['organization'] is None:
                return JsonResponse({
                    'success': False,
                    'error': f"Invalid organization: '{data['organization']}'. Valid options are: {list(organization_map.keys())}"
                })

            religion_map = {
                "Roman Catholic": 1,
                "Catholic": 1,  # Maps "Catholic" to "Roman Catholic"
                "Iglesia ni Cristo": 2,
                "Protestant": 3,
                "Born Again Christian": 4,
                "Evangelical Christian": 5,
                "Seventh-day Adventist": 6,
                "Jehovah's Witness": 7,
                "Aglipayan": 8,
                "Church of Jesus Christ of Latter-day Saints (Mormon)": 9,
                "Islam": 10,
                "Judaism": 11,
                "Buddhism": 12,
                "Other": 13
            }

            # Map religion input to ID (ensure case-insensitivity)
            data['religion'] = religion_map.get(data['religion'].strip().title(), None)
            if data['religion'] is None:
                return JsonResponse({'success': False, 'error': f"Invalid religion: {data['religion']}. Please use one of {list(religion_map.keys())}"})

            # Handle sex (gender-specific)
            sex_map = {
                'Male': 'Male',
                'Female': 'Female',
                'Lesbian': 'Female',  # Map 'Lesbian' to 'Female'
                'Gay': 'Male',        # Map 'Gay' to 'Male'
            }

            data['sex'] = sex_map.get(data['sex'], None)

            # Validate education fields and trap missing or invalid data
            if 'education' not in data:
                return JsonResponse({'success': False, 'error': "Education information is missing."})

            # Check required education fields
            education = data['education']

            required_education_fields = ['schoolLevel', 'schoolName', 'schoolAddress', 'schoolYear']
            for field in required_education_fields:
                if field not in education or not education[field]:
                    return JsonResponse({'success': False, 'error': f"Missing or invalid education field: {field}"})

            # Check if school year is valid (4-digit year)
            if len(education['schoolYear']) != 4 or not education['schoolYear'].isdigit():
                return JsonResponse({'success': False, 'error': "Invalid school year. It must be a 4-digit year."})

            # Map education level to valid options (with trapping)
            valid_education_levels = [
                'Nursery', 'Elementary', 'Junior High School', 'Senior High School', 
                'Undergraduate (Bachelor’s Degree)', 'Postgraduate (Master’s Degree)', 
                'Doctoral (PhD)', 'Alternative Learning System (ALS)'
            ]
            if education['schoolLevel'] not in valid_education_levels:
                return JsonResponse({'success': False, 'error': f"Invalid school level: {education['schoolLevel']}. Valid options are: {valid_education_levels}"})

            # Prepare parameters for the stored procedure
            resident_params = (
                data['lastName'],                   # p_res_lname
                data['firstName'],                  # p_res_fname
                data.get('middleName', None),       # p_res_mname
                data.get('nickname', None),         # p_res_nickname
                data['birthdate'],                  # p_res_dob
                data['sex'],                        # p_res_sex
                data['gender'],                     # p_res_gender
                data['religion'],                   # p_relig_id
                data['civilStatus'],                # p_res_civil_status
                data['weight'],                     # p_res_weight
                data['eyeColor'],                   # p_res_eye_color
                data['bloodType'],                  # p_res_blood_type
                data['organization'],               # p_org_id
                address['block'],                   # p_add_block
                address['street'],                  # p_add_street
                address['houseNumber'],             # p_add_h_num
                data.get('isOwner', 'Not Owner'),   # p_res_isowner
                education['schoolLevel'],           # p_educ_sch_level
                education['schoolName'],            # p_educ_sch_name
                education['schoolAddress'],         # p_educ_sch_address
                education.get('course', None),      # p_educ_course
                education['schoolYear'],            # p_educ_sch_year
                data.get('userId', None)            # p_user_id
            )

            # Call the stored procedure
            with connection.cursor() as cursor:
                cursor.callproc('insert_resident', resident_params)

            return JsonResponse({'success': True, 'message': 'Resident data saved successfully.'})

        except KeyError as e:
            return JsonResponse({'success': False, 'error': f"Missing required field: {str(e)}"})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})




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

def secretary_resident_add_resident_view(request):
    return render(request, "secretary/SaddResident_details.html")

def secretary_resident_add_educ_view(request):
    return render(request, "secretary/SaddEduc_details.html")

def secretary_update_resident_details_view(request):
    return render(request, "secretary/Sresident_update.html")

def secretary_update_resident_educ_view(request):
    return render(request, "secretary/Sresident_update_educ.html")


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