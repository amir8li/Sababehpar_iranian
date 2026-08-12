from django.shortcuts import render
from django.contrib import messages
from .models import ContactInquiry

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        company = request.POST.get('company', '')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        inquiry_type = request.POST.get('inquiry_type', 'general')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        if name and email and phone:
            ContactInquiry.objects.create(
                name=name,
                company=company,
                email=email,
                phone=phone,
                inquiry_type=inquiry_type,
                subject=subject,
                message=message,
            )
            messages.success(request, 'Thank you! Your request has been submitted successfully.')
            return render(request, 'contact/index.html', {'submitted': True})
        else:
            messages.error(request, 'Please fill in all required fields.')

    return render(request, 'contact/index.html')
