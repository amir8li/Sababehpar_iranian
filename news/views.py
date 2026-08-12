from django.shortcuts import render, get_object_or_404
from .models import NewsArticle, TechnicalArticle

def news_list(request):
    articles = NewsArticle.objects.filter(is_published=True)
    return render(request, 'news/index.html', {'articles': articles})

def news_1(request):
    article = NewsArticle.objects.filter(slug='news-1').first()
    return render(request, 'news/news_1.html', {'article': article})

def news_2(request):
    article = NewsArticle.objects.filter(slug='news-2').first()
    return render(request, 'news/news_2.html', {'article': article})

def news_3(request):
    article = NewsArticle.objects.filter(slug='news-3').first()
    return render(request, 'news/news_3.html', {'article': article})

def news_detail(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug, is_published=True)
    return render(request, 'news/detail.html', {'article': article})

def articles_list(request):
    technical_articles = TechnicalArticle.objects.filter(is_published=True)
    return render(request, 'articles/index.html', {'technical_articles': technical_articles})

def article_1(request):
    article = TechnicalArticle.objects.filter(slug='article-1').first()
    return render(request, 'articles/article_1.html', {'article': article})

def article_detail(request, slug):
    article = get_object_or_404(TechnicalArticle, slug=slug, is_published=True)
    return render(request, 'articles/detail.html', {'article': article})
