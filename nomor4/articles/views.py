from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'post_list.html',{'articles': articles})

def detail(request, art_id):    
    try:
        article = Article.objects.get(pk=art_id)
        article.views = article.views + 1
        article.save()
    except Article.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'post_detail.html', {'article': article})