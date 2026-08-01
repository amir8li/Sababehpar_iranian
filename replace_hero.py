import re

with open('industries/index.html', 'r') as f:
    content = f.read()

old_hero = r'''        <!-- Industries Hero -->\s*<section class="page-hero" style="background-image: linear-gradient\(rgba\(10,10,12,0.8\), rgba\(10,10,12,0.8\)\), url\('\.\./assets/images/products_hero\.jpg'\);">\s*<div class="container page-hero__inner">\s*<h1 class="page-hero__title" id="industries-hero-title">Industries We Serve</h1>\s*<p class="page-hero__text" id="industries-hero-text">High-performance mineral solutions tailored for diverse industrial applications\.</p>\s*</div>\s*</section>'''

new_hero = """    <header class="about-page-hero" style="background: url('../assets/images/products_hero.jpg') center/cover no-repeat;">
        <div class="hero__overlay" style="background: linear-gradient(to right, rgba(10,10,12,0.9), rgba(10,10,12,0.5));"></div>
        <div class="container hero__content" style="z-index: 2;">
            <div style="max-width: 700px;">
                <span class="hero__tag" id="industries-badge" style="background: rgba(222,131,75,0.18); color: #de834b; border: 1px solid rgba(222,131,75,0.4); margin-bottom: 1rem; display: inline-block; padding: 0.4rem 1rem; border-radius: 50px; font-weight: 600; font-size: 0.85rem; letter-spacing: 1px; text-transform: uppercase;">Global Reach</span>
                <h1 id="industries-hero-title" style="font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: #FFF; line-height: 1.1; margin-bottom: 1.5rem;">Industries We <span style="color: #de834b;">Serve</span></h1>
                <p id="industries-hero-text" style="font-size: 1.1rem; color: rgba(255,255,255,0.8); line-height: 1.7;">High-performance mineral solutions tailored for diverse industrial applications.</p>
            </div>
        </div>
    </header>"""

new_content = re.sub(old_hero, new_hero, content)

with open('industries/index.html', 'w') as f:
    f.write(new_content)
