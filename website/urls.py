from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/management-team/', views.management_team, name='management_team'),
    path('about/sustainability/', views.sustainability, name='sustainability'),
    path('industries/', views.industries, name='industries'),
    path('knowledge-center/', views.knowledge_center, name='knowledge_center'),
    path('knowledge-center/quality-control/', views.quality_control, name='quality_control'),
    path('knowledge-center/labs/', views.labs, name='labs'),
    path('knowledge-center/certifications/', views.certifications, name='certifications'),
]
