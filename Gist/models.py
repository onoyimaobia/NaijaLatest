from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings
from  ckeditor.fields import RichTextField, CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField

CATEGORY_CHOICES = (
    ('gossip', 'GOSSIP'),
    ('relationship', 'RELATIONSHIP'),
    ('wedding', 'WEDDING'),
    ('celeb', 'CELEB'),
)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.username, filename)


class GistPost(models.Model):
    title = RichTextField(max_length=250, config_name='special')
    body = RichTextUploadingField(config_name='default',
                                  external_plugin_resources=[('youtube',
                                                              '/static/ckeditor/youtube/',
                                                              'plugin.js',)],
                                  )
    category = models.CharField(max_length=250, choices=CATEGORY_CHOICES, default='gossip')
    seo_title = models.CharField(max_length=300, blank=True)
    description = RichTextField(max_length=200, blank=True, config_name='special')
    slug = models.SlugField(max_length=300, unique=True)
    cover_image = models.ImageField(upload_to=user_directory_path)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    poster = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='gistpost', on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(GistPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comedy(models.Model):
    comedy = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comedy', on_delete=models.DO_NOTHING)
    music = models.ForeignKey(GistPost, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.comedy)


class MostView(models.Model):
    what_viewd = models.ForeignKey(GistPost, on_delete=models.DO_NOTHING)
