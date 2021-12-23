from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import Http404

from blog.models import Article

# Create your views here.

def apphome(request):
    return render(request, 'teamapp/apphome.html', {})

def index(request):
    context = {
        "articles": Article.objects.all()
    }
    return render(request, 'teamapp/index.html', context)
    
    """
    if request.method == 'GET':
        return render(request, 'teamapp/index.html', {})
    elif request.method == 'POST':
        title = request.POST['title']
        text = request.POST['task']
        return HttpResponse('Title: {}, Task: {}'.format(title, text))
    """

def redirect_test(request):
    return redirect(apphome)

def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist.")
    context = {
        "article": article
    }
    return render(request, 'teamapp/tbd.html', context)

def update(request, article_id):
    context = {
        "article_id": article_id
    }
    return render(request, 'teamapp/tbd.html', context)

def delete(request, article_id):
    return redirect(index)