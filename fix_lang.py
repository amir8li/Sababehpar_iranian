import re

with open('lang.js', 'r') as f:
    content = f.read()

# Add to 'en'
en_add = """'about-sustain-title': 'Commitment to Sustainability',
    'industries-badge': 'Global Reach',
    'industries-hero-title': 'Industries We <span style="color: #de834b;">Serve</span>',
    'industries-hero-text': 'High-performance mineral solutions tailored for diverse industrial applications.',"""
content = re.sub(r"'about-sustain-title': 'Commitment to Sustainability',", en_add, content)

# Add to 'fa'
fa_add = """'about-sustain-title': 'تعهد به پایداری',
        'industries-badge': 'دسترسی جهانی',
        'industries-hero-title': 'صنایعی که به آنها <span style="color: #de834b;">خدمت می‌کنیم</span>',
        'industries-hero-text': 'راه‌حل‌های معدنی با کارایی بالا، سفارشی‌سازی شده برای کاربردهای متنوع صنعتی.',"""
content = re.sub(r"'about-sustain-title': 'تعهد به پایداری',", fa_add, content)

# Add to elementsToTranslate
elem_add = """'about-sustain-title': '#about-sustain-title',
    'industries-badge': '#industries-badge',
    'industries-hero-title': '#industries-hero-title',
    'industries-hero-text': '#industries-hero-text',"""
content = re.sub(r"'about-sustain-title': '#about-sustain-title',", elem_add, content)

with open('lang.js', 'w') as f:
    f.write(content)
