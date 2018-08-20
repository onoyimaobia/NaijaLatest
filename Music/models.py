from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Music(models.Model):
    song_title = models.CharField(max_length=50)
    album = models.CharField(default='No Album', max_length=50)
    genre = models.CharField(max_length=50)
    released_Year = models.CharField(max_length=20, blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to='cover_image/')
    uploader = models.CharField(max_length=20)
    artist = models.CharField(default='None', max_length=20)
    featured_artist = models.CharField(default='None', max_length=20)

    # create a string representation of song
    def __str__(self):
        return self.song_title


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.username, filename)


class Video(models.Model):
    video = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='videos', on_delete=models.DO_NOTHING)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.video)


class Audio(models.Model):
    audio = models.FileField(upload_to= user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='audios', on_delete=models.DO_NOTHING)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return str(self.audio)


class UserPlayVideo(models.Model):
    user = models.ForeignKey(User,related_name='playvideo', on_delete=models.DO_NOTHING)
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING)


class UserDownloadVideo(models.Model):
    user = models.ForeignKey(User,related_name='downloadvideo', on_delete=models.DO_NOTHING)
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING)


class UserPlayAudio(models.Model):
    user = models.ForeignKey(User, related_name='playaudio', on_delete=models.DO_NOTHING)
    audio = models.ForeignKey(Audio, on_delete=models.DO_NOTHING)


class UserDownloadAudio(models.Model):
    user = models.ForeignKey(User, related_name='downloadaudio', on_delete=models.DO_NOTHING)
    audio = models.ForeignKey(Audio, on_delete=models.DO_NOTHING)


class Lyrics(models.Model):
    lyric = models.TextField()
    music = models.ForeignKey(Music, on_delete=models.DO_NOTHING)




#class Videos(models.Model):
    #music = models.ForeignKey(Music,on_delete=models.CASCADE)
    #video = models.FileField(upload_to='videos/', null=True, verbose_name="")
    #cover_image = models.ImageField(upload_to= 'video_image')

    #def __str__(self):
        #return str(self.video)

#class Audios(models.Model):
    #music = models.ForeignKey(Music,on_delete=models.CASCADE)
    #audio = models.FileField(upload_to='audio', blank=True, verbose_name="")
    #cover_image = models.ImageField(upload_to='audio_image')

    #def __str__(self):
        #return str(self.audio)
