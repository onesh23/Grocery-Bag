from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            try:
                User.objects.get(username=username)
                messages.error(request,'User Alredy Exists')
            except:
                User.objects.create_user(username=username,password=password)
                messages.success(request,'Reistered Successful')
                return redirect('signin')
        else:
            messages.error(request,'Username and Password Required')
    return render(request,'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.error(request,'Please Enter valid Username and Password')
        else:
            messages.error(request,'Both Fields are Required')
    return render(request,'signin.html')



def signout(request):
    logout(request)
    messages.info(request,'Logout Successful')
    return redirect('signin')