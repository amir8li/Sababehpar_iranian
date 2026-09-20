from django.shortcuts import render
from django.template.loader import select_template
from .models import NewsArticle, TechnicalArticle

def news_list(request):
    articles = NewsArticle.objects.filter(is_published=True)
    return render(request, 'news/index.html', {'articles': articles})

def news_1(request):
    return news_detail(request, 'news-1')

def news_2(request):
    return news_detail(request, 'news-2')

def news_3(request):
    return news_detail(request, 'news-3')

def news_detail(request, slug):
    clean_slug = slug.replace('.html', '')
    article = NewsArticle.objects.filter(slug=clean_slug, is_published=True).first()
    if not article:
        article = NewsArticle.objects.filter(slug=clean_slug).first()
    return render(request, 'news/detail.html', {'article': article})

def articles_list(request):
    technical_articles = TechnicalArticle.objects.filter(is_published=True)
    return render(request, 'articles/index.html', {'technical_articles': technical_articles})

def article_1(request):
    return article_detail(request, 'article-1')

def article_detail(request, slug):
    clean_slug = slug.replace('.html', '')
    article = TechnicalArticle.objects.filter(slug=clean_slug, is_published=True).first()
    if not article:
        article = TechnicalArticle.objects.filter(slug=clean_slug).first()
    return render(request, 'articles/detail.html', {'article': article})
