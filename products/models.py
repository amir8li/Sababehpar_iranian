from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    name_fa = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    name = models.CharField(max_length=150)
    name_fa = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    short_description_fa = models.TextField(blank=True, null=True)
    full_description = models.TextField(blank=True, null=True)
    purity = models.CharField(max_length=50, help_text="e.g. 99.2% CaCO3")
    whiteness = models.CharField(max_length=50, help_text="e.g. 98.5%")
    d50_size = models.CharField(max_length=50, help_text="e.g. 2.5 Micron")
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    tds_pdf = models.FileField(upload_to='product_tds/', blank=True, null=True, verbose_name="Technical Data Sheet (TDS)")
    coa_pdf = models.FileField(upload_to='product_coa/', blank=True, null=True, verbose_name="Certificate of Analysis (COA)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
