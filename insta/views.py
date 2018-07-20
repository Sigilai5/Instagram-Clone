from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_page(request):

    return render(request, 'registration/login.html')

@login_required(login_url='/accounts/login/')
def image(request, image_id):
    return  render(request,'registration/login.html')

