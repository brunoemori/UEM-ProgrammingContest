from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from wiki.models import Article

def problems(request):
    articleList = Article.objects.all()
    try:
        ownArticles = articleList.filter(authorID=request.user.id).order_by('date')[:5]
    except ObjectDoesNotExist:
        ownArticles = None
    
    try:
        otherArticles = articleList.exclude(authorID=request.user.id).order_by('date')[:5]
    except ObjectDoesNotExist:
        otherArticles = None

    return render(request, 'problems/problems.html',
        {"ownArticles": ownArticles, "otherArticles": otherArticles})

def ownProblems(request):
    try:
        ownArticlesList = Article.objects.all().filter(authorID=request.user.id).order_by('date')
        paginator = Paginator(ownArticlesList, 10)

        page = request.GET.get('page')
        ownArticles = paginator.get_page(page)

    except ObjectDoesNotExist:
        ownArticles = None

    return render(request, 'problems/yourarticles.html', {"ownArticles": ownArticles})

def otherProblems(request):
    try:
        otherArticlesList = Article.objects.all().exclude(authorID=request.user.id).order_by('date')
        paginator = Paginator(otherArticlesList, 10)

        page = request.GET.get('page')
        otherArticles = paginator.get_page(page)

    except ObjectDoesNotExist:
        otherArticles = None

    return render(request, 'problems/otherarticles.html', {"otherArticles": otherArticles})
