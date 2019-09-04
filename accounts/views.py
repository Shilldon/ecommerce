from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def index(request):
    #Return the index.html file
    return render(request,"index.html")
    
@login_required
# decorator that ensures the page is not displayed if the user is logged out.
# it redirects to log in page (not sure how... - default setting in django)
def logout(request):
    """Log the user out"""
    
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('index'))

def login(request):
    """Return a log in page"""
    
    
    # login_form = UserLoginForm()
    
    if request.user.is_authenticated:
        #checks if user is logged in. If they are it returns to index page to ensure we do not display log in page to a logged in user
        # jinja templating helps but this ensures if they type in the login in address in the bar they are returned to the index page
        return redirect(reverse('index'))
    
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], 
                                     password=request.POST['password']) # 
            #authenticate will return a user object
                                     
            if user:
                # check if user object exists.
                messages.success(request, "You have successfully logged in!")
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else: 
                login_form.add_error(None, "Your username or password is incorrect")  
                # None means it will display on the form rather a specific input
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


def registration(request):
    """render the regstration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
        
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})

def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    return render(request,'profile.html', {"profile": user})