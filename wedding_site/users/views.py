
def is_event_admin(user):
    return user.is_authenticated and getattr(user, 'is_event_admin', False)

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_event_admin:
            login(request, user)
            # 返回带跳转的模板
            return render(request, 'registration/admin_login.html', {'redirect_url': '/events_manage/'})
        else:
            return render(request, 'registration/admin_login.html', {'error': '用户名或密码错误，或无管理员权限'})
    return render(request, 'registration/admin_login.html')
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('event_list')  # Redirect to the event list after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('event_list')  # Redirect to the event list after login
        else:
            return HttpResponse("Invalid login")
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout