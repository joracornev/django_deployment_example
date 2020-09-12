from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm
#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse #removed OLD: django.core.urlresolvers
from django.contrib.auth.decorators import login_required#@login_required



# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')


@login_required
def special(request):
    return HttpResponce('You are logged in, Nice!')

##################### view logOut #########################
@login_required#Django BuiltIn Decorator: User must be loged in to be able to logout
def user_logout(request):
    logout(request)
    return(HttpResponse(reverse('index')))


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save() # grab data from user_form
            user.set_password(user.password)# hashing the password
            user.save() # save

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
#
    return render(request, 'basic_app/registration.html',
    {'user_form':user_form,
    'profile_form':profile_form,
    'registered':registered})

##################### view login #########################
def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')# login.html => input => Username
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return(HttpResponseRedirect(reverse('index')))
            else:
                return(HttpResponse('ACCOUNT IS NOT ACTIVE'))
        else:
            print('Someone tried login and failed!')
            print('Username:{} Password:{}'.format(username, password))
            return(HttpResponse('INCORRECT LOGIN DATA SUPPLIED - ERROR'))
    else:
        return (render(request,'basic_app/login.html',{}))
