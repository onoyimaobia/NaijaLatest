from django.shortcuts import render, redirect
from .forms import ProfilePic
from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_decode
from Music.models import Music, Video, Audio,Confirmemail, Lyrics
from Gist.models import GistPost
from TalkZone.models import TalkZone
from News.models import NewsPosts
from django.contrib.auth.decorators import login_required
from  Music.token import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as auth_login,logout
from django.template.loader import render_to_string
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import ProfilePic



def dashboard(request):
    current_user = request.user
    user_id = current_user.id
    profile_pic = ProfilePic.objects.filter(user_id=user_id)
    context = {'profile_pic': profile_pic}
    template = 'Profile/dash-board.html'
    return render(request, template, context)


def profile(request):
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Profile:login')
    else:
        form = ProfilePic(request.POST, request.FILES)
    return render(request, 'Profile/profil.html', {'form': form})


def sign_up_with_confirmation_mail(request):

    if request.method == 'POST':
        firstname = request.POST['first_name']
        firstname1 = firstname.lower()
        lastname = request.POST['last_name']
        lastname1 = lastname.lower()
        email = request.POST['email']
        email1 = email.lower()
        username = request.POST['username']
        username1 = username.lower()
        password = request.POST['password']
        password1 = password.lower()
        picture = request.POST['picture']

        check_user_exist = User.objects.filter(username=username1).exists()
        if check_user_exist:
            messages.success(request, 'User already exist.')
            return redirect('Music:hip_hop_rap')
        else:
            user = User.objects.create_user(first_name=firstname1, last_name=lastname1, email=email1,
                                                   username=username1, password=password1, is_active=False)
            user.save()
            creat_profile = ProfilePic.objects.create(user_id=user.id, picture=picture)
            creat_profile.save()
            my_group = Group.objects.get(name='Viewers')
            user.groups.add(my_group)
            current_site = get_current_site(request)
            message = render_to_string('Profile/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            subject = 'Activate Your NaijaLatest Account'
            to_email = email
            email = EmailMessage(subject, message, to=[to_email])
            email.send()
            return redirect('Profile:account_activation_sent')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        print('+++++++')
        print(uid)
        print('+++++++')
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        print('Nothing is showing')
        print('-------------------------')
        print(uidb64)
        print('-------------------------')
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        confirm = Confirmemail.objects.create(confirm_email=True, user_id=user)
        confirm.save()

        messages.success(request, 'Registration successful')
        #auth_login(request, user)
        return redirect('Profile:login')
    else:
        return render(request, 'Profile/account_activation_invalid.html')


def account_activation_sent(request):

    return render(request, 'Profile/account_activation_sent.html')


def account_activation_invalid(request):
    return render(request, 'Profile/account_activation_invalid.html')


def login(request):
    template = 'Profile/login.html'
    return render(request, template)


def loginn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                # log user in
                auth_login(request, user)
                return redirect('Profile:user-dashboard')
        else:
            messages.warning(request, 'username or password does not match')
            return redirect('Music:home1')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Kindly click on Login link on the Footer to Login')
        return redirect('Music:home1')



@login_required(login_url='/Profile/login')
def user_dashboard(request):
    current_user = request.user
    user_id = current_user.id
    user_uploaded_song = Audio.objects.all().filter(user_id=user_id)
    user_uploaded_video = Video.objects.all().filter(user_id=user_id)
    user_uploaded_gist = GistPost.objects.all().filter(user_id=user_id)
    user_uploaded_news = NewsPosts.objects.all().filter(user_id=user_id)
    user_uploaded_talk = TalkZone.objects.all().filter(user_id=user_id)
    template = 'Profile/user_dashboard.html'
    context = {'user_uploaded_song': user_uploaded_song, 'user_uploaded_video': user_uploaded_video,
               'user_uploaded_gist': user_uploaded_gist, 'user_uploaded_news': user_uploaded_news,
               'user_uploaded_talk': user_uploaded_talk}
    return render(request, template, context)


def text(request):
    template = 'Profile/test.html'
    current_user = request.user
    user_id = current_user.id
    print(current_user.username)
    user_uploaded_song = Audio.objects.all().filter(user_id=user_id)
    user_uploaded_video = Video.objects.all().filter(user_id=user_id)
    user_uploaded_gist = GistPost.objects.all().filter(user_id=user_id)
    context = {'user_uploaded_song': user_uploaded_song, 'user_uploaded_video': user_uploaded_video,
               'user_uploaded_gist': user_uploaded_gist,}
    return render(request, template, context)


def password_forgot(request):
    template = 'Profile/password_reset_form.html'
    return render(request, template)

def password_reset(request):

    if request.method == 'POST':
        email = request.POST['email']
        get_user_email = User.objects.filter(email=email).exists()
        if get_user_email:
            user_email = User.objects.get(email=email)
            user = user_email.username
            mail = user_email.email
            current_site = get_current_site(request)
            message = render_to_string('Profile/activate_password.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user_email.pk)).decode(),
                'token': account_activation_token.make_token(user_email),
            })
            subject = 'Reset Your Password'
            to_email = mail
            email = EmailMessage(subject, message, to=[to_email])
            email.send()
            return redirect('Profile:password_reset_email')

        else:
            messages.warning(request, 'Email does not exist')
            return redirect('Profile:password_reset_form')


