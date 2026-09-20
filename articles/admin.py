from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title', 'title_fa', 'author', 'summary', 'summary_fa', 'content')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('English Content', {
            'fields': ('title', 'slug', 'author', 'summary', 'content', 'cover_image', 'pdf_file')
        }),
        ('Persian / Farsi Content (محتوای فارسی)', {
            'fields': ('title_fa', 'summary_fa', 'content_fa'),
        }),
        ('Publication Settings', {
            'fields': ('is_published',)
        }),
    )
