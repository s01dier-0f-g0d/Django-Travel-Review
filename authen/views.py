from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate,update_session_auth_hash,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            username = request.POST['username'],
            password = request.POST['password']
        )
        messages.success(request,'Registration Successful')
        return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        customer = authenticate(request,
                                username=request.POST['username'],
                                password=request.POST['password'])
        if customer:
            login(request,customer)
            messages.success(request,'Login Successful')
            return redirect('home')
    return render(request,'signin.html')

@login_required(login_url='signin')
def profile(request):
    return render(request,'profile.html',{'customer':request.user})

@login_required(login_url='signin')
def updateProfile(request):
    if request.method == 'POST':
        customer = request.user
        customer.first_name = request.POST['first_name']
        customer.last_name = request.POST['last_name']
        customer.email = request.POST['email']
        customer.username = request.POST['username']
        return redirect('profile')
    return render(request,'updateProfile.html',{'customer':request.user})

@login_required(login_url='signin')
def updatePass(request):
    if request.method == 'POST':
        customer = request.user
        old_pass = request.POST['old_pass']
        new_pass = request.POST['new_pass']
        confirm_pass = request.POST['confirm_pass']
        if not customer.check_password(old_pass):
            messages.error(request,'Old Password do not match')
        elif new_pass==old_pass:
            messages.error(request,'New Password cannot be same as Old Password')
        elif new_pass!=old_pass and new_pass!=confirm_pass:
            messages.error(request,'New Password must be same as Confirm Password')
        else:
            customer.set_password(new_pass)
            customer.save()
            update_session_auth_hash(request,customer)
            messages.success(request,'Password updated successfully')
            return redirect('profile')
    return render(request,'updatePass.html')

@login_required(login_url='signin')
def signout(request):
    logout(request)

    return redirect('signin')

