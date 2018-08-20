from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings

CATEGORY_CHOICES = (
    ('politics', 'POLITICS'),
    ('entertainment', 'ENTERTAINMENT'),
    ('sports', 'SPORT'),
)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.username, filename)


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='politics')
    slug = models.SlugField(max_length=200, unique=True)
    cover_image = models.ImageField(upload_to=user_directory_path)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    poster = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='post', on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class NewsPosts(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='politics')
    slug = models.SlugField(max_length=200, unique=True)
    cover_picture = models.ImageField(upload_to=user_directory_path)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    speaker = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='newsposts', on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NewsPosts, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
