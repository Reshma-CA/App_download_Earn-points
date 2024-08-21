from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from .models import Category, SubCategory, App,People,UserProfile,Task

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

from django.conf import settings


# Create your views here.



def profile(request):
    if 'username' in request.session:
        username = request.session["username"]
        try:
            # Retrieve the UserProfile object associated with the username
            user_profile = UserProfile.objects.get(user__username=username)

            # Get the number of points and completed tasks
            user_points = user_profile.user_points
            tasks_completed = user_profile.tasks_completed

            context = {
                "person_name": user_profile.user.username,  # Display the username
                "user_points": user_points,
                "tasks_completed": tasks_completed,
                
            }
            
            return render(request, 'user/profile.html', context)
        except UserProfile.DoesNotExist:
            # Handle case where the user profile does not exist
            return redirect('home')
    else:
        # Redirect to home if username is not in session
        return redirect('home')

def points(request):
    if 'username' in request.session:
        username = request.session["username"]
        try:
            # Retrieve the UserProfile object associated with the username
            user_profile = UserProfile.objects.get(user__username=username)

            # Get the number of points and completed tasks
            user_points = user_profile.user_points

            context = {
                "person_name": user_profile.user.username,  # Display the username
                "user_points": user_points,                
            }
            
            return render(request, 'user/points.html', context)
        except UserProfile.DoesNotExist:
            # Handle case where the user profile does not exist
            return redirect('home')
    else:
        # Redirect to home if username is not in session
        return redirect('home')
   
def task(request):
    if 'username' in request.session:
        username = request.session["username"]
        try:
            person = People.objects.get(username=username)
            all_Apps= App.objects.all()
            context = {"person_name": person.username,"all_Apps": all_Apps}
            return render(request, 'user/task.html', context)
        except People.DoesNotExist:
            # Handle case where the user does not exist
            return redirect('user_login')
    
    return render(request, 'user/task.html')



def complete_task(request, app_id):
    if 'username' in request.session:
        username = request.session["username"]
        try:
            # Get the user and their profile
            person = People.objects.get(username=username)
            user_profile = UserProfile.objects.get(user=person)

            # Get the task (App)
            app = App.objects.get(id=app_id)

            # Check if the user has enough points to complete the task
            if user_profile.user_points >= app.points:
                if request.method == 'POST' and 'screenshot' in request.FILES:
                    # Handle file upload
                    screenshot = request.FILES['screenshot']
                    fs = FileSystemStorage()
                    filename = fs.save(screenshot.name, screenshot)

                    # Award fixed points for task completion
                    points_awarded = 50
                    
                    # Create a new task object
                    task = Task.objects.create(
                        name=f"Task for {app.name}",
                        app=app,
                        screenshot=screenshot,
                        user_profile=user_profile,
                        completed=True,  # Automatically mark as completed
                        points_awarded=points_awarded  # Fixed points awarded for completion
                    )

                    # Update user's points and task count
                    user_profile.user_points += points_awarded
                    user_profile.tasks_completed += 1
                    user_profile.save()

                    # Success context
                    context = {
                        "person_name": person.username,
                        "app": app,
                        "task": task,
                        "user_profile": user_profile,
                        "message": "Task completed successfully!"
                    }

                    return render(request, 'user/task_complete.html', context)
                else:
                    # If GET request, render the task form
                    context = {
                        "person_name": person.username,
                        "app": app,
                    }
                    return render(request, 'user/task_done.html', context)
            else:
                # If the user doesn't have enough points, render task_not.html
                context = {
                    "person_name": person.username,
                    "app": app,
                    "message": "You do not have enough points to complete this task."
                }
                return render(request, 'user/task_not.html', context)

        except People.DoesNotExist:
            return redirect('user_login')
        except App.DoesNotExist:
            return redirect('task')

    return redirect('user_login')
    
def app_downloader(request):
    if 'username' in request.session:
        username = request.session["username"]
        try:
            person = People.objects.get(username=username)
            context = {"person_name": person.username}
            return render(request, 'user/app_downloader.html', context)
        except People.DoesNotExist:
            # Handle case where the user does not exist
            return redirect('user_login')
    return redirect('user_login')



@csrf_exempt
def user_signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        # Check if passwords match
        if password == confirm_password:
            # Create a new People instance with hashed password
            user = People(
                username=username,
                email=email,
                password=make_password(password)  # Hashing the password
            )
            user.save()
            # Create a UserProfile with initial points
            UserProfile.objects.create(user=user, user_points=100)
            return redirect('user_login')  # Redirect to login page after successful signup

    return render(request, 'user/user_signup.html')  # 


@never_cache
def user_login_view(request):
    if 'username' in request.session:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Attempt to get the user from the People model
        try:
            user = People.objects.get(username=username)
        except People.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'user/user_login.html')

        # Check if the password matches using check_password
        if user and check_password(password, user.password):
            request.session['username'] = username
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'user/user_login.html')

    return render(request, 'user/user_login.html')

def user_logout_view(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('user_login')

@never_cache
def user_home_view(request):
    if 'username' in request.session:
        username = request.session["username"]
        try:
            person = People.objects.get(username=username)
            context = {"person_name": person.username,}
            return render(request, 'user/home.html', context)
        except People.DoesNotExist:
            # Handle case where the user does not exist
            return redirect('user_login')
    return redirect('user_login')



def Welcome_page(request):
    return render(request, 'user/intro_page.html')  
