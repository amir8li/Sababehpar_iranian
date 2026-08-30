from django.contrib import admin
from .models import ProductCategory, Product

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_fa', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'purity', 'whiteness', 'd50_size', 'is_active', 'created_at')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'short_description', 'purity')
    prepopulated_fields = {'slug': ('name',)}
