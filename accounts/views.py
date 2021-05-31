from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        passwd = request.POST.get("passwd")
        user = User.objects.create_user(username, email, passwd)
        user.save()
        return redirect("freeboard:index")
    else:
        return render(request, "accounts/signup.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passwd = request.POST.get("passwd")
        user = authenticate(username=username, password=passwd)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("freeboard:index")
        else:
            # No backend authenticated the credentials
            pass
    else:
        return render(request, "accounts/login.html")

def user_logout(request):
    user = get_user(request)
    if user.is_authenticated:
        logout(request)
    return redirect("freeboard:index")

def myaccount(request):
    return render(request, "accounts/myaccount.html")