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

from django.http import HttpResponse

def robots_txt(request):
    host = request.get_host()
    scheme = 'https' if request.is_secure() else 'http'
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        f"Sitemap: {scheme}://{host}/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def sitemap_xml(request):
    host = request.get_host()
    scheme = 'https' if request.is_secure() else 'http'
    base = f"{scheme}://{host}"
    
    urls = [
        {'loc': f"{base}/", 'changefreq': 'daily', 'priority': '1.0'},
        {'loc': f"{base}/about/", 'changefreq': 'weekly', 'priority': '0.8'},
        {'loc': f"{base}/about/management-team/", 'changefreq': 'monthly', 'priority': '0.6'},
        {'loc': f"{base}/about/sustainability/", 'changefreq': 'monthly', 'priority': '0.6'},
        {'loc': f"{base}/industries/", 'changefreq': 'weekly', 'priority': '0.8'},
        {'loc': f"{base}/products/", 'changefreq': 'daily', 'priority': '0.9'},
        {'loc': f"{base}/products/calcium-carbonate/", 'changefreq': 'weekly', 'priority': '0.9'},
        {'loc': f"{base}/products/coated-calcium-carbonate/", 'changefreq': 'weekly', 'priority': '0.9'},
        {'loc': f"{base}/products/talc/", 'changefreq': 'weekly', 'priority': '0.8'},
        {'loc': f"{base}/products/afghan-talc/", 'changefreq': 'weekly', 'priority': '0.8'},
        {'loc': f"{base}/products/barite/", 'changefreq': 'weekly', 'priority': '0.8'},
        {'loc': f"{base}/products/ochre/", 'changefreq': 'weekly', 'priority': '0.8'},
        {'loc': f"{base}/news/", 'changefreq': 'daily', 'priority': '0.8'},
        {'loc': f"{base}/articles/", 'changefreq': 'daily', 'priority': '0.8'},
        {'loc': f"{base}/articles/article-1/", 'changefreq': 'monthly', 'priority': '0.7'},
        {'loc': f"{base}/knowledge-center/", 'changefreq': 'weekly', 'priority': '0.7'},
        {'loc': f"{base}/knowledge-center/quality-control/", 'changefreq': 'monthly', 'priority': '0.6'},
        {'loc': f"{base}/knowledge-center/labs/", 'changefreq': 'monthly', 'priority': '0.6'},
        {'loc': f"{base}/knowledge-center/certifications/", 'changefreq': 'monthly', 'priority': '0.6'},
        {'loc': f"{base}/contact/", 'changefreq': 'monthly', 'priority': '0.7'},
    ]
    
    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u in urls:
        xml.append('  <url>')
        xml.append(f"    <loc>{u['loc']}</loc>")
        xml.append(f"    <changefreq>{u['changefreq']}</changefreq>")
        xml.append(f"    <priority>{u['priority']}</priority>")
        xml.append('  </url>')
    xml.append('</urlset>')
    
    return HttpResponse("\n".join(xml), content_type="application/xml")

