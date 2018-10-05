from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.username, filename)


class Profile(models.Model):
    address = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=12)
    profile_picture = models.FileField(upload_to='cover_image')


class ProfilePic(models.Model):
    picture = models.FileField(upload_to= user_directory_path)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='picture', on_delete=models.DO_NOTHING)
    upload_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



