from django.db import models

class NewsArticle(models.Model):
    CATEGORY_CHOICES = [
        ('company', 'Company News'),
        ('rd', 'R&D & Innovation'),
        ('press', 'Press Release'),
        ('sustainability', 'Sustainability'),
    ]

    title = models.CharField(max_length=255)
    title_fa = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title (Farsi)")
    slug = models.SlugField(unique=True, max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='company')
    summary = models.TextField()
    summary_fa = models.TextField(blank=True, null=True, verbose_name="Summary (Farsi)")
    content = models.TextField()
    content_fa = models.TextField(blank=True, null=True, verbose_name="Content (Farsi)")
    cover_image = models.ImageField(upload_to='news_covers/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'News Article'
        verbose_name_plural = 'News Articles'

    def __str__(self):
        return self.title

    @property
    def display_title(self):
        from django.utils import translation
        lang = translation.get_language()
        if lang and lang.startswith('fa') and self.title_fa:
            return self.title_fa
        return self.title

    @property
    def display_summary(self):
        from django.utils import translation
        lang = translation.get_language()
        if lang and lang.startswith('fa') and self.summary_fa:
            return self.summary_fa
        return self.summary

    @property
    def display_content(self):
        from django.utils import translation
        lang = translation.get_language()
        if lang and lang.startswith('fa') and self.content_fa:
            return self.content_fa
        return self.content


class TechnicalArticle(models.Model):
    title = models.CharField(max_length=255)
    title_fa = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title (Farsi)")
    slug = models.SlugField(unique=True, max_length=255)
    author = models.CharField(max_length=150, default="Sababehpar R&D Team")
    summary = models.TextField()
    summary_fa = models.TextField(blank=True, null=True, verbose_name="Summary (Farsi)")
    content = models.TextField()
    content_fa = models.TextField(blank=True, null=True, verbose_name="Content (Farsi)")
    pdf_file = models.FileField(upload_to='technical_papers/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='article_covers/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Technical Article'
        verbose_name_plural = 'Technical Articles'

    def __str__(self):
        return self.title

    @property
    def display_title(self):
        from django.utils import translation
        lang = translation.get_language()
        if lang and lang.startswith('fa') and self.title_fa:
            return self.title_fa
        return self.title

    @property
    def display_summary(self):
        from django.utils import translation
        lang = translation.get_language()
        if lang and lang.startswith('fa') and self.summary_fa:
            return self.summary_fa
        return self.summary

    @property
    def display_content(self):
        from django.utils import translation
        lang = translation.get_language()
        if lang and lang.startswith('fa') and self.content_fa:
            return self.content_fa
        return self.content
