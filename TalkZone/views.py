from django.shortcuts import render, redirect
from .models import TalkZone, Comments
from django.conf import settings
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse


# Create your views here.
def talk_zone(request):
    talk_zone = TalkZone.objects.all().order_by('-id')[1:]
    template = 'TalkZone/Talk_zone.html'
    context = {'talk_zone': talk_zone}
    return render(request, template, context)


def talk_zone_view(request, talk_id):
    try:
        talk_zone = TalkZone.objects.get(pk=int(talk_id))
        select_related_date = TalkZone.objects.get(pk=int(talk_id))
        related_date = select_related_date.created_on.date()
        title = select_related_date.subtitle
        print(related_date)
        one_talk_zone = TalkZone.objects.filter(~Q(pk=int(talk_id)), created_on__date=related_date).order_by('-id')[
                          :1]
        comments = Comments.objects.filter(talk_zone=talk_zone)
        total = comments.count()
        template = 'TalkZone/talk_zone_view.html'
        ref_url = settings.SHARE_TALKZONE_URL
        context = {'talk_zone': talk_zone, 'select_related_date': select_related_date,
                   'one_talk_zone': one_talk_zone, 'title': title, 'ref_url': ref_url,
                   'comments': comments, 'total': total}
    except TalkZone.DoesNotExist:
        raise Http404("No such Post")
    return render(request, template, context)


def save_comment(request):
    if request.method == 'POST':
        talk_zone_id = int(request.POST['talk_zone'])
        comment = request.POST['comment']
        name = request.POST['name']
        saved_comment = Comments.objects.create(talk_zone_id=talk_zone_id, comment=comment, name=name)
        saved_comment.save()
        # talkzone = TalkZone.objects.get(pk=talk_zone_id)
        return HttpResponseRedirect(reverse('TalkZone:talk_zone_view', kwargs={'talk_id': talk_zone_id}))
        # return redirect('TalkZone:talk_zone_view',)


def display_comment(request, talk_id):
    comment = Comments.objects.filter(talk_zone=talk_id)
    total = comment.count()
    template = 'TalkZone/talk_zone_view.html'
    context = {'comment': comment, 'total': total}
    return render(request, template, context)


def index(request):
    posts = TalkZone.objects.all()
    return render(request, 'TalkZone/index.html', {'posts': posts})


def lazy_load_posts(request):
    page = request.POST.get('page')
    posts = TalkZone.objects.all()[:5]  # get just 5 posts

    # use Django's pagination
    # https://docs.djangoproject.com/en/dev/topics/pagination/
    results_per_page = 5
    paginator = Paginator(posts, results_per_page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(2)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # build a html posts list with the paginated posts
    posts_html = loader.render_to_string('TalkZone/posts.html', {'posts': posts})

    # package output data and return it as a JSON object
    output_data = {'posts_html': posts_html, 'has_next': posts.has_next()}
    return JsonResponse(output_data)

