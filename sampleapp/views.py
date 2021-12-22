from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone
import random
from blog.models import Article

# Create your views here.
def index(request):
    if request.method=='POST':
        article=Article(title=request.POST['title'],body=request.POST['text'])
        article.save()
        return redirect(detail, article.id)
    context = {
        "articles": Article.objects.all()
    }
    return render(request, 'blog/index.html', context)

def detail(request, article_id):
    try:
        article=Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    context={
        'article':article,
    }
    return render(request, "blog/detail.html", context)