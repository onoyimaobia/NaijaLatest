from django.shortcuts import render
from datetime import datetime
# Create your views here.
from .models import Music,Video,Audio,Lyrics
from django.http import JsonResponse
from Gist.models import GistPost
from News.models import NewsPosts
from django.db.models import Q
from django.http import Http404


def home(request):

    time = datetime.now()
    day = time.strftime("%A")
    hour = time.hour
    if hour < 12:
        message = "Good Morning"
    elif 12 <= hour < 16:
        message = "Good afternoon"
    else:
        message = "Good Evening"

    first_six = Music.objects.all().order_by('-id')[:6]
    first_twelve = Music.objects.all().order_by('-id')[6:9]

    print(first_six)
    context = {'time': time, 'message': message, 'day': day, 'first_six': first_six, 'first_twelve':first_twelve }
    template = 'Music/home.html'
    return render(request, template, context)



def base(request):
    time = datetime.now()
    day = time.strftime("%A")



    hour = time.hour
    if hour < 12:
        message = "Good Morning"
    elif 12 <= hour < 16:
        message = "Good afternoon"
    else:
        message = "Good Evening"
    context = {'time': time, 'message': message,'day': day}
    template = 'Music/base.html'
    return render(request, template,context)


def newsticker(request):
    template = 'Music/newsticker.html'
    return render(request, template)


def home1(request):
    #video
    first = Music.objects.all().order_by('-id')[:1]
    second = Music.objects.all().order_by('-id')[1:2]
    third = Music.objects.all().order_by('-id')[2:3]
    forth = Music.objects.all().order_by('-id')[3:4]
    #first_twelve = Music.objects.all().order_by('-id')[6:9]
    first_ten_song = Audio.objects.all().order_by('-id')[3:11]
    videos = Video.objects.all().order_by('-id')[3:11]
    #from News
    first_slide = NewsPosts.objects.all().order_by('-id')[:1]
    second_slide = NewsPosts.objects.all().order_by('-id')[1:2]
    third_slide = NewsPosts.objects.all().order_by('-id')[2:3]
    forth_slide = NewsPosts.objects.all().order_by('-id')[3:4]
    fifth_slide = NewsPosts.objects.all().order_by('-id')[4:5]
    sixth_slide = NewsPosts.objects.all().order_by('-id')[5:6]
    news = NewsPosts.objects.all().order_by('-id')[6:9]

    #Gist
    slide0ne = GistPost.objects.all().order_by('-id')[:1]
    slidetwo = GistPost.objects.all().order_by('-id')[1:2]
    slidethree = GistPost.objects.all().order_by('-id')[2:3]
    slidefour = GistPost.objects.all().order_by('-id')[3:4]
    gist = GistPost.objects.all().order_by('-id')[4:7]
    #Songs
    one = Audio.objects.all().order_by('-id')[:1]
    two = Audio.objects.all().order_by('-id')[1:2]
    three = Audio.objects.all().order_by('-id')[2:3]

    #print(first_six)
    context = {'videos': videos, 'first': first, 'second': second, 'third': third, 'forth': forth, 'first_ten_song': first_ten_song,
               'first_slide': first_slide, 'second_slide': second_slide, 'third_slide': third_slide,
               'forth_slide': forth_slide, 'fifth': fifth_slide, 'sixth': sixth_slide, 'slideone': slide0ne,
               'slidetwo': slidetwo, 'slidethree': slidethree, 'slidefour': slidefour, 'one': one, 'two': two,
               'three': three, 'news': news, 'gist': gist}

    template = 'Music/home1.html'
    return render(request, template, context)


def testing(request):
    template = 'Music/testing.html'
    return render(request, template)


def songs(request):
    first_songs = Audio.objects.all().order_by('-id')[:12]
    second_songs = Audio.objects.all().order_by('-id')[12:]
    template = 'Music/songs.html'
    context = {'first_songs': first_songs, 'second_songs': second_songs}
    return render(request, template, context)


def gospel(request):
    first_fifteen_gospel = Audio.objects.all().filter(Q(music__genre='Christian/Gospel') | Q(music__genre='R&B/soul')
                                                      ).order_by('-id')[:15]
    template = 'Music/gospel.html'
    context = {'first_fifteen_gospel': first_fifteen_gospel}
    return render(request, template, context)


