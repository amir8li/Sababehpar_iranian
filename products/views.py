from django.shortcuts import render
from django.template.loader import select_template
from .models import Product, ProductCategory

def product_list(request):
    products = Product.objects.filter(is_active=True)
    categories = ProductCategory.objects.all()
    return render(request, 'products/index.html', {
        'products': products,
        'categories': categories,
    })

def calcium_carbonate(request):
    product = Product.objects.filter(slug='calcium-carbonate').first()
    return render(request, 'products/calcium_carbonate.html', {'product': product})

def coated_calcium_carbonate(request):
    product = Product.objects.filter(slug='coated-calcium-carbonate').first()
    return render(request, 'products/coated_calcium_carbonate.html', {'product': product})

def talc(request):
    product = Product.objects.filter(slug='talc').first()
    return render(request, 'products/talc.html', {'product': product})

def afghan_talc(request):
    product = Product.objects.filter(slug='afghan-talc').first()
    return render(request, 'products/afghan_talc.html', {'product': product})

def barite(request):
    product = Product.objects.filter(slug='barite').first()
    return render(request, 'products/barite.html', {'product': product})

def ochre(request):
    product = Product.objects.filter(slug='ochre').first()
    return render(request, 'products/ochre.html', {'product': product})

def product_detail(request, slug):
    # Strip .html if present in slug
    clean_slug = slug.replace('.html', '')
    product = Product.objects.filter(slug=clean_slug, is_active=True).first()
    
    # Try finding specific static template first (e.g., products/calcium_carbonate.html)
    template_name = f"products/{clean_slug.replace('-', '_')}.html"
    try:
        select_template([template_name])
        return render(request, template_name, {'product': product})
    except:
        return render(request, 'products/detail.html', {'product': product})
