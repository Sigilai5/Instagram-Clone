from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def home(request):
    image = Image.objects.all()


    return render(request, 'home.html',locals())

def profile(request):

    return render(request,'profile.html')

@login_required(login_url='/accounts/login/')
def image(request, image_idz):
    return  render(request,'registration/login.html')

