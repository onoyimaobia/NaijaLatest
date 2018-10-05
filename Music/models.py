from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from  ckeditor.fields import RichTextField, CKEditorWidget
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    about_song = models.CharField(max_length=300, blank=True)

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
    slug = models.SlugField(max_length=300, unique=True, null=True)
    slug_title = models.CharField(max_length=300, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug_title)
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.video)


class Audio(models.Model):
    audio = models.FileField(upload_to= user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='audios', on_delete=models.DO_NOTHING)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to=user_directory_path)
    slug = models.SlugField(max_length=300, unique=True, null=True)
    slug_title = models.CharField(max_length=300, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug_title)
        super(Audio, self).save(*args, **kwargs)

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


class Confirmemail(models.Model):
    confirm_email = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Mixtape(models.Model):
    tape_name = RichTextField(max_length=250, config_name='special')
    slug = models.SlugField(max_length=250)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mixtape', on_delete=models.DO_NOTHING)
    tape = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tracks = RichTextField(max_length=2500, config_name='special')
    dj_description = RichTextUploadingField(config_name='special')
    tape_image = models.FileField(upload_to=user_directory_path)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.tape_name)
        super(Mixtape, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.tape_name)


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

class Comments(models.Model):
    mixtape = models.ForeignKey(Mixtape, on_delete=models.DO_NOTHING)
    comment = models.TextField()
    name = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name