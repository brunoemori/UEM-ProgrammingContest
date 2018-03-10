from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Article
from .forms import ArticleForm
import datetime

def wikiHome(request):
    pass

def getPage(request, articleUrl):
    try:
        article = Article.objects.get(problemNumber=articleUrl)
    
    except Article.DoesNotExist:
        #TO_DO: If page doesn't exist, implement an option to create it.
        return HttpResponse('<h5> This page does not exist. </h5>')

    return render(request, 'wiki/wiki.html', {'article': article})

def newPage(request):
    if (request.method == 'POST'):
        form = ArticleForm(request.POST)
        if (form.is_valid()):
            article = form.save(commit=False)
            article.date = datetime.datetime.now()
            article.authorID = request.user

            article.save()
            messages.success(request, 'Article ' + str(article.problemNumber) + ' created successfully!')
                
    else:
        form = ArticleForm()
    
    print(form.errors)
    return render(request, 'wiki/newpage.html', {"form": form})
