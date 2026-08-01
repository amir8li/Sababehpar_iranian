import re

with open('about/index.html', 'r') as f:
    shell = f.read()

# 1. Extract shell
header_match = re.search(r'(<!DOCTYPE html>.*?</nav>)', shell, re.DOTALL)
footer_match = re.search(r'(<footer class="footer".*</html>)', shell, re.DOTALL)

head = header_match.group(1)
foot = footer_match.group(1)

# 2. Fix head links
head = head.replace('<title>About Us | Sababehpar Iranian Mining Co.</title>', '<title>Industries | Sababehpar Iranian</title>')
head = head.replace('href="../about/index.html" class="navbar__link active"', 'href="../about/index.html" class="navbar__link"')

# The navbar in about/index.html already has the Industries link fixed from my previous fix_industries_nav.py script!
# Let's just make the Industries link active.
head = head.replace('href="../industries/index.html" class="navbar__link" id="nav-industries"', 'href="../industries/index.html" class="navbar__link active" id="nav-industries"')
head = head.replace('href="../industries/index.html" class="navbar__mobile-link" id="mobile-industries"', 'href="../industries/index.html" class="navbar__mobile-link active" id="mobile-industries"')

# 3. Proper Modal HTML
modal_html = """
    <div class="industry-modal" id="industry-modal">
        <div class="industry-modal__overlay" id="modal-overlay"></div>
        <div class="industry-modal__content" id="modal-content">
            <button class="industry-modal__close" id="modal-close" aria-label="Close modal">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
            </button>
            <div class="industry-modal__icon" id="modal-icon"></div>
            <h3 class="industry-modal__title" id="modal-title"></h3>
            <p class="industry-modal__description" id="modal-description"></p>
            <div class="industry-modal__specs" id="modal-specs"></div>
            <a href="../contact/index.html" class="btn btn--gold" id="modal-cta">Request Industry Sample</a>
        </div>
    </div>
"""

# 4. Main HTML
main_html = """
    <main class="page-main">
        <!-- Industries Hero -->
        <section class="page-hero" style="background-image: linear-gradient(rgba(10,10,12,0.8), rgba(10,10,12,0.8)), url('../assets/images/products_hero.jpg');">
            <div class="container page-hero__inner">
                <h1 class="page-hero__title" id="industries-hero-title">Industries We Serve</h1>
                <p class="page-hero__text" id="industries-hero-text">High-performance mineral solutions tailored for diverse industrial applications.</p>
            </div>
        </section>

        <!-- Industries Grid -->
        <section class="products-grid-section section-padding">
            <div class="container">
                <div class="products-grid">
                
                    <div class="industry-card products-grid__card" data-industry="paint" id="industry-paint">
                        <img src="../assets/images/ind_paint.jpg" alt="Paint & Resin" class="products-grid__img">
                        <div class="products-grid__content">
                            <h3 class="industry-card__title" id="ind-card-paint-title">Paint & Resin</h3>
                            <p class="industry-card__text" id="ind-card-paint-desc">Essential mineral filler for paints and industrial coatings.</p>
                        </div>
                    </div>

                    <div class="industry-card products-grid__card" data-industry="plastics" id="industry-plastics">
                        <img src="../assets/images/ind_plastics.jpg" alt="Plastics & Polymers" class="products-grid__img">
                        <div class="products-grid__content">
                            <h3 class="industry-card__title" id="ind-card-plastics-title">Plastics & Polymers</h3>
                            <p class="industry-card__text" id="ind-card-plastics-desc">High-quality filler for masterbatches and polymer compounds.</p>
                        </div>
                    </div>

                    <div class="industry-card products-grid__card" data-industry="pvc" id="industry-pvc">
                        <img src="../assets/images/ind_pvc.jpg" alt="PVC, UPVC & Profiles" class="products-grid__img">
                        <div class="products-grid__content">
                            <h3 class="industry-card__title" id="ind-card-pvc-title">PVC, UPVC & Profiles</h3>
                            <p class="industry-card__text" id="ind-card-pvc-desc">Crucial ingredient for window profiles, wall panels, and flooring.</p>
                        </div>
                    </div>

                    <div class="industry-card products-grid__card" data-industry="paper" id="industry-paper">
                        <img src="../assets/images/ind_paper.jpg" alt="Paper & Cardboard" class="products-grid__img">
                        <div class="products-grid__content">
                            <h3 class="industry-card__title" id="ind-card-paper-title">Paper & Cardboard</h3>
                            <p class="industry-card__text" id="ind-card-paper-desc">Improves whiteness, surface uniformity, and printability.</p>
                        </div>
                    </div>

                    <div class="industry-card products-grid__card" data-industry="feed" id="industry-feed">
                        <img src="../assets/images/ind_feed.jpg" alt="Animal & Poultry Feed" class="products-grid__img">
                        <div class="products-grid__content">
                            <h3 class="industry-card__title" id="ind-card-feed-title">Animal & Poultry Feed</h3>
                            <p class="industry-card__text" id="ind-card-feed-desc">Rich calcium source for livestock, poultry, and aquatic feed.</p>
                        </div>
                    </div>

                    <div class="industry-card products-grid__card" data-industry="rubber" id="industry-rubber">
                        <img src="../assets/images/ind_rubber.jpg" alt="Rubber & Foam" class="products-grid__img">
                        <div class="products-grid__content">
                            <h3 class="industry-card__title" id="ind-card-rubber-title">Rubber & Foam</h3>
                            <p class="industry-card__text" id="ind-card-rubber-desc">Enhances physical properties and flowability in rubber compounds.</p>
                        </div>
                    </div>

                    <div class="industry-card products-grid__card" data-industry="construction" id="industry-construction">
                        <img src="../assets/images/ind_construction.jpg" alt="Tiles & Construction" class="products-grid__img">
                        <div class="products-grid__content">
                            <h3 class="industry-card__title" id="ind-card-construction-title">Tiles & Construction</h3>
                            <p class="industry-card__text" id="ind-card-construction-desc">Used in ceramic bodies, dry mortars, tile adhesives, and putties.</p>
                        </div>
                    </div>

                </div>
            </div>
        </section>
    </main>
"""

final_html = head + "\n" + main_html + "\n" + modal_html + "\n" + foot

with open('industries/index.html', 'w') as f:
    f.write(final_html)

