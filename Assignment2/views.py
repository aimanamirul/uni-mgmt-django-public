from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404, get_list_or_404
from Assignment2.forms import AdminForm
from Assignment2.models import Course, University, UniversityCourse, Admin
from django.utils.crypto import get_random_string

# Create your views here.
def createInterface(request): #Create or Add Unversities details
    return render(request,'Assignment2/CreatePage - Prototype.html',{
        'Universities': University.objects.all(),
        'Courses': Course.objects.all()
    })
    return render(request,'Assignment2/CreatePage.html',{
        'VariableName': ''
    })

def viewInterface(request): #View Unversities details
    admin = None
    if 'admin_id' in request.session:
        admin = Admin.objects.get(AdminID=request.session['admin_id'])

    return render(request,'Assignment2/ViewPage.html',{
        'admin': admin,
        'VariableName': ''
    })

def editInterface(request, mode, id=None): #Edit Unversities/Courses details
    if mode == 'university':
        obj = get_object_or_404(University, pk=id) if id else None
    elif mode == 'course':
        obj = get_object_or_404(Course, pk=id) if id else None
    else:
        obj = None

    print(obj)

    return render(request,'Assignment2/EditPage.html',{
        'mode': mode,
        'id': id,
        'obj': obj,
    })

def deleteInterface(request):
    return render(request,'Assignment2/DeletePage - Prototype.html',{
        'Universities': University.objects.all(),
        'Courses': Course.objects.all(),
        'FirstCourse': (lambda UC : (
            None if  UC == None else UniversityCourse.objects.filter(University = University.objects.all().first()).first().Course.CourseCode
        ))(UniversityCourse.objects.filter(University = University.objects.all().first()).first()),
        'UniversityCourse': UniversityCourse.objects.all()
    })

# Register new admin
def create_admin_account(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()

        if not username:
            messages.error(request, 'Username is required.')
        elif len(username) < 4:
            messages.error(request, 'Username must be at least 4 characters long.')
        elif Admin.objects.filter(Username=username).exists():
            messages.error(request, 'Username not available.')
        elif not password:
            messages.error(request, 'Password is required.')
        elif len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long.')
        else:
            token = get_random_string(32)  # Generating a random token
            # Create the Admin object and save the hashed password
            admin = Admin.objects.create(Username=username)
            admin.set_password(password)
            admin.Token = token
            admin.save()

            messages.success(request, 'Admin account created successfully!')
            return redirect('create_login')
        
        # If validation fails, stay on the registration page
        return redirect('create_admin')
    
    return render(request, 'Assignment2/create_admin.html')
    # return render(request, 'Assignment2/admin_login.html')

# Admin login
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()

        if not username:
            messages.error(request, 'Username is required.')
        elif not password:
            messages.error(request, 'Password is required.')
        elif len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long.')
        else:
            try:
                admin = Admin.objects.get(Username=username)
            except Admin.DoesNotExist:
                messages.error(request, 'Invalid username or password.')
                return redirect('create_login')  # Redirect back to the login page
                # return HttpResponse('Invalid credentials', status=401)
            
            if admin.check_password(password):
                # On successful login, create a session or token and redirect
                request.session['admin_id'] = admin.AdminID
                return redirect('ViewInterface')  # Redirect to the admin's view interface
            else:
                messages.error(request, 'Invalid username or password') 

        return redirect('create_login')  # Redirect back to the login page
        
        # return HttpResponse('Invalid credentials', status=401)
    return render(request, 'Assignment2/admin_login.html')

# Logout
def logout_view(request):
    # Clear the session for the logged-in admin
    if 'admin_id' in request.session:
        del request.session['admin_id']
    return redirect('create_login')  # Redirect to the login page
