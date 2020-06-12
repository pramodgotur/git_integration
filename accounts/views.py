from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            context["message"] = "Invalid credentials"
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)
