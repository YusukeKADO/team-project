from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import Http404

from .forms import ArticleCreateForm

from sampleapp.models import Article

# Create your views here.


def article_create(request):
    if request.method == "POST":
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('sampleapp:index')
        else:
            form = ArticleCreateForm()

            return render(request, 'sampleapp/_create.html', {'form:form'})

def index(request):
    context = {
        "articles": Article.objects.all()
    }
    return render(request, 'sampleapp/index.html', context)

def redirect_test(request):
    return redirect(index)

def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist.")
    context = {
        "article": article
    }
    return render(request, 'sampleapp/tbd.html', context)

def update(request, article_id):
    context = {
        "article_id": article_id
    }
    return render(request, 'sampleapp/tbd.html', context)

def delete(request, article_id):
    return redirect(index)