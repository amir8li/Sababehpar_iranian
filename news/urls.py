from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='index'),
    path('index.html', views.news_list),
    path('news-1/', views.news_1, name='news_1'),
    path('news-1.html', views.news_1),
    path('news-2/', views.news_2, name='news_2'),
    path('news-2.html', views.news_2),
    path('news-3/', views.news_3, name='news_3'),
    path('news-3.html', views.news_3),
    path('<slug:slug>/', views.news_detail, name='detail'),
    path('<slug:slug>.html', views.news_detail),
]
