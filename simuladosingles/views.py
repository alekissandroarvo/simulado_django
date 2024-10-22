from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def login_view(request):
    username = request.POST["name"]
    password = request.POST["senha"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request)
        context = {
            'nome': username.upper() ,
        }
        return render(request, "welcome.html",context)
    else:
        return render(request, "badlogin.html")