def hip_hop_rap(request):
    first_twelve_hip_hop_rap = Audio.objects.all().filter(music__genre='Hip-Hop/Rap').order_by('-id')[:12]
    second_hip_hop_rap = Audio.objects.all().filter(music__genre='Hip-Hop/Rap').order_by('-id')[12:]
    template = 'Music/hiphoprap.html'
    context = {'first_twelve_hip_hop_rap': first_twelve_hip_hop_rap, 'second_hip_hop_rap': second_hip_hop_rap}
    return render(request, template, context)

def hiphop_pop(request):
    hiphop_pop = Audio.objects.all().filter(Q(music__genre='Hip-Hop') | Q(music__genre='Pop')).order_by('-id')[:15]
    template = 'Music/hiphop-pop.html'
    context = {'hiphop_pop': hiphop_pop}
    return render(request, template, context)

def others(request):
    genres = ['Christian/Gospel', 'Hip-Hop/Rap', 'R&B/Soul', 'Hip-Hop', 'Pop']
    song_others = Audio.objects.all().filter(~Q(music__genre__in=genres)).order_by('-id')[:12]
    template = 'Music/song-others.html'
    context = {'song_others': song_others}
    return render(request, template, context)


def video(request):
    first_fifteen_video = Video.objects.all().order_by('-id')[:15]
    rest_video = Video.objects.all().order_by('-id')[15:]
    template = 'Music/video.html'
    context = {'first_fifteen_video': first_fifteen_video, 'rest_video': rest_video}
    return render(request, template, context)


def video_gospel(request):
    vedeo_gospel = Video.objects.all().filter(Q(music__genre='Christian/Gospel') | Q(music__genre='R&B/soul')
                                                      ).order_by('-id')[:15]
    vedeo_gospel2 = Video.objects.all().filter(Q(music__genre='Christian/Gospel') | Q(music__genre='R&B/soul')
                                              ).order_by('-id')[15:]
    template = 'Music/video_gospel.html'
    context = {'vedeo_gospel':  vedeo_gospel, 'vedeo_gospel2': vedeo_gospel2}
    return render(request, template, context)


def video_hiphop_rap(request):
    video_hiphop_rap = Video.objects.all().filter(music__genre='Hip-Hop/Rap').order_by('-id')[:12]
    template = 'Music/video_hiphop_rap.html'
    context = {'video_hiphop_rap': video_hiphop_rap}
    return render(request, template, context)


def video_hiphop_pop(request):
    video_hiphop_pop = Video.objects.all().filter(Q(music__genre='Hip-Hop') | Q(music__genre='Pop')).order_by('-id')[:15]

    template = 'Music/video_hiphop_pop.html'
    context = {'video_hiphop_pop': video_hiphop_pop}
    return render(request, template, context)


def video_others(request):
    genres = ['Christian/Gospel', 'Hip-Hop/Rap', 'R&B/Soul', 'Hip-Hop', 'Pop']
    video_others = Video.objects.all().filter(~Q(music__genre__in=genres)).order_by('-id')[:12]
    template = 'Music/video_others.html'
    context = {'video_others': video_others}
    return render(request, template, context)


def song_download(request, audio_id):
    try:
        featured_artist = Audio.objects.get(pk=int(audio_id))
        artist = featured_artist.music.artist
        first_six_artist_song = Audio.objects.filter(~Q(pk=int(audio_id)), music__artist=artist).order_by('-id')[:6]
        play_audio = Audio.objects.filter(pk=audio_id)
    except Music.DoesNotExist:
        raise Http404("can't play or download song")
    return render(request, 'Music/song_download.html', {'play_audio': play_audio,
                                                        'first_six_artist_song': first_six_artist_song,
                                                        'featured_artist': featured_artist})


def video_download(request, video_id):
    try:
        play_video = Video.objects.filter(pk=video_id)
        featured_artist = Video.objects.get(pk=int(video_id))
        artist = featured_artist.music.artist
        first_six_artist_video = Video.objects.filter(~Q(pk=int(video_id)), music__artist=artist).order_by('-id')[:6]
    except Video.DoesNotExist:
        raise Http404("Can't download Video")
    return render(request, 'Music/video_download.html', {'play_video': play_video,
                                                         'first_six_artist_video': first_six_artist_video,
                                                         'featured_artist': featured_artist})
