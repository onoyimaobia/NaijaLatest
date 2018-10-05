from django.shortcuts import render, redirect
from .models import NewsPosts
from django.db.models import Q
from django.http import Http404
from .forms import AddNews
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


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
    news = NewsPosts.objects.all().order_by('-id')
    paginator = Paginator(news, 36)
    page = request.GET.get('page', 1)
    try:
        newss = paginator.page(page)
    except PageNotAnInteger:
        newss = paginator.page(1)
    except EmptyPage:
        newss = paginator.page(paginator.num_pages)
    template = 'News/all_news.html'
    context = {'newss': newss}
    return render(request, template, context)


def display_news(request, slug):
    try:
        print(slug)
        news = NewsPosts.objects.filter(slug=slug)
        select_related_date = NewsPosts.objects.get(slug=slug)
        related_date = select_related_date.category
        print(related_date)
        #more_news_three = NewsPosts.objects.filter(~Q(slug=slug), created_on__date=related_date).order_by('-id')[:3]
        more_news = NewsPosts.objects.filter(~Q(slug=slug), category=related_date).order_by('-id')[:6]
        template = 'News/display_news.html'
        context = {'news': news, 'select_related_date': select_related_date, 'more_news': more_news}
    except NewsPosts.DoesNotExist:
        raise Http404("No such Post")
    return render(request, template, context)


def add_news(request):
    current_user = request.user
    user_id = current_user.id
    if request.method == 'POST':
        form = AddNews(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            title = request.POST.get('title')
            qs = NewsPosts.objects.filter(title=title)
            if qs.exists():
                messages.error(request, 'Song Title already Exist')
                form = AddNews()
                return redirect('Music:add-music', {'form': form})
            else:
                news.user_id = user_id
                element_to_replace = ['', '@', '&', '$', '#', "'", '"', '--', ]
                for element in element_to_replace:
                    if element in title:

                        news.slug = title.replace(element, '-')
                form.save()
                messages.success(request, ' Music added successfully')
            return redirect('Profile:user-dashboard')
    else:
        form = AddNews()
        template = 'News/addnews.html'
        return render(request, template, {
            'form': form
        })


