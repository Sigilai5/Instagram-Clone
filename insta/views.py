from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import NewImageForm,CommentForm
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    image = Image.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            print('valid')
        else:
            form =CommentForm()


    return render(request, 'home.html',locals())

def profile(request):
    image = Image.objects.all()

    return render(request,'profile.html',locals())

@login_required(login_url='/accounts/login/')
def image(request, image_idz):
    return  render(request,'registration/login.html')

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.save(commit=False)
            image.owner = current_user
            image.save()

            redirect('home.html')

    else:
        form = NewImageForm()



    return render(request, 'new_image.html',locals())



