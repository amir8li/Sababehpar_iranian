from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

from news import views as news_views

from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
from website import views as website_views

from django.contrib.auth.models import Group

# Custom Admin Branding
admin.site.site_header = "Sababehpar Iranian Administration"
admin.site.site_title = "Sababehpar Admin Portal"
admin.site.index_title = "Website Content Management"

try:
    admin.site.unregister(Group)
except Exception:
    pass

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

    path('درباره-ما-2/', RedirectView.as_view(url='/fa/about/', permanent=True)),
    path('درباره-ما-2', RedirectView.as_view(url='/fa/about/', permanent=True)),
    path('%d8%af%d8%b1%d8%a8%d8%a7%d8%b1%d9%87-%d9%85%d8%a7-2/', RedirectView.as_view(url='/fa/about/', permanent=True)),
    path('%d8%af%d8%b1%d8%a8%d8%a7%d8%b1%d9%87-%d9%85%d8%a7-2', RedirectView.as_view(url='/fa/about/', permanent=True)),
    path('پودر-میکرونیزه/', RedirectView.as_view(url='/fa/products/', permanent=True)),
    path('پودر-میکرونیزه', RedirectView.as_view(url='/fa/products/', permanent=True)),
    path('%d9%be%d9%88%d8%af%d8%b1-%d9%85%db%8c%da%a9%d8%b1%d9%88%d9%86%db%8c%d8%b2%d9%87/', RedirectView.as_view(url='/fa/products/', permanent=True)),
    path('%d9%be%d9%88%d8%af%d8%b1-%d9%85%db%8c%da%a9%d8%b1%d9%88%d9%86%db%8c%d8%b2%d9%87', RedirectView.as_view(url='/fa/products/', permanent=True)),



]

urlpatterns += i18n_patterns(
    path('', include('website.urls')),
    path('products/', include('products.urls')),
    path('news/', include('news.urls')),
    path('articles/', news_views.articles_list, name='articles_list'),
    path('articles/index.html', news_views.articles_list),
    path('articles/article-1/', news_views.article_1, name='article_1'),
    path('articles/article-1.html', news_views.article_1),
    path('articles/<slug:slug>/', news_views.article_detail, name='article_detail'),
    path('articles/<slug:slug>.html', news_views.article_detail),
    path('contact/', include('contact.urls')),
    prefix_default_language=False,
)


from django.urls import re_path
from django.views.static import serve

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATICFILES_DIRS[0] if settings.STATICFILES_DIRS else settings.STATIC_ROOT}),
]

