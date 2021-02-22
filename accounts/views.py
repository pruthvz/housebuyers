# imports
import stripe
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from .forms import UserProfileForm, CreateUserForm
from django.contrib import messages

# Create your views here.

# login requests here


def login(request):

    # once the login button is pressed in login.html or 'accounts/login'
    # it will process this login function. first it will check the user and pass and then use the built in authenticate function to authenticate the user.
    # these built in functions have to be imported 'auth'
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        # and if the user doesn't exist within the postgreSQL database, then it will loop back to login.html
        if user is not None:
            # if the pass and username is right then it will login for them. and redirect them to home page
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')


# register requests here
# This function will be processed when the register button is pressed in 'register.html' or 'accounts/register'
def register(request):
    # checks for which request you are making, since the form is a POST request its  checking here.
    if request.method == "POST":
        # checks for the POST request.
        form = CreateUserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        # checks if both the files are valid and all the fields are entered with the correct value
        if form.is_valid() and profile_form.is_valid():
            user = form.save()  # saves the data to the database PostgreSQL.
            # the param 'commit=False' doesn't save the extra field we created it waits here.
            profile = profile_form.save(commit=False)
            # that data is then appendeded into the user form.
            profile.user = user

            # then the entire form is saved here containing the user details and the extra fields like household income etc.
            profile.save()
            # this just grabs the username that was entered.
            username = form.cleaned_data.get('username')
            # if the register is successful then it will prompt that 'the {username} has been successfully registered'
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # redirect back to home page

    else:
        # if the data is wrong, then it will keep looping until its valid.
        form = CreateUserForm()
        profile_form = UserProfileForm()

    # the context contains both the forms that will be displayed in the register.html page
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'register.html', context)


# Logout requests here come here
def logout(request):
    # simple logout request that logs you out and takes you back to home page
    auth.logout(request)
    return redirect('/')
