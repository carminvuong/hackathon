from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return HttpResponseRedirect('/home/')
        else:
            messages.error(
                request, "Unsuccessful registration. Invalid information.")
    else:
        form = SignupForm()
    return render(request, "signup/signup.html", {"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/home/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="signup/login.html", context={"login_form": form})
