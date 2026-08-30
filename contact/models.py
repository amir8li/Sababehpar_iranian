from django.db import models

class ContactInquiry(models.Model):
    INQUIRY_TYPES = [
        ('general', 'General Inquiry'),
        ('quote', 'Fast Quote Request'),
        ('sample', 'Sample Request'),
        ('tour', 'Factory Tour Booking'),
    ]

    name = models.CharField(max_length=150)
    company = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    inquiry_type = models.CharField(max_length=30, choices=INQUIRY_TYPES, default='general')
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Inquiry'
        verbose_name_plural = 'Contact Inquiries'

    def __str__(self):
        return f"{self.name} - {self.get_inquiry_type_display()} ({self.created_at.strftime('%Y-%m-%d')})"
