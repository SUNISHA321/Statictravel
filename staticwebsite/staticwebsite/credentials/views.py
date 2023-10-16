from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect("register")
            else:
                user=User.objects.create(username=username,
                                 first_name=first_name,
                                 last_name=last_name,
                                 email=email)
                user.set_password(password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password not match")

    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')


