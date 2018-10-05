from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings
# Create your models here.


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.username, filename)


class TalkZone(models.Model):
    subtitle = models.CharField(max_length=96)
    title = models.TextField()
    slug = models.TextField()
    subbody = models.CharField(max_length=200, default='clean me and type')
    description = models.TextField(default='clean me and type')
    body1 = models.TextField()
    middle_image = models.ImageField(upload_to=user_directory_path)
    body2 = models.TextField(default='clean me and type')
    cover_image = models.ImageField(upload_to=user_directory_path)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    poster = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='talkzone', on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TalkZone, self).save(*args, **kwargs)

    def __str__(self):
        return self.subtitle


class Comments(models.Model):
    talk_zone = models.ForeignKey(TalkZone, on_delete=models.DO_NOTHING)
    comment = models.TextField()
    name = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name