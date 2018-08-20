from django.urls import path
from . import views

app_name = 'Gist'

urlpatterns = [
    path('gossip', views.gossip, name='gossip'),
    path('relationship', views.relationship, name='relationship'),
    path('celeb', views.celeb, name='celeb'),
    path('wedding', views.wedding, name='wedding'),
    path('all_gist', views.all_gist, name='all_gist'),
    path('display_gist/<int:gist_id>/', views.display_gist, name='display_gist')
    ]