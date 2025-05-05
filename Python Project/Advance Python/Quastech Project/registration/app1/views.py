from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    # Example: Accessing user-specific data from the session
    user_preference = request.session.get('user_preference', 'default_preference')  # session
    return render(request, 'home.html', {'user_preference': user_preference})

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not same!!")
        else:
            # print(uname, email, pass1, pass2)

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()

            # return HttpResponse("User has been created successfully!!!")

            # Store user-related data in the session  # session
            request.session['user_preference'] = 'default_preference'  # session

            return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')

        # print(username, pass1)

        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            # Store user-related data in the session upon successful login  # session
            request.session['user_preference'] = 'default_preference'  # session
            return redirect('home')
        else:
            return HttpResponse("Username and password is incorrect!!")

    return render(request, 'login.html')

@login_required(login_url='login')
def ServicesPage(request):
    return render(request, 'services.html')

@login_required(login_url='login')
def ContactPage(request):
    return render(request, 'contact.html')

@login_required(login_url='login')
def AboutPage(request):
    return render(request, 'about.html')

def LogoutPage(request):
    # Clear user-related data from the session upon logout  # session
    request.session.pop('user_preference', None)  # session
    logout(request)
    return redirect('login')


'''Session is just use to store temporary files, which ever temporarily file it creates during login and logout process.
It is not compulsory to use session. If you want to use you can use it.
Session is an inbuilt code. Here you are using 'authenticate' so it is mostly similar close to session code only. So you don't need to use it.
But still if they say to use than use it.'''
