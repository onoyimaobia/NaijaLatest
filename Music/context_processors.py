


def song(request):
    from Music.models import Audio,Video
    latest_song = Audio.objects.all().order_by('-id')[:1]
    latest_video = Video.objects.all().order_by('-id')[:1]
    return {
        'song': latest_song, 'video': latest_video,  # Add 'latest_song' to the context
    }