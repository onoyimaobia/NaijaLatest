from django.urls import path
from . import views

app_name = 'Mysteries'

urlpatterns = [
    path('love quotes', views.love_quotes, name='love quotes'),
    ]
