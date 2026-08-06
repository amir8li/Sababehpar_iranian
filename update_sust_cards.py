import re
import os

keys_en = {
    'sust-hero-tag': 'GREEN MINING & ESG COMMITMENT',
    'sust-hero-title': 'Sustainability & Environmental Responsibility',
    'sust-hero-desc': 'Driving eco-friendly mining, closed-loop water recycling, and energy-efficient micronizing across Sababehpar Iranian operations.',
    'sust-page-badge': '01',
    'sust-page-title': 'Environmental Practices & Sustainable Mining',
    'about-esg-title': 'Key ESG Performance Metrics',
    'about-card-1-title': 'Energy Optimization',
    'about-card-1-desc': 'Gradual reduction of carbon footprint through smart automation and high-efficiency motors.',
    'about-card-2-title': 'Zero-Waste Production',
    'about-card-2-desc': 'Maximum utilization of extracted minerals by transforming every part of the ore into practical products.',
    'about-card-3-title': 'Air Quality Control',
    'about-card-3-desc': 'Advanced bag filters absorbing 99.9% of suspended particles for a pollution-free environment.',
    'about-card-4-title': 'Workforce Empowerment',
    'about-card-4-desc': 'Prioritizing local employment and continuous training to create sustainable job opportunities.',
    'about-card-5-title': 'HSE Standards',
    'about-card-5-desc': 'Strict preventive safety protocols ensuring the physical health and safety of all employees.'
}

keys_fa = {
    'sust-hero-tag': 'طرح معدنکاری سبز',
    'sust-hero-title': 'پایداری و مسئولیت محیط‌زیستی',
    'sust-hero-desc': 'پیشگام در معدنکاری دوستدار محیط‌زیست، بازچرخانی آب و میکرونیزاسیون کم‌مصرف در عملیات صبا بهپر.',
    'sust-page-badge': '۰۱',
    'sust-page-title': 'تعهد به پایداری محیط‌زیست و ESG',
    'about-esg-title': 'شاخص‌های کلیدی عملکرد ESG',
    'about-card-1-title': 'بهینه‌سازی انرژی',
    'about-card-1-desc': 'کاهش تدریجی ردپای کربنی از طریق هوشمندسازی و استفاده از موتورهای با بازدهی بالا.',
    'about-card-2-title': 'تولید بدون ضایعات',
    'about-card-2-desc': 'بهره‌برداری حداکثری از مواد معدنی و تبدیل تمامی بخش‌های سنگ به محصولات کاربردی.',
    'about-card-3-title': 'کنترل کیفیت هوا',
    'about-card-3-desc': 'استفاده از فیلترهای پیشرفته برای جذب ۹۹.۹ درصد ذرات معلق و تضمین هوای پاک.',
    'about-card-4-title': 'توانمندسازی نیروی کار',
    'about-card-4-desc': 'اولویت استخدام نیروهای بومی و آموزش مستمر برای ایجاد اشتغال پایدار.',
    'about-card-5-title': 'استانداردهای ایمنی (HSE)',
    'about-card-5-desc': 'اجرای پروتکل‌های سختگیرانه و پیشگیرانه برای تضمین سلامت فیزیکی تمامی کارکنان.'
}

keys_ar = {
    'sust-hero-tag': 'مبادرة التعدين الأخضر',
    'sust-hero-title': 'الاستدامة والمسؤولية البيئية',
    'sust-hero-desc': 'الريادة في التعدين الصديق للبيئة، وإعادة تدوير المياه، والميكرونة الموفرة للطاقة في صبا بهپر.',
    'sust-page-badge': '٠١',
    'sust-page-title': 'الممارسات البيئية والتعدين المستدام',
    'about-esg-title': 'مقاييس الأداء الرئيسية ESG',
    'about-card-1-title': 'تحسين الطاقة',
    'about-card-1-desc': 'التخفيض التدريجي للبصمة الكربونية من خلال الأتمتة الذكية.',
    'about-card-2-title': 'إنتاج خالي من النفايات',
    'about-card-2-desc': 'الاستفادة القصوى من المعادن وتحويل كل جزء من الخام إلى منتجات عملية.',
    'about-card-3-title': 'مراقبة جودة الهواء',
    'about-card-3-desc': 'استخدام فلاتر متقدمة لامتصاص ٩٩.٩٪ من الجسيمات العالقة.',
    'about-card-4-title': 'تمكين القوى العاملة',
    'about-card-4-desc': 'إعطاء الأولوية للتوظيف المحلي والتدريب المستمر لخلق فرص عمل مستدامة.',
    'about-card-5-title': 'معايير السلامة المهنية',
    'about-card-5-desc': 'تنفيذ بروتوكولات وقائية صارمة لضمان الصحة البدنية لجميع الموظفين.'
}

