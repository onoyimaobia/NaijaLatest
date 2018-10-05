from django.urls import path
from . import views

app_name = 'Music'

urlpatterns = [
    path('base', views.base, name='base'),
    path('newsticker', views.newsticker, name='newsticker'),
    path('home', views.home, name='home'),
    path('', views.home1, name='home1'),
    path('testing', views.testing, name='testing'),
    path('songs', views.songs, name='songs'),
    path('gospel', views.gospel, name='gospel'),
    path('hip_hop_rap', views.hip_hop_rap, name='hip_hop_rap'),
    path('hiphop_pop', views.hiphop_pop, name='hiphop_pop'),
    path('others', views.others, name='others'),
    path('video', views.video, name='video'),
    path('video_gospel', views.video_gospel, name='video_gospel'),
    path('video_hiphop_rap', views.video_hiphop_rap, name='video_hiphop_rap'),
    path('video_hiphop_pop', views.video_hiphop_pop, name='video_hiphop_pop'),
    path('video_others', views.video_others, name='video_others'),
    path('song_download/<int:audio_id>/', views.song_download, name='song_download'),
    path('video_download/<int:video_id>/', views.video_download, name='video_download'),
    path('video_download/<int:video_id>/', views.video_download, name='video_download'),
    path('add_music', views.add_music, name='add-music'),
    path('add_audio/<music_id>', views.add_audio, name='add-audio'),
    path('Add Video/<music_id>', views.add_video, name='add-video'),
    path('add_mixtape', views.add_mixtape, name='add_mixtape'),
    path('mixtape', views.mixtape, name='mixtape'),
    path('music_mixtape/<slug>/', views.play_mixtape, name='music_mixtape'),
    path('save_commment', views.save_comment, name='save_comment'),
    path('commment', views.display_comment, name='display_comment')


]