def password_reset_email(request):

    return render(request, 'Profile/password_reset_email.html')


def change_password(request, uidb64, token):
    if request.method == 'POST':
        uid = urlsafe_base64_decode(uidb64).decode()
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            get_user_password = User.objects.get(pk=uid)
            get_user_password.set_password(password)
            get_user_password.save()
            messages.success(request, 'password changed successfull. click on the login blow')
            return redirect('Music:home1')

    return render(request, 'Profile/change_password.html')


def permission(request):
    group = Group.objects.all()
    user = User.objects.all()
    viewer = User.objects.filter(groups__name='Viewers')
    staff = User.objects.filter(groups__name='Special_Users')
    template = 'Profile/permission.html'
    context = {'group': group, 'user': user, 'viewer': viewer, 'staff': staff}
    return render(request, template, context)


def add_user(request):
    if request.method == 'POST':
        user_id = request.POST['users']
        grp = request.POST['Special_Users']
        user = User.objects.get(pk=user_id)
        if grp == "":
            messages.warning(request,'Please select Group')
            return redirect('Profile:permission')
        else:
            if grp == 'Special_Users':
                if user.groups.filter(name='Special_Users').exists():
                    messages.warning(request, 'User already exist')
                    return redirect('Profile:permission')
                else:
                    Add_user = Group.objects.get(name='Special_Users')
                    user.groups.add(Add_user)
                    if user.groups.filter(name='Viewers').exists():
                        remove_user = Group.objects.get(name='Viewers')
                        remove_user.user_set.remove(user)
                        messages.success(request, 'User successfully Added')
                    return redirect('Profile:permission')
            elif grp =='Viewers':
                if user.groups.filter(name='Viewers').exists():
                    messages.warning(request, 'User already exist')
                    return redirect('Profile:permission')
                else:
                    Add_user = Group.objects.get(name='Viewers')
                    user.groups.add(Add_user)
                    if user.groups.filter(name='Viewers').exists():
                        remove_user = Group.objects.get(name='Special_Users')
                        remove_user.user_set.remove(user)
                        messages.success(request, 'User successfully Added')
                    return redirect('Profile:permission')




def delete_user(request):
    if request.method =='POST':
        user_id = request.POST['deleteuser']
        grp = request.POST['Special_Users']

        user = User.objects.get(pk=user_id)
        if grp == 'Special_Users':
            if user.groups.filter(name='Special_Users').exists():
                deleteuser = Group.objects.get(name=grp)
                deleteuser.user_set.remove(user)
                messages.success(request, 'User successfully Removed')
                return redirect('Profile:permission')
            else:
                messages.warning(request, 'No such user in group')
                return redirect('Profile:permission')
        elif grp == 'Viewers':
            if user.groups.filter(name='Viewers').exists():
                deleteuser = Group.objects.get(name=grp)
                deleteuser.user_set.remove(user)
                messages.success(request, 'User successfully Removed')
                return redirect('Profile:permission')
            else:
                messages.warning(request, 'No such user in group')
                return redirect('Profile:permission')
