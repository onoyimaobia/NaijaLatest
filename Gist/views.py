from django.shortcuts import render
from django.http import Http404
# Create your views here.
from datetime import datetime
# Create your views here.
from Music.models import Music,Video,Audio,Lyrics
from django.http import JsonResponse
from .models import GistPost
from News.models import NewsPosts
from django.db.models import Q
from django.conf import settings


def gossip(request):
    first_twelve_gossip = GistPost.objects.all().filter(category='gossip').order_by('-id')[:12]
    last_gossip = GistPost.objects.all().filter(category='gossip').order_by('-id')[12:]
    template = 'Gist/gossip.html'
    context = {'first_twelve_gossip': first_twelve_gossip, 'last_gossip': last_gossip}
    return render(request, template, context)


def relationship(request):
    first_twelve_relationship = GistPost.objects.all().filter(category='relationship').order_by('-id')[:12]
    last_relationship = GistPost.objects.all().filter(category='relationship').order_by('-id')[:12]
    template = 'Gist/relationship.html'
    context = {'first_twelve_relationship': first_twelve_relationship, 'last_relationship':  last_relationship}
    return render(request, template, context)

def celeb(request):
    first_twelve_celeb = GistPost.objects.all().filter(category='celeb').order_by('-id')[:12]
    last_relationship = GistPost.objects.all().filter(category='celeb').order_by('-id')[12:]
    template = 'Gist/celeb.html'
    context = {'first_twelve_celeb': first_twelve_celeb, 'last_relationship': last_relationship}
    return render(request, template, context)


def wedding(request):
    first_twelve_wedding = GistPost.objects.all().filter(category='wedding').order_by('-id')[:12]
    last_wedding = GistPost.objects.all().filter(category='wedding').order_by('-id')[12:]
    template = 'Gist/wedding.html'
    context = {'first_twelve_wedding': first_twelve_wedding, 'last_wedding': last_wedding}
    return render(request, template, context)


def all_gist(request):
    first_fifteen_gist = GistPost.objects.all().order_by('-id')[:15]
    rest_gist = GistPost.objects.all().order_by('-id')[15:]
    template = 'Gist/all_gist.html'
    context = {'first_fifteen_gist': first_fifteen_gist, 'rest_gist': rest_gist}
    return render(request, template, context)


def display_gist(request, gist_id):
    try:
        gist = GistPost.objects.filter(pk=gist_id)
        select_related_date = GistPost.objects.get(pk=int(gist_id))
        related_date = select_related_date.created_on.date()
        title = select_related_date.title
        print(related_date)
        more_gist_three = NewsPosts.objects.filter(~Q(pk=int(gist_id)), created_on__date=related_date).order_by('-id')[
                          :3]
        more_gist = NewsPosts.objects.filter(~Q(pk=int(gist_id)), created_on__date=related_date).order_by('-id')[3:8]
        template = 'Gist/display_gist.html'
        ref_url = settings.SHARE_URL + str(gist)
        context = {'gist': gist, 'select_related_date': select_related_date, 'more_gist': more_gist,
                   'more_gist_three': more_gist_three, 'title': title, 'ref_url': ref_url}
    except NewsPosts.DoesNotExist:
        raise Http404("No such Post")
    return render(request, template, context)


def share_gist(request, gist_id):
    share = GistPost.objects.get(pk=int(gist_id))
    gist = share.title
    ref_url = settings.SHARE_URL + str(gist)
    template = 'Gist/share_gist.html'
    context = {'share': share, 'ref_url': ref_url}
    return render(request, template, context)
