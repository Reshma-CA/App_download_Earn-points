from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
# Create your views here.




def admin_add_view(request):
    return render(request, 'djadmin/add_app.html')


@never_cache
def admin_login_view(request):
    if 'username' in request.session:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Attempt to get the user from the People model
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'djadmin/admin_login.html')

        # Check if the password matches using check_password
        if user and check_password(password, user.password):
            request.session['username'] = username
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'user/user_login.html')

    return render(request, 'djadmin/admin_login.html')


@never_cache
def admin_dashbord_view(request):
    if 'username' in request.session:
        return render(request, 'djadmin/admin.html')
    return redirect('admin_login')




def admin_logout_view(request):
    if 'username' in request.session:
        request.session.flush()
    return render(request, 'djadmin/admin_login.html')
