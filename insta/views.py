from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def image(request, image_idz):
    return  render(request,'registration/login.html')

