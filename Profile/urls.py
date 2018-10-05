from django.urls import path, include
from . import views
from social_django.urls import app_name as name
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib import admin
from social_core.utils import setting_name
app_name = 'Profile'
NAMESPACE = getattr(settings, setting_name('URL_NAMESPACE'), None) or 'social'

urlpatterns = [
    #path('login', auth_views.login, name='login'),
    path('oauth', include('social_django.urls', namespace='social')),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('sign_up_with_confirmation_mail', views.sign_up_with_confirmation_mail, name='sign_up_with_confirmation_mail'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    path('account_activation_invalid', views.account_activation_invalid, name='account_activation_invalid'),
    path('account_activation_sent', views.account_activation_sent, name='account_activation_sent'),
    path('login', views.login, name='login'),
    path('loginn', views.loginn, name='signin'),
    path('logout', views.logout_view, name='logout'),
    path('test', views.text, name='test'),
    path('user-dashboard', views.user_dashboard, name='user-dashboard'),
    path('permission', views.permission, name='permission'),
    path('add_user', views.add_user, name='add_user'),
    path('delete_user', views.delete_user, name='delete_user'),
    path('password_reset_form',views.password_forgot, name='password_reset_form'),
    path('password_reset', views.password_reset, name='reset_password'),
    path('password_reset_email', views.password_reset_email, name='password_reset_email'),
    path('change_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.change_password, name='change_password')
    ]
