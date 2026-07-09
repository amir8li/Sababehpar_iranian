/**
 * Sababehpar Iranian Mining Company
 * Homepage Interactive Scripts
 * 
 * Sections:
 * 1. Hero Slideshow
 * 2. Navbar Scroll & Mobile Menu
 * 3. Language Selector
 * 4. Stats Counter Animation
 * 5. Industries Carousel & Modal
 * 6. Floating Phone Widget
 * 7. Scroll Reveal Animations
 * 8. Smooth Scroll & Active Nav
 */

document.addEventListener('DOMContentLoaded', () => {

    /* =========================================
       1. HERO SLIDESHOW
       ========================================= */

    const slides = document.querySelectorAll('.hero__slide');
    const dots = document.querySelectorAll('.hero__dot');
    let currentSlide = 0;
    let slideInterval;

    function goToSlide(index) {
        slides.forEach(s => s.classList.remove('active'));
        dots.forEach(d => d.classList.remove('active'));
        currentSlide = index;
        slides[currentSlide].classList.add('active');
        dots[currentSlide].classList.add('active');
    }

    function nextSlide() {
        goToSlide((currentSlide + 1) % slides.length);
    }

    function startSlideshow() {
        slideInterval = setInterval(nextSlide, 5000);
    }

    function stopSlideshow() {
        clearInterval(slideInterval);
    }

    // Dot click handlers
    dots.forEach(dot => {
        dot.addEventListener('click', () => {
            stopSlideshow();
            goToSlide(parseInt(dot.dataset.slide));
            startSlideshow();
        });
    });

    startSlideshow();


    /* =========================================
       2. NAVBAR SCROLL EFFECT & MOBILE MENU
       ========================================= */

    const navbar = document.getElementById('navbar');
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobile-menu');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        mobileMenu.classList.toggle('open');
    });

    // Close mobile menu on link click
    document.querySelectorAll('.navbar__mobile-link').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            mobileMenu.classList.remove('open');
        });
    });


    /* =========================================
       3. LANGUAGE SELECTOR
       ========================================= */

    const langToggle = document.getElementById('lang-toggle');
    const langDropdown = document.getElementById('lang-dropdown');

    langToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        langDropdown.classList.toggle('open');
    });

    document.addEventListener('click', () => {
        langDropdown.classList.remove('open');
    });

    document.querySelectorAll('.language-selector__option').forEach(option => {
        option.addEventListener('click', (e) => {
            e.preventDefault();
            document.querySelectorAll('.language-selector__option').forEach(o => o.classList.remove('active'));
            option.classList.add('active');
            langToggle.childNodes[2].textContent = ` ${option.textContent.trim().substring(0, 2).toUpperCase()} `;
            langDropdown.classList.remove('open');
        });
    });


    /* =========================================
       4. STATS COUNTER ANIMATION
       ========================================= */

    const statNumbers = document.querySelectorAll('.about__stat-number');
    let statsAnimated = false;

    function animateCounters() {
        statNumbers.forEach(counter => {
            const target = parseInt(counter.dataset.target);
            const duration = 2000;
            const startTime = performance.now();

            function updateCount(currentTime) {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);
                // Ease-out cubic
                const eased = 1 - Math.pow(1 - progress, 3);
                let text = Math.round(target * eased).toString();
                if (document.documentElement.dir === 'rtl') {
                    const faDigits = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
                    text = text.replace(/\d/g, d => faDigits[d]);
                }
                counter.textContent = text;
                if (progress < 1) {
                    requestAnimationFrame(updateCount);
                }
            }

            requestAnimationFrame(updateCount);
        });
    }

    // Observe stats section for intersection
    const statsSection = document.getElementById('about-stats');
    if (statsSection) {
        const statsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !statsAnimated) {
                    statsAnimated = true;
                    animateCounters();
                }
            });
        }, { threshold: 0.5 });

        statsObserver.observe(statsSection);
    }


    /* =========================================
       5. INDUSTRIES CAROUSEL & MODAL
       ========================================= */

    const track = document.getElementById('industries-track');
    const prevBtn = document.getElementById('carousel-prev');
    const nextBtn = document.getElementById('carousel-next');

    function getCardWidth() {
        const cards = track.querySelectorAll('.industry-card');
        if (cards.length === 0) return 0;
        const style = getComputedStyle(track);
        const gap = parseFloat(style.gap) || 24;
        return cards[0].offsetWidth + gap;
    }

    if (prevBtn && nextBtn && track) {
        let isAnimating = false;

        nextBtn.addEventListener('click', () => {
            if (isAnimating) return;
            isAnimating = true;

            const step = getCardWidth();
            const dir = document.documentElement.dir === 'rtl' ? 1 : -1;
            
            track.style.transition = 'transform 0.5s ease';
            track.style.transform = `translateX(${dir * step}px)`;

            setTimeout(() => {
                track.style.transition = 'none';
                track.appendChild(track.firstElementChild);
                track.style.transform = 'translateX(0)';
                track.offsetHeight; // force reflow
                isAnimating = false;
            }, 500);
        });

        prevBtn.addEventListener('click', () => {
            if (isAnimating) return;
            isAnimating = true;

            const step = getCardWidth();
            const dir = document.documentElement.dir === 'rtl' ? 1 : -1;
            
            track.insertBefore(track.lastElementChild, track.firstElementChild);
            track.style.transition = 'none';
            track.style.transform = `translateX(${dir * step}px)`;
            
            track.offsetHeight; // force reflow

            track.style.transition = 'transform 0.5s ease';
            track.style.transform = 'translateX(0)';

            setTimeout(() => {
                isAnimating = false;
            }, 500);
        });
    }

    // Industry Modal
    const modal = document.getElementById('industry-modal');
    const modalOverlay = document.getElementById('modal-overlay');
    const modalClose = document.getElementById('modal-close');
    const modalTitle = document.getElementById('modal-title');
    const modalDescription = document.getElementById('modal-description');
    const modalSpecs = document.getElementById('modal-specs');
    const modalIcon = document.getElementById('modal-icon');

    window.industryData = {
        paint: {
            title: 'Paint & Coatings Industry',
            description: 'Calcium carbonate serves as a critical extender and filler in paint formulations. Our ultra-fine GCC and coated CaCO₃ provide excellent whiteness, opacity control, and viscosity management while significantly reducing production costs.',
            specs: [
                { label: 'Recommended Mesh', value: '800 – 2500' },
                { label: 'Whiteness Required', value: '96%+' },
                { label: 'Coating Type', value: 'Stearic Acid' },
                { label: 'Application', value: 'Interior & Exterior' }
            ]
        },
        plastics: {
            title: 'Plastics & Polymers Industry',
            description: 'Our coated CaCO₃ serves as an impact modifier and cost-effective filler in PVC, PP, and PE compounds. The stearic acid coating ensures excellent dispersion and compatibility with polymer matrices.',
            specs: [
                { label: 'Recommended Mesh', value: '1500 – 3500' },
                { label: 'Purity Required', value: '98%+' },
                { label: 'Coating', value: 'Stearic Coated' },
                { label: 'Application', value: 'PVC Pipes, PE Films' }
            ]
        },
        adhesive: {
            title: 'Adhesive & Mastic Industry',
            description: 'Micronized calcium carbonate acts as a rheology modifier and thixotropic agent in sealants, adhesives, and mastic compounds. Our precise particle size distribution ensures optimal consistency.',
            specs: [
                { label: 'Recommended Mesh', value: '400 – 1500' },
                { label: 'Oil Absorption', value: 'Low' },
                { label: 'Particle Shape', value: 'Rhombohedral' },
                { label: 'Application', value: 'Sealants, Putty' }
            ]
        },
        paper: {
            title: 'Paper & Packaging Industry',
            description: 'Our paper-grade CaCO₃ provides brightness and opacity enhancement for both coated and uncoated paper. High whiteness and controlled particle distribution deliver superior print quality.',
            specs: [
                { label: 'Recommended Mesh', value: '2500 – 3500' },
                { label: 'Whiteness', value: '97%+' },
                { label: 'Brightness', value: '95%+' },
                { label: 'Application', value: 'Coating, Filling' }
            ]
        },
        construction: {
            title: 'Construction Industry',
            description: 'Calcium carbonate and limestone products are essential in cement, mortar, dry-mix products, and tile adhesives. Our range of grades supports diverse construction applications.',
            specs: [
                { label: 'Recommended Mesh', value: '200 – 800' },
                { label: 'CaCO₃ Content', value: '95%+' },
                { label: 'Form', value: 'Powder & Lumps' },
                { label: 'Application', value: 'Cement, Mortar' }
            ]
        }
    };

    document.querySelectorAll('.industry-card').forEach(card => {
        card.addEventListener('click', () => {
            const industry = card.dataset.industry;
            const data = window.industryData[industry];
            if (!data) return;

            modalTitle.textContent = data.title;
            modalDescription.textContent = data.description;
            modalIcon.innerHTML = card.querySelector('.industry-card__icon').innerHTML;
            modalSpecs.innerHTML = data.specs.map(spec =>
                `<div class="industry-modal__spec">
                    <div class="industry-modal__spec-label">${spec.label}</div>
                    <div class="industry-modal__spec-value">${spec.value}</div>
                </div>`
            ).join('');

            modal.classList.add('open');
            document.body.style.overflow = 'hidden';
        });
    });

    function closeModal() {
        modal.classList.remove('open');
        document.body.style.overflow = '';
    }

    if (modalClose) modalClose.addEventListener('click', closeModal);
    if (modalOverlay) modalOverlay.addEventListener('click', closeModal);

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeModal();
    });


    /* =========================================
       6. FLOATING PHONE WIDGET
       ========================================= */

    const phoneTrigger = document.getElementById('phone-trigger');
    const phonePopup = document.getElementById('phone-popup');

    if (phoneTrigger && phonePopup) {
        phoneTrigger.addEventListener('click', (e) => {
            e.stopPropagation();
            phonePopup.classList.toggle('open');
        });

        document.addEventListener('click', (e) => {
            if (!e.target.closest('.floating-phone')) {
                phonePopup.classList.remove('open');
            }
        });
    }


    /* =========================================
       7. SCROLL REVEAL ANIMATIONS
       ========================================= */

    const revealElements = document.querySelectorAll(
        '.about__image-frame, .about__content, .product-card, .news-card, .industries__header, .industry-card'
    );

    revealElements.forEach(el => el.classList.add('reveal'));

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                revealObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -40px 0px'
    });

    revealElements.forEach(el => revealObserver.observe(el));

    // Stagger product cards
    document.querySelectorAll('.product-card').forEach((card, i) => {
        card.style.transitionDelay = `${i * 0.1}s`;
    });

    // Stagger news cards
    document.querySelectorAll('.news-card').forEach((card, i) => {
        card.style.transitionDelay = `${i * 0.15}s`;
    });


    /* =========================================
       8. SMOOTH SCROLL & ACTIVE NAV
       ========================================= */

    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.navbar__link');

    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 150;
            if (window.scrollY >= sectionTop) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });

});
