from django.shortcuts import render
from .models import TeamMember
from news.models import NewsArticle
from products.models import Product

def home(request):
    latest_news = NewsArticle.objects.filter(is_published=True)[:3]
    featured_products = Product.objects.filter(is_active=True)[:4]
    context = {
        'latest_news': latest_news,
        'featured_products': featured_products,
    }
    return render(request, 'website/index.html', context)

def about(request):
    team_members = TeamMember.objects.all()[:5]
    return render(request, 'website/about.html', {'team_members': team_members})

def management_team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'website/management_team.html', {'team_members': team_members})

def sustainability(request):
    return render(request, 'website/sustainability.html')

def industries(request):
    return render(request, 'website/industries.html')

def knowledge_center(request):
    return render(request, 'knowledge_center/index.html')

def quality_control(request):
    return render(request, 'knowledge_center/quality_control.html')

def labs(request):
    return render(request, 'knowledge_center/labs.html')

def certifications(request):
    return render(request, 'knowledge_center/certifications.html')
