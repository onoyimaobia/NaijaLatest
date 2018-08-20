from django.contrib import admin
from .models import Music,Video,Audio,Lyrics
# Register your models here.


admin.site.register(Music)
admin.site.register(Video)
admin.site.register(Audio)
admin.site.register(Lyrics)