import os
import re

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.venv' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            dir_depth = root.count(os.sep)
            depth_prefix = '../' * dir_depth if root != '.' else ''

            with open(filepath, 'r') as f:
                content = f.read()

            # 1. Remove Duplicate Floating Phones
            # Find all <div class="floating-phone" ...> and remove them.
            # Then we'll re-inject the good one at the bottom.
            # Actually, I can just find the LAST one, keep it, and remove all earlier ones.
            fp_indices = [m.start() for m in re.finditer(r'<div class="floating-phone"', content)]
            if len(fp_indices) > 1:
                # keep only the last one
                last_fp = fp_indices[-1]
                # remove all before it
                for idx in reversed(fp_indices[:-1]):
                    # find the end of this block. It ends with '</div>\n    </div>\n    </div>' or similar
                    end_idx = content.find('id="phone-linkedin"', idx)
                    if end_idx != -1:
                        end_idx = content.find('</div>', end_idx) # close a tag
                        end_idx = content.find('</div>', end_idx+1) # close messengers
                        end_idx = content.find('</div>', end_idx+1) # close popup
                        end_idx = content.find('</div>', end_idx+1) # close floating-phone
                        if end_idx != -1:
                            content = content[:idx] + content[end_idx+6:]

            # 2. Fix Header Social Media (move WhatsApp)
            # Remove WhatsApp from utility-header__contact if it's there
            whatsapp_link_wrong = r'<a href="https://wa\.me/989123956647" class="utility-header__link" aria-label="WhatsApp">.*?</a>\s*'
            content = re.sub(whatsapp_link_wrong, '', content, flags=re.DOTALL)
            
            # Inject WhatsApp into utility-header__actions next to social-icon
            # We look for <a href="#" aria-label="LinkedIn" class="social-icon" id="social-linkedin">
            whatsapp_social_icon = '<a href="https://wa.me/989123956647" aria-label="WhatsApp" class="social-icon" id="social-whatsapp">\n                        <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>\n                    </a>'
            
            if 'id="social-whatsapp"' not in content and 'id="social-linkedin"' in content:
                content = content.replace('<a href="#" aria-label="LinkedIn" class="social-icon" id="social-linkedin">',
                                          whatsapp_social_icon + '\n                    <a href="#" aria-label="LinkedIn" class="social-icon" id="social-linkedin">')

            # 3. Fix Navbar Products Links
            # Replace all occurrences of Products Overview link
            content = re.sub(r'<a href="[^"]*index\.html" class="navbar__dropdown-item( active)?" id="nav-products-overview"', 
                             f'<a href="{depth_prefix}products/index.html" class="navbar__dropdown-item\\1" id="nav-products-overview"', content)
            content = re.sub(r'<a href="[^"]*calcium-carbonate\.html" class="navbar__dropdown-item( active)?" id="nav-products-caco3"', 
                             f'<a href="{depth_prefix}products/calcium-carbonate.html" class="navbar__dropdown-item\\1" id="nav-products-caco3"', content)
            content = re.sub(r'<a href="[^"]*talc\.html" class="navbar__dropdown-item( active)?" id="nav-products-talc"', 
                             f'<a href="{depth_prefix}products/talc.html" class="navbar__dropdown-item\\1" id="nav-products-talc"', content)

            with open(filepath, 'w') as f:
                f.write(content)