# Fix about/sustainability.html IDs
with open('about/sustainability.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change about-sust-badge to sust-page-badge in this file ONLY
html = html.replace('id="about-sust-badge"', 'id="sust-page-badge"')
html = html.replace('id="about-sust-title"', 'id="sust-page-title"')

# Also update the hardcoded card icons and titles
html = html.replace('<span style="font-size: 2rem;">💧</span>', '<span style="font-size: 2rem;">⚡</span>')
# Wait, let's just do a manual replace for the cards section.
import re

# Update HTML card icons to match the new text
html = html.replace('💧', '⚡', 1)
html = html.replace('⚡', '♻️', 1) # wait, replace limits?
html = html.replace('🌿', '🌬️', 1)
html = html.replace('🏞️', '👥', 1)
html = html.replace('🌍', '🛡️', 1)

with open('about/sustainability.html', 'w', encoding='utf-8') as f:
    f.write(html)


with open('lang.js', 'r', encoding='utf-8') as f:
    lang = f.read()

def inject_keys(lang_text, new_dict, anchor_key):
    # Find where the anchor key is in the file, then inject right after it
    # to avoid the replace issue, we will construct the injection string
    injection = ""
    for k, v in new_dict.items():
        if f"'{k}':" not in lang_text:
            injection += f"        '{k}': '{v}',\n"
        else:
            # if exists, replace it
            lang_text = re.sub(rf"'{k}': '[^']*',", f"'{k}': '{v}',", lang_text)
    
    if injection:
        anchor_str = f"'{anchor_key}':"
        # Find the anchor string and inject after its line
        parts = lang_text.split(anchor_str)
        if len(parts) > 1:
            # We must be careful because anchor_key might appear multiple times (EN, FA, AR)
            # but we only want the one in the specific block.
            pass
    return lang_text

# It's safer to just inject at the very end of the translations object, but translations has nested dicts.
# Let's just do precise regex replacements for the blocks.

# EN block ends before 'fa': {
en_block, rest = lang.split("'fa': {", 1)
for k, v in keys_en.items():
    if f"'{k}':" not in en_block:
        en_block = en_block.replace("'about-esg-title': 'Key ESG Performance Metrics',", f"'{k}': '{v}',\n        'about-esg-title': 'Key ESG Performance Metrics',")
    else:
        en_block = re.sub(rf"'{k}': '[^']*',", f"'{k}': '{v}',", en_block)

fa_block, ar_block = rest.split("'ar': {", 1)
for k, v in keys_fa.items():
    if f"'{k}':" not in fa_block:
        fa_block = fa_block.replace("'about-esg-title': 'شاخص‌های کلیدی عملکرد ESG',", f"'{k}': '{v}',\n        'about-esg-title': 'شاخص‌های کلیدی عملکرد ESG',")
    else:
        fa_block = re.sub(rf"'{k}': '[^']*',", f"'{k}': '{v}',", fa_block)

for k, v in keys_ar.items():
    if f"'{k}':" not in ar_block:
        # Arabic might not have about-esg-title. Let's inject after about-sust-p5
        if "'about-sust-p5':" in ar_block:
            ar_block = re.sub(r"('about-sust-p5': '[^']*',)", r"\1\n        '" + k + "': '" + v + "',", ar_block)
        else:
            ar_block = ar_block.replace("}", f"        '{k}': '{v}',\n    }}") # very fragile
    else:
        ar_block = re.sub(rf"'{k}': '[^']*',", f"'{k}': '{v}',", ar_block)


new_lang = en_block + "'fa': {" + fa_block + "'ar': {" + ar_block

# Update mapIds
for k in keys_en.keys():
    if f"'{k}':" not in new_lang:
        new_lang = new_lang.replace("'about-esg-title': '#about-esg-title',", f"'{k}': '#{k}',\n    'about-esg-title': '#about-esg-title',")

with open('lang.js', 'w', encoding='utf-8') as f:
    f.write(new_lang)

os.remove('update_sust_cards.py')
print("done updating sustainability cards")
