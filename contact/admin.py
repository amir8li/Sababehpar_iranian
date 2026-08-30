from django.contrib import admin
from .models import ContactInquiry

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'phone', 'inquiry_type', 'is_processed', 'created_at')
    list_filter = ('inquiry_type', 'is_processed', 'created_at')
    search_fields = ('name', 'company', 'email', 'phone', 'message')
    list_editable = ('is_processed',)
