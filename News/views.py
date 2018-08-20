from django.shortcuts import render
from .models import NewsPosts
from django.db.models import Q
from django.http import Http404
# Create your views here.


def politics(request):
    first_twelve_politics = NewsPosts.objects.all().filter(category='politics').order_by('-id')[:12]
    last_politics = NewsPosts.objects.all().filter(category='politics').order_by('-id')[12:]
    template = 'News/politics.html'
    context = {'first_twelve_politics': first_twelve_politics, 'last_politics': last_politics}
    return render(request,template, context)


def sport(request):
    first_tweleve_sports = NewsPosts.objects.all().filter(category='sports').order_by('-id')[:12]
    rest_sports = NewsPosts.objects.all().filter(category='sports').order_by('-id')[12:]
    template = 'News/sports.html'
    context = {'first_tweleve_sports': first_tweleve_sports, 'rest_sports': rest_sports}
    return render(request, template, context)


def entertainment(request):
    first_tweleve_entertainment = NewsPosts.objects.all().filter(category='entertainment').order_by('-id')[:12]
    rest_entertainment = NewsPosts.objects.all().filter(category='entertainment').order_by('-id')[12:]
    template = 'News/entertainment.html'
    context = {'first_tweleve_entertainment': first_tweleve_entertainment, 'rest_entertainment': rest_entertainment}
    return render(request, template, context)


def all_news(request):
    first_fifteen_news = NewsPosts.objects.all().order_by('-id')[:15]
    rest_news = NewsPosts.objects.all().order_by('-id')[15:]
    template = 'News/all_news.html'
    context = {'first_fifteen_news': first_fifteen_news, 'rest_news': rest_news}
    return render(request, template, context)


def display_news(request, news_id):
    try:
        news = NewsPosts.objects.filter(pk=news_id)
        select_related_date = NewsPosts.objects.get(pk=int(news_id))
        related_date = select_related_date.created_on.date()
        print(related_date)
        more_news_three = NewsPosts.objects.filter(~Q(pk=int(news_id)), created_on__date=related_date).order_by('-id')[:3]
        more_news = NewsPosts.objects.filter(~Q(pk=int(news_id)), created_on__date=related_date).order_by('-id')[3:8]
        template = 'News/display_news.html'
        context = {'news': news, 'select_related_date': select_related_date, 'more_news': more_news,
                   'more_news_three': more_news_three}
    except NewsPosts.DoesNotExist:
        raise Http404("No such Post")
    return render(request, template, context)

