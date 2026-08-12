from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='index'),
    path('calcium-carbonate/', views.calcium_carbonate, name='calcium_carbonate'),
    path('coated-calcium-carbonate/', views.coated_calcium_carbonate, name='coated_calcium_carbonate'),
    path('talc/', views.talc, name='talc'),
    path('afghan-talc/', views.afghan_talc, name='afghan_talc'),
    path('barite/', views.barite, name='barite'),
    path('ochre/', views.ochre, name='ochre'),
    path('<slug:slug>/', views.product_detail, name='detail'),
]
