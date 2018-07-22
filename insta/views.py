from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    print(User)

    return render(request, 'home.html')

def profile(request):

    return render(request,'profile.html')

@login_required(login_url='/accounts/login/')
def image(request, image_idz):
    return  render(request,'registration/login.html')

