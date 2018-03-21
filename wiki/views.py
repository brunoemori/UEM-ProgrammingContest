from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

    return render(request, 'wiki/wiki.html', {'article': article, 'user': request.user})

@login_required()
def newPage(request):
    if (request.method == 'POST'):
        form = ArticleForm(request.POST)
        if (form.is_valid()):
            article = form.save(commit=False)
            article.date = datetime.datetime.now()
            article.authorID = request.user

            article.save()
            messages.success(request, 'Article ' + str(article.problemNumber) + ' created successfully!')
            return redirect('/wiki/' + str(article.problemNumber))
                
    else:
        form = ArticleForm()
    
    print(form.errors)
    return render(request, 'wiki/newpage.html', {"form": form})

@login_required
def editPage(request, articleUrl):
    article = Article.objects.get(problemNumber=articleUrl)

    if (article.authorID.id != request.user.id):
        return redirect('/home')

    form = ArticleForm(request.POST, instance=article)

    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()
            messages.success(request, 'Article ' + str(article.problemNumber) + ' updated!')
            return redirect('/wiki/' + str(article.problemNumber))
        
    else:
        form = ArticleForm(instance=article)

    return render(request, 'wiki/newpage.html', {'form': form, 'user': request.user, 'isEditing': True})

@login_required()
def deletePage(request, articleUrl):
    article = Article.objects.get(problemNumber=articleUrl)

    if (article.authorID.id != request.user.id):
        return redirect('/home')

    if (request.method == 'POST'):
        print("Here")
        form = ArticleForm(request.POST, instance=article)
        article.delete()
        messages.success(request, 'Article' + str(article.problemNumber) + ' successfully deleted!')
        return redirect('/problems')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'wiki/newpage.html', {'form': form, 'user': request.user, 'isDeleting': True})
