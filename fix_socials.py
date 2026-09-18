import re

# 1. Fix contact/index.html
with open('templates/contact/index.html', 'r', encoding='utf-8') as f:
    contact = f.read()

# Replace Telegram link
contact = contact.replace('href="#" aria-label="Telegram"', 'href="https://t.me/Sababehpariranian" target="_blank" rel="noopener noreferrer" aria-label="Telegram"')

# Add Rubica and Bale
# Find the social media div
social_match = re.search(r'(<div style="display: flex; gap: 16px;">.*?)(</div>\s*</div>\s*</div>)', contact, flags=re.DOTALL)
if social_match:
    social_block = social_match.group(1)
    
    bale_svg = '<a href="https://ble.ir/989123956647" target="_blank" rel="noopener noreferrer" aria-label="Bale" style="display:inline-block; transition: transform 0.2s;"><svg width="24" height="24" viewBox="0 0 24 24" fill="#00B52B"><rect width="24" height="24" rx="12"/><text x="12" y="16" font-weight="bold" font-size="12" font-family="sans-serif" fill="#fff" text-anchor="middle">بله</text></svg></a>'
    
    rubica_svg = '<a href="https://rubika.ir/989123956647" target="_blank" rel="noopener noreferrer" aria-label="Rubica" style="display:inline-block; transition: transform 0.2s;"><svg width="24" height="24" viewBox="0 0 24 24" fill="#9B59B6"><rect width="24" height="24" rx="5"/><text x="12" y="16" font-weight="bold" font-size="12" font-family="sans-serif" fill="#fff" text-anchor="middle">روبیکا</text></svg></a>'
    
    new_social_block = social_block + "\n                                " + bale_svg + "\n                                " + rubica_svg + "\n                            "
    contact = contact.replace(social_block, new_social_block)
else:
    print("Could not find social media div in contact/index.html")

with open('templates/contact/index.html', 'w', encoding='utf-8') as f:
    f.write(contact)


# 2. Fix base.html (emails and telegram)
with open('templates/base.html', 'r', encoding='utf-8') as f:
    base = f.read()

# Add second email
email_block = """<a href="mailto:info@sababehpar.com" class="utility-header__link" id="header-email">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
                    <span dir="ltr">info@sababehpar.com</span>
                </a>"""

new_email_block = """<a href="mailto:info@sababehpar.com" class="utility-header__link" id="header-email">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
                    <span dir="ltr">info@sababehpar.com</span>
                </a>
                <span style="color: rgba(255,255,255,0.3); margin: 0 4px;">|</span>
                <a href="mailto:info@sababehpariranian.com" class="utility-header__link" id="header-email-2">
                    <span dir="ltr">info@sababehpariranian.com</span>
                </a>"""

base = base.replace(email_block, new_email_block)

# Add Telegram to base social icons
telegram_icon_15 = """<a href="https://t.me/Sababehpariranian" target="_blank" rel="noopener noreferrer" aria-label="Telegram" class="social-icon" id="social-telegram">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.479.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
                    </a>"""

telegram_icon_22 = """<a href="https://t.me/Sababehpariranian" target="_blank" rel="noopener noreferrer" aria-label="Telegram" class="social-icon" style="color: rgba(255, 255, 255, 0.7); display: flex; align-items: center; transition: color 0.3s;">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.479.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
                </a>"""
                
telegram_icon_20 = """<a href="https://t.me/Sababehpariranian" target="_blank" rel="noopener noreferrer" aria-label="Telegram" class="social-icon" style="color: rgba(255, 255, 255, 0.65); display: flex; align-items: center; transition: color 0.3s, transform 0.3s;">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.479.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
                    </a>"""

# Insert before Instagram
base = re.sub(r'(<a href="https://www.instagram.com/sababehpariranian/".*?id="social-instagram">)', telegram_icon_15 + r'\n                    \1', base)
base = re.sub(r'(<a href="https://www.instagram.com/sababehpariranian/".*?transition: color 0\.3s;">\s*<svg width="22")', telegram_icon_22 + r'\n                \1', base)
base = re.sub(r'(<a href="https://www.instagram.com/sababehpariranian/".*?transition: color 0\.3s, transform 0\.3s;">\s*<svg width="20")', telegram_icon_20 + r'\n                    \1', base)

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(base)

