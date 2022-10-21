from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import NewUser

# Create your views here.

def index(req):
    if req.method == 'POST':
        email = req.POST['email']
        password = req.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('home')
        else:
            messages.info(req, 'invalid credentials')
            return redirect('/')
    
    
    return render(req, 'login.html')

def register(req):
    if req.method == 'POST':
        password1 = req.POST['password1']
        password2 = req.POST['password2']
        firstname = req.POST['tname']
        email= req.POST['email']
        image = req.FILES.get('image')
        username = firstname
        if password1 == password2:
            if NewUser.objects.filter(username=username).exists():
                messages.info(req, 'Username taken')
                return redirect('register')
            elif NewUser.objects.filter(email = email).exists():
                messages.info(req, 'Email taken')
                return redirect('register')
            else:
                NewUser.objects.create_user(username=username, firstname=firstname, email=email, password=password1, img = image)
                return redirect('/')
                # user.save()
        else:
            messages.info(req, 'Passwords dont match')
            return redirect('register')
    else:
        return render(req, 'register.html')
    
def home(req):
    return render(req, 'index.html')