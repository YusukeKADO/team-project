from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
<<<<<<< HEAD

from .forms import ArticleCreateForm

from sampleapp.models import Article, Media

# Create your views here.


def home(request):
    return render(request, 'sampleapp/home.html', {})

def article_create(request):
    if request.method == "POST":
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sampleapp:index')
    else:
        form = ArticleCreateForm()
    return render(request, 'sampleapp/article_create.html', {'form':form})

def index(request):
    if request.method == "POST":
        article = Article(title=request.POST['title'], body=request.POST['text'])
        article.save()
        media = Media(title=request.POST['title'], image=request.POST['image'])
        media.save()
        return redirect(detail, article.id, media.id)
=======
from django.utils import timezone
import random
from sampleapp.models import Article

# Create your views here.
def index(request):
    if request.method=='POST':
        article=Article(title=request.POST['title'],body=request.POST['text'])
        article.save()
        return redirect(detail, article.id)
>>>>>>> 6d9121448ef78e7a760c324615df55681f96e8c3
    context = {
        "articles": Article.objects.all(),
        "media": Media.objects.all(),
    }
    return render(request, 'sampleapp/index.html', context)
<<<<<<< HEAD

def redirect_test(request):
    return redirect(index)
=======
>>>>>>> 6d9121448ef78e7a760c324615df55681f96e8c3

def detail(request, article_id):
    try:
        article=Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    context={
        'article':article,
    }
<<<<<<< HEAD
    return render(request, 'sampleapp/detail.html', context)

def update(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist.")
    if request.method == "POST":
        article.title = request.POST['title']
        article.body = request.POST['text']
        article.save()
        return redirect(detail, article_id)
    context = {
        "article_id": article_id
    }
    return render(request, 'sampleapp/edit.html', context)

def delete(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article>DoesNotExist:
        raise Http404("Article does not exist.")
    article.delete()
    return redirect(index)


def media_create(request):
    if request.method == "POST":
        form = MediaCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sampleapp:index')
    else:
        form = MediaCreateForm()
    return render(request, 'sampleapp/media_create.html', {'form':form})
=======
    return render(request, "blog/detail.html", context)
>>>>>>> 6d9121448ef78e7a760c324615df55681f96e8c3
