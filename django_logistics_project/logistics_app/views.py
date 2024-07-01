from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


@login_required
def index_view(request):
    return render(request, "index.html")


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        existing_user = User.objects.filter(username=username, email=email).first()
        if existing_user:
            return redirect('login_view')
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return redirect('login_view')
    return render(request, "register.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index_view')
        return redirect('login_view')
    return render(request, "login.html")


@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('login_view')


@login_required
def contact_view(request):
    return render(request, "contact.html")


@login_required
def about_view(request):
    return render(request, "about.html")


@login_required
def ship_view(request):
    return render(request, "ship.html")


@login_required
def testimonial_view(request):
    return render(request, "testimonial.html")