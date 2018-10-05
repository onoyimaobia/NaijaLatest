from django.shortcuts import render
from .models import Quote
# Create your views here.


def love_quotes(request):
    one = Quote.objects.all().filter(category='love').order_by('-id')[:1]
    two = Quote.objects.all().order_by('-id')[1:3]
    first_ten_lovequotes = Quote.objects.all().filter(category='love').order_by('-id')[:10]
    more_love_quotes = Quote.objects.all().order_by('-id')[5:]
    template = 'Mysteries/love_quotes.html'
    context = {'first_ten_lovequotes': first_ten_lovequotes, 'more_love_quotes': more_love_quotes}
    return render(request, template, context)
