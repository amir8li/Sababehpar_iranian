from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='index'),
    path('calcium-carbonate/', views.calcium_carbonate, name='calcium_carbonate'),
    path('calcium-carbonate.html', views.calcium_carbonate),
    path('coated-calcium-carbonate/', views.coated_calcium_carbonate, name='coated_calcium_carbonate'),
    path('coated-calcium-carbonate.html', views.coated_calcium_carbonate),
    path('talc/', views.talc, name='talc'),
    path('talc.html', views.talc),
    path('afghan-talc/', views.afghan_talc, name='afghan_talc'),
    path('afghan-talc.html', views.afghan_talc),
    path('barite/', views.barite, name='barite'),
    path('barite.html', views.barite),
    path('ochre/', views.ochre, name='ochre'),
    path('ochre.html', views.ochre),
    path('<slug:slug>/', views.product_detail, name='detail'),
    path('<slug:slug>.html', views.product_detail),
]
