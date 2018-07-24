from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import NewImageForm,CommentForm,SignupForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

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
            print('valid')
            comment = form.cleaned_data['comment']
            saving = Comments(comment=comment)
            saving.save()
    else:

        form = CommentForm()

    return render(request, 'home.html',{"commentform":form,"image":image,"comment":comment})

def profile(request):
    image = Image.objects.all()

    # other_user = User.objects.get(pk=1)
    # Friend.objects.add_friend(
    #     request.user,
    #     other_user,
    #     message='Hello! can we be friends?'
    # )
    #
    # friend_request = FriendshipRequest.objects.get(pk=1)
    # friend_request.accept()

#    friend_request.reject()


    return render(request,'profile.html',locals())

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

            redirect('home.html')

    else:
        form = NewImageForm()



    return render(request, 'new_image.html',locals())



