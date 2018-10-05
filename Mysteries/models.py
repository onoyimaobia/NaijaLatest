from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.username, filename)
# Create your models here.


CATEGORY_CHOICES = (
    ('love', 'LOVE'),
    ('inspirational', 'INSPIRATIONAL'),
    ('motivational', 'MOTIVATIONAL'),
    ('insight', 'INSIGHT')
)


class Quote(models.Model):
    message = models.TextField()
    quote_picture = models.ImageField(upload_to=user_directory_path)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='love')
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mysteries', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.category