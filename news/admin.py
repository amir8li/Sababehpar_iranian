from django.contrib import admin
from .models import NewsArticle

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'created_at')
    list_filter = ('category', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title', 'title_fa', 'summary', 'summary_fa', 'content')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('English Content', {
            'fields': ('title', 'slug', 'category', 'summary', 'content', 'cover_image')
        }),
        ('Persian / Farsi Content (محتوای فارسی)', {
            'fields': ('title_fa', 'summary_fa', 'content_fa'),
        }),
        ('Publication Settings', {
            'fields': ('is_published',)
        }),
    )
