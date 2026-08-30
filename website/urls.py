from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home),
    path('about/', views.about, name='about'),
    path('about.html', views.about),
    path('about/index.html', views.about),
    path('about/management-team/', views.management_team, name='management_team'),
    path('about/management-team.html', views.management_team),
    path('management-team/', views.management_team),
    path('management-team.html', views.management_team),
    path('about/sustainability/', views.sustainability, name='sustainability'),
    path('about/sustainability.html', views.sustainability),
    path('sustainability/', views.sustainability),
    path('sustainability.html', views.sustainability),
    path('industries/', views.industries, name='industries'),
    path('industries.html', views.industries),
    path('industries/index.html', views.industries),
    path('knowledge-center/', views.knowledge_center, name='knowledge_center'),
    path('knowledge-center.html', views.knowledge_center),
    path('knowledge-center/index.html', views.knowledge_center),
    path('knowledge-center/quality-control/', views.quality_control, name='quality_control'),
    path('knowledge-center/quality-control.html', views.quality_control),
    path('knowledge-center/labs/', views.labs, name='labs'),
    path('knowledge-center/labs.html', views.labs),
    path('knowledge-center/certifications/', views.certifications, name='certifications'),
    path('knowledge-center/certifications.html', views.certifications),
]
