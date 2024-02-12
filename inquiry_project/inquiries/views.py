from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import inquiries
from inquiries.models import enquiry
from .forms import EnquiryForm 
from django.contrib import messages

# Create your views here.


@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')


def enquiry_view(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Enquiry submitted successfully!')
            return redirect('enquiry') 
    else:
        form = EnquiryForm() 
        return render(request, 'enquiry.html', {'form': form})


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("password does not match")
        
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')


    return render(request,'signup.html')

 
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username = username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            # return HttpResponse("username or password is incorrect!")
            error = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error': error})
    else:
        
        return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')




# show data on webpage from database


# myapp/views.py

def my_view(request):
    data = enquiry.objects.all()
    return render(request, 'home.html', {'data': data})