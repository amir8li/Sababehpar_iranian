from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from news import views as news_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('products/', include('products.urls')),
    path('news/', include('news.urls')),
    path('articles/', news_views.articles_list, name='articles_list'),
    path('articles/article-1/', news_views.article_1, name='article_1'),
    path('articles/<slug:slug>/', news_views.article_detail, name='article_detail'),
    path('contact/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
