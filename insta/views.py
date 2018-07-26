from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from friendship.models import Friend, Follow, Block,FriendshipRequest

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Insta Clone account.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/registration_form.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.<a href="/accounts/login/">Login</a>')
    else:
        return HttpResponse('Activation link is invalid,Please try again or login <a href="/accounts/login/">Login</a>!')



# Create your views here.

def home(request):

    image = Image.objects.all()
    comment = Comments.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()

            redirect('home.html')

    else:
        form = CommentForm()

    return render(request, 'home.html',{"form":form,"image":image,"comment":comment})


def profile(request,User):
    image = Image.filter_user(User)

    profile = Profile.objects.all()

    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            prof = form.save(commit=False)
            profile.user = current_user
            profile.save()

    else:
        form = ProfileForm()


    return render(request,'profile.html',locals())


def prof(request):

    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = current_user
            prof.save()

    else:
        form = ProfileForm()


    return render(request,'registration/new_profile.html',locals())




def nav(request,User):

    user = User

    return render(request,'navbar.html',locals())





@login_required(login_url='/accounts/login/')
def image(request):


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

            redirect('/')

    else:
        form = NewImageForm()

    return render(request, 'new_image.html',locals())




def search_users(request):

    # other_user = User.objects.get(pk=1)
    # Friend.objects.add_friend(
    #     request.user,  # The sender
    #     other_user,  # The recipient
    #     message='Hi! I would like to add you')  # This message is optional
    #
    # friend_request = FriendshipRequest.objects.get(pk=1)
    # friend_request.accept()
    # or friend_request.reject()

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")

        articles = Profile.search_users(search_term)

        message = f"{search_term}"

        return render(request, 'search.html',locals() )

    else:
        message = "You have not searched any user"




        return render(request, 'search.html',{"message":message})

