from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Registration
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():  # checking the userid with existing userid in database
                messages.info(request, 'User already exist!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():  # checking the email with existing email in database
                messages.info(request, 'Email already exist!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password1)  # add user data to database
                user.save()
                messages.info(request, 'User created!')
                return redirect('login')
        else:
            messages.info(request, "Password doesn't matched")  # Display message on screen
            return redirect('register')
    return render(request, 'register.html')


# login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)  # checking the login data with database
        if user is not None:
            auth.login(request, user)
            return redirect('employee_data')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'login.html')


# logout
def logout(request):
    auth.logout(request,)
    return redirect('/')


def index(request):
    return render(request, 'Home.html')
