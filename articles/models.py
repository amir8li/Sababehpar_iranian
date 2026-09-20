from django.db import models
from news.models import TechnicalArticle

class Article(TechnicalArticle):
    class Meta:
        proxy = True
        app_label = 'articles'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
