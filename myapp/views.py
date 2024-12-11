from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
       if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('home')
       return render(request,'register.html')

def login_user(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return redirect('login')
        return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('home') 
