from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

def sign_up(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        new_user = User(username = username)
        new_user.set_password(password)

        new_user.save()
        login(request, new_user)
        messages.success(request, "Your profile was created.")
        
        return redirect("index")
    
    context = {
            "form": form
        }
    
    return render(request, "signup.html", context)
        
    """    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            new_user = User(username = username)
            new_user.set_password(password)

            new_user.save()
            login(request, new_user)
            return redirect("index")
        
        context = {
            "form": form
        }

        return render(request, "signup.html", context)

    else:
        form = SignUpForm()
        context = {
            "form": form
        }

        return render(request, "signup.html", context)
    """

def log_in(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password)

        if user is None:
            messages.warning(request, "Username and/or password is/are not correct.")
            return render(request, "login.html", context)
        
        messages.success(request, "You have successfully logged in.")
        login(request, user)

        return redirect("index")

    return render(request, "login.html", context)


def log_out(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")

    return redirect("index")

