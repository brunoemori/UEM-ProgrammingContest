from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def wikiHome(request):
    pass

def getPage(request, articleUrl):
    try:
        article = Article.objects.get(problemNumber=articleUrl)
    
    except Article.DoesNotExist:
        #TO_DO: If page doesn't exist, implement an option to create it.
        return HttpResponse('<h5> This page does not exist. </h5>')

    return render(request, 'wiki/wiki.html', {'article': article})
