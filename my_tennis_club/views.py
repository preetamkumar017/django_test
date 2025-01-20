from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.sessions.backends.db import SessionStore
from configuration.models import InternalUser
from configuration.utils import get_database_connection


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Username: {username}, Password: {password}")

        try:
            connection = get_database_connection('preetam.com')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM framework.internal_user WHERE username = %s", [username])
            user_data = cursor.fetchone()

            # Debug print the whole user_data
            print(f"User Data: {user_data}")

            # if user_data:
            #     stored_password = user_data[2]  # Assuming user_data[2] is the stored password
            #     print(f"Stored Password: {stored_password}")
            #     print(f"Entered Password: {password}")

            #     if check_password(password, stored_password):  # Securely compare the password
            #         print("Password matched")
            #         institute_id = user_data[0]  # Institute ID
            #         # id1 = user_data[1]  #÷ Institute ID
            #         username = user_data[1]  # Username

            #         # Check if institute_id and username are valid and not None
            #         if institute_id is not None and username is not None:
            #             print(f"Institute ID: {institute_id}")
            #             print(f"Username: {username}")

            #             # Simulate creating a user object for Django's session system
            #             user = InternalUser(
            #                 institute_id=institute_id,
            #                 # id=id1,
            #                 username=username,
            #                 # created_by=0,  # Default value
            #                 # modified_by=0,  # Default value
            #             )
            #             user.suspended = user_data[3]  # Example: assigning additional fields
            #             user.save()
            #             # Store user ID and institute_id in the session
            #             if user.id is not None:
            #                 request.session['user_id'] = user.id
            #             request.session['institute_id'] = user.institute_id
            #             request.session['username'] = user.username

            #             print("User logged in successfully")
            #             return redirect('home')  # Redirect to the home page
            #         else:
            #             error_message = 'Missing required information (Institute ID or Username).'

            #     else:
            #         error_message = 'Invalid username or password'

            # else:
            #     error_message = 'Invalid username or password'

        except Exception as e:
            error_message = f"Error: {str(e)}"
            print(f"Error: {e}")


    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'secure/home.html')
