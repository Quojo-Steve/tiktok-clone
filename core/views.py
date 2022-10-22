from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import VideoUpload
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(req):
    if req.method == 'POST':
        username = req.POST['tname']
        password = req.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('/')
        else:
            messages.info(req, 'invalid creds')
    
    
    return render(req, 'login.html')

def register(req):
    if req.method == 'POST':
        password1 = req.POST['password1']
        password2 = req.POST['password2']
        username = req.POST['tname']
        email= req.POST['email']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(req, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(req, 'Email taken')
                return redirect('register')
            else:
                User.objects.create_user(username=username, email=email, password=password1)
                return redirect('login')
                # user.save()
        else:
            messages.info(req, 'Passwords dont match')
            return redirect('register')
    else:
        return render(req, 'register.html')
    
def home(req):
    return render(req, 'index.html')

@login_required(login_url='login')
def upload(req):
    if req.method == 'POST':
        video = req.FILES.get('video')
        description = req.POST['description']
        
        post = VideoUpload.objects.create(video = video, description = description)
        post.save()
        return redirect('/')
        
    return render(req, 'upload.html')

def logout(req):
    auth.logout(req)
    return redirect('login')