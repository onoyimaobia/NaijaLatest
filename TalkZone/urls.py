from django.urls import path
from . import views

app_name = 'TalkZone'

urlpatterns = [
    path('talkzone', views.talk_zone, name='talkzone'),
    path('talk_zone_view/<int:talk_id>/', views.talk_zone_view, name='talk_zone_view'),
    path('Comment', views.save_comment, name='save_comment'),
    path('commment', views.display_comment, name='display_comment'),
    path('index', views.index, name='index'),
    path('lazy_load_posts', views.lazy_load_posts, name='lazy_load_posts'),
     ]
