from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from news import views as news_views

from django.views.generic.base import RedirectView
from website import views as website_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', website_views.robots_txt, name='robots_txt'),
    path('sitemap.xml', website_views.sitemap_xml, name='sitemap_xml'),
    
    # Legacy WordPress 301 Redirects (Preserves old SEO rank & prevents 404s)
    path('shop/', RedirectView.as_view(url='/products/', permanent=True)),
    path('shop', RedirectView.as_view(url='/products/', permanent=True)),
    path('gallery/', RedirectView.as_view(url='/', permanent=True)),
    path('gallery', RedirectView.as_view(url='/', permanent=True)),
    path('packing/', RedirectView.as_view(url='/products/', permanent=True)),
    path('packing', RedirectView.as_view(url='/products/', permanent=True)),
    path('pages/', RedirectView.as_view(url='/', permanent=True)),
    path('pages', RedirectView.as_view(url='/', permanent=True)),
    path('contact-us/', RedirectView.as_view(url='/contact/', permanent=True)),
    path('contact-us', RedirectView.as_view(url='/contact/', permanent=True)),

    path('', include('website.urls')),
    path('products/', include('products.urls')),
    path('news/', include('news.urls')),
    path('articles/', news_views.articles_list, name='articles_list'),
    path('articles/article-1/', news_views.article_1, name='article_1'),
    path('articles/article-1.html', news_views.article_1),
    path('articles/<slug:slug>/', news_views.article_detail, name='article_detail'),
    path('articles/<slug:slug>.html', news_views.article_detail),
    path('contact/', include('contact.urls')),
]


from django.urls import re_path
from django.views.static import serve

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

