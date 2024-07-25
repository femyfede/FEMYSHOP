from django.shortcuts import render,redirect
from .models import User
from .forms import RegForm,LogForm
from django import forms

from django.contrib.auth import authenticate


# Create your views here.
def registration(request):
    if request.method == 'POST':
        print("I")
        form = RegForm(request.POST)
        print("ME")
        if form.is_valid():
            form.save()
            print("fede")
            return redirect('logindjango')
    else:
        form = RegForm()
        return render(request,'pages/regdjango.html',{'form':form})
    return render(request,'pages/regdjango.html',{'form':form})

def login(request):
        if request.method == 'POST':
          form = LogForm(request.POST)
          if form.is_valid():
              UserName = request.POST['UserName']
              password = request.POST['password']
              User = authenticate(request,UserName = UserName,password = password)
              return redirect('home')
          else:
                form.add_error(None, 'Invalid username or password')
        form = LogForm()
        return render(request,'pages/logindjango.html',{'form':form})
def home(request):
    return render(request, 'pages/home.html')

