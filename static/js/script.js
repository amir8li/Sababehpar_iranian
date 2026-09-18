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
        if (dots.length > 0) dots.forEach(d => d.classList.remove('active'));
        currentSlide = index;
        if (slides.length > 0) slides[currentSlide].classList.add('active');
        if (dots.length > 0) dots[currentSlide].classList.add('active');
    }

    function nextSlide() {
        if (slides.length > 0) goToSlide((currentSlide + 1) % slides.length);
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

    // Close mobile menu on link click, EXCEPT toggle links
    document.querySelectorAll('.navbar__mobile-link:not(.navbar__mobile-toggle), .navbar__mobile-sublink').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            mobileMenu.classList.remove('open');
        });
    });

    // Mobile dropdown toggle logic
    document.querySelectorAll('.navbar__mobile-toggle').forEach(toggle => {
        toggle.addEventListener('click', (e) => {
             // Prevent navigating to href="#"
            toggle.classList.toggle('open');
            const sublinks = toggle.nextElementSibling;
            if (sublinks && sublinks.classList.contains('navbar__mobile-sublinks')) {
                sublinks.classList.toggle('open');
            }
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
            document.getElementById("lang-toggle-text").textContent = option.dataset.lang === 'fa' ? ' FA ' : ' EN ';
            langDropdown.classList.remove('open');
            window.location.href = option.href;
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

    if (!window.industryData) {
        window.industryData = {
            en: {
                paint: {
                    title: 'Paint & Resin',
                    description: 'Micronized calcium carbonate powder is used as one of the most widely used mineral fillers in the production of various industrial paints, resins, and coatings. Having desirable whiteness and uniform granulation, it helps improve coverage, adjust viscosity, and create appropriate texture in the final product. Using the right grade of calcium carbonate can optimize formulation and reduce production costs while maintaining quality. This product is used in the production of architectural paints, industrial paints, primers, putties, and various water-based and solvent-based coatings. Selecting the right grade is based on whiteness, particle size, oil absorption, and dispersibility in the formulation.',
                    specs: []
                },
                plastics: {
                    title: 'Plastics & Polymers',
                    description: 'Micronized calcium carbonate powder is one of the most consumed mineral fillers in the plastics and polymer industries, used in producing a wide range of polymeric products. Its controlled granulation, low moisture, and good dispersibility contribute to blend uniformity and production process stability. Regular and coated calcium carbonate grades are selected based on the polymer type and formulation to improve processing properties and final product characteristics. It is applied in manufacturing masterbatches, polymer films, injection molded products, plastic parts, and polymer compounds. Grade selection considers particle size, surface coating, whiteness, and end-product requirements.',
                    specs: []
                },
                pvc: {
                    title: 'PVC, UPVC & Profiles',
                    description: 'Micronized calcium carbonate powder is an essential mineral in PVC and UPVC product formulations, widely used in manufacturing door and window profiles, wall panels, baseboards, flooring, and construction parts. The powder\'s granulation uniformity, suitable whiteness, and low moisture impact the product\'s visual quality, extrusion stability, and production consistency. Coated grades are utilized in many PVC formulations due to better dispersion in the polymer matrix. The appropriate grade is chosen based on product type, usage percentage, production speed, and expected mechanical and visual properties. Continuous powder quality control ensures stable production and reduces process fluctuations.',
                    specs: []
                },
                paper: {
                    title: 'Paper & Cardboard',
                    description: 'Micronized calcium carbonate powder is a highly utilized mineral filler in the paper and cardboard industry, used to produce various packaging and printing papers and boards. This material improves the product\'s whiteness, surface uniformity, and visual quality, thereby enhancing printability and final appearance. Controlling the powder\'s granulation, purity, and quality stability is crucial for achieving stable production and a uniform product. Calcium carbonate is used in filler applications as well as certain coating formulations. Grade selection depends on the production line type, paper/cardboard specifications, and consumer technical needs.',
                    specs: []
                },
                feed: {
                    title: 'Animal, Poultry & Aquatic Feed',
                    description: 'Micronized calcium carbonate powder is considered a rich source of calcium for meeting vital needs in the animal, poultry, and aquatic feed industry. This substance plays a key role in strengthening skeletal structure, improving eggshell quality in poultry, and regulating animal metabolism. High purity, the absence of heavy metal impurities, and precise granulation are significant features of this powder to ensure maximum absorption and final product health. Using a suitable grade with controlled particle size helps achieve uniform distribution in the formulation and increases feed production efficiency. This product fully complies with health and nutritional standards and is extensively used in producing various concentrates and supplements for livestock, poultry, and aquatic animals.',
                    specs: []
                },
                rubber: {
                    title: 'Rubber & Foam',
                    description: 'Micronized calcium carbonate powder acts as a key mineral filler in the rubber and foam industries, effectively improving physical properties and reducing production costs. Using this material in rubber product formulations not only increases hardness and elastic modulus but also improves processing characteristics and compound flowability during production. In producing various foams, this powder enhances product quality and durability by maintaining uniform cellular structure. Selecting the right grade with precise granulation and optimal oil absorption directly impacts the dimensional stability and abrasion resistance of the final products.',
                    specs: []
                },
                construction: {
                    title: 'Tiles, Ceramics & Construction',
                    description: 'Micronized calcium carbonate powder is widely used as an applied mineral in producing various tiles, ceramics, and construction materials. It effectively contributes to the formulations of ceramic bodies, dry mortars, tile adhesives, putties, polymer plasters, and construction coatings. The powder\'s uniform granulation and stable quality significantly help control the production process and enhance the final product\'s quality. Choosing the right grade based on required technical features and production line conditions ensures achieving the desired texture and physical resistance. Micronized calcium carbonate plays a fundamental role in optimizing construction and ceramic product formulations by providing excellent filling properties.',
                    specs: []
                }
            },
            fa: {
                paint: {
                    title: 'رنگ و رزین',
                    description: 'پودر میکرونیزه کربنات کلسیم به‌عنوان یکی از پرکننده‌های معدنی پرکاربرد در تولید انواع رنگ، رزین و پوشش‌های صنعتی استفاده می‌شود. این ماده با برخورداری از سفیدی مطلوب و دانه‌بندی یکنواخت، به بهبود پوشش‌دهی، تنظیم غلظت و ایجاد بافت مناسب در محصول نهایی کمک می‌کند. استفاده از گرید مناسب کربنات کلسیم می‌تواند ضمن حفظ کیفیت، باعث بهینه‌سازی فرمولاسیون و کاهش هزینه‌های تولید شود. این محصول در تولید رنگ‌های ساختمانی، رنگ‌های صنعتی، پرایمرها، بتونه‌ها و انواع پوشش‌های پایه آب و پایه حلال کاربرد دارد. انتخاب گرید مناسب بر اساس میزان سفیدی، اندازه ذرات، جذب روغن و قابلیت پراکنش در فرمولاسیون انجام می‌شود.',
                    specs: []
                },
                plastics: {
                    title: 'پلاستیک و پلیمر',
                    description: 'پودر میکرونیزه کربنات کلسیم یکی از پرکننده‌های معدنی پرمصرف در صنایع پلاستیک و پلیمر است و در تولید طیف گسترده‌ای از محصولات پلیمری به کار می‌رود. دانه‌بندی کنترل‌شده، رطوبت پایین و پراکنش‌پذیری مناسب این ماده، به یکنواختی ترکیب و پایداری فرآیند تولید کمک می‌کند. گریدهای معمولی و کوتد کربنات کلسیم، بسته به نوع پلیمر و فرمولاسیون، برای بهبود خواص فرآیندی و تنظیم ویژگی‌های محصول نهایی انتخاب می‌شوند. این محصول در تولید مستربچ، فیلم‌های پلیمری، محصولات تزریقی، قطعات پلاستیکی و کامپاندهای پلیمری کاربرد دارد. انتخاب گرید مناسب با توجه به اندازه ذرات، میزان پوشش‌دهی سطحی، سفیدی و الزامات محصول نهایی انجام می‌شود.',
                    specs: []
                },
                pvc: {
                    title: 'PVC، UPVC و پروفیل',
                    description: 'پودر میکرونیزه کربنات کلسیم یکی از مواد معدنی مهم در فرمولاسیون محصولات PVC و UPVC است و در تولید پروفیل‌های در و پنجره، دیوارپوش، قرنیز، کفپوش و قطعات ساختمانی کاربرد گسترده دارد. یکنواختی دانه‌بندی، سفیدی مناسب و رطوبت پایین پودر در کیفیت ظاهری محصول، پایداری فرآیند اکستروژن و یکنواختی تولید نقش دارد. گریدهای کوتد به‌دلیل پراکنش بهتر در ماتریس پلیمری، در بسیاری از فرمولاسیون‌های PVC مورد استفاده قرار می‌گیرند. انتخاب گرید مناسب با توجه به نوع محصول، درصد مصرف، سرعت تولید و ویژگی‌های مکانیکی و ظاهری مورد انتظار انجام می‌شود. کنترل مستمر کیفیت پودر، به تولید پایدار و کاهش نوسان در فرآیند کمک می‌کند.',
                    specs: []
                },
                paper: {
                    title: 'کاغذ و مقوا',
                    description: 'پودر میکرونیزه کربنات کلسیم یکی از پرکننده‌های معدنی پرکاربرد در صنعت کاغذ و مقوا است و در تولید انواع کاغذ و مقوای بسته‌بندی و چاپ استفاده می‌شود. این ماده می‌تواند به بهبود سفیدی، یکنواختی سطح و کیفیت ظاهری محصول کمک کند و در نتیجه قابلیت چاپ‌پذیری و جلوه نهایی را ارتقا دهد. کنترل دانه‌بندی، خلوص و ثبات کیفیت پودر، برای دستیابی به تولید پایدار و محصول یکنواخت اهمیت بالایی دارد. کربنات کلسیم می‌تواند در کاربردهای فیلر و همچنین برخی فرمولاسیون‌های کوتینگ مورد استفاده قرار گیرد. انتخاب گرید مناسب بر اساس نوع خط تولید، مشخصات کاغذ/مقوا و نیازهای فنی مصرف‌کننده انجام می‌شود.',
                    specs: []
                },
                feed: {
                    title: 'خوراک دام، طیور و آبزیان',
                    description: 'پودر میکرونیزه کربنات کلسیم یک منبع غنی از کلسیم برای تأمین نیازهای حیاتی در صنعت خوراک دام، طیور و آبزیان محسوب می‌شود. این ماده در تقویت استخوان‌بندی، بهبود کیفیت پوسته تخم‌مرغ در طیور و تنظیم سوخت‌وساز بدن دام نقش کلیدی ایفا می‌کند. خلوص بالا، عدم وجود ناخالصی‌های فلزات سنگین و دانه‌بندی دقیق، از ویژگی‌های حائز اهمیت این پودر برای اطمینان از جذب حداکثری و سلامت محصولات نهایی است. استفاده از گرید مناسب با اندازه ذرات کنترل‌شده، به توزیع یکنواخت در فرمولاسیون و افزایش راندمان تولید خوراک کمک می‌کند. این محصول با استانداردهای بهداشتی و تغذیه‌ای سازگاری کامل دارد و در تولید انواع کنسانتره‌ها و مکمل‌های دامی، طیور و آبزیان به شکل گسترده استفاده می‌شود.',
                    specs: []
                },
                rubber: {
                    title: 'صنایع لاستیک و فوم',
                    description: 'پودر میکرونیزه کربنات کلسیم به‌عنوان یک پرکننده معدنی کلیدی در صنایع لاستیک و فوم، نقش مؤثری در بهبود خواص فیزیکی و کاهش هزینه‌های تولید دارد. استفاده از این ماده در فرمولاسیون محصولات لاستیکی، علاوه بر افزایش سختی و مدول الاستیسیته، به بهبود ویژگی‌های پردازشی و جریان‌پذیری آمیزه در فرآیند تولید کمک می‌کند. در صنایع تولید انواع فوم، این پودر با حفظ یکنواختی سلولی و ساختار نهایی، کیفیت و دوام محصول را ارتقا می‌دهد. انتخاب گرید مناسب با دانه‌بندی دقیق و جذب روغن بهینه، تأثیر مستقیمی بر پایداری ابعادی و مقاومت سایشی محصولات نهایی خواهد داشت.',
                    specs: []
                },
                construction: {
                    title: 'کاشی، سرامیک و ساختمان',
                    description: 'پودر میکرونیزه کربنات کلسیم در تولید انواع کاشی، سرامیک و مصالح ساختمانی به‌عنوان یک ماده معدنی پرکاربرد استفاده می‌شود. این محصول در فرمولاسیون بدنه‌های سرامیکی، ملات‌های خشک، چسب کاشی، بتونه، گچ‌های پلیمری و پوشش‌های ساختمانی نقش مؤثری دارد. یکنواختی دانه‌بندی و کیفیت پایدار پودر، به کنترل بهتر فرآیند تولید و افزایش کیفیت محصول نهایی کمک شایانی می‌کند. انتخاب گرید مناسب با توجه به ویژگی‌های فنی مورد نیاز و شرایط خط تولید، دستیابی به بافت مطلوب و مقاومت فیزیکی مورد انتظار را تضمین می‌نماید. کربنات کلسیم میکرونیزه با ایجاد خواص پرکنندگی عالی، در بهینه‌سازی فرمولاسیون محصولات ساختمانی و سرامیکی نقش اساسی ایفا می‌کند.',
                    specs: []
                }
            }
        };
    }

    document.querySelectorAll('.industry-card').forEach(card => {
        card.addEventListener('click', () => {
            const industry = card.dataset.industry;
            const currentLang = localStorage.getItem('sababehpar-lang') || 'en';
            const langData = (window.industryData && window.industryData[currentLang]) 
                ? window.industryData[currentLang] 
                : (window.industryData && window.industryData.en ? window.industryData.en : window.industryData);
            const data = langData ? langData[industry] : null;
            if (!data) return;

            if (modalTitle) modalTitle.textContent = data.title;
            if (modalDescription) modalDescription.textContent = data.description;
            const iconEl = card.querySelector('.industry-card__icon');
            if (modalIcon) modalIcon.innerHTML = iconEl ? iconEl.innerHTML : '';
            if (modalSpecs) {
                modalSpecs.innerHTML = (data.specs || []).map(spec =>
                    `<div class="industry-modal__spec">
                        <div class="industry-modal__spec-label">${spec.label}</div>
                        <div class="industry-modal__spec-value">${spec.value}</div>
                    </div>`
                ).join('');
            }

            const modalCta = document.getElementById('modal-cta');
            if (modalCta) {
                if (currentLang === 'fa') {
                    modalCta.textContent = 'درخواست نمونه محصول';
                } else {
                    modalCta.textContent = 'Request Industry Sample';
                }
            }

            if (modal) {
                modal.dataset.activeIndustry = industry;
                modal.classList.add('open');
                document.body.style.overflow = 'hidden';
            }
        });
    });

    function closeModal() {
        if (modal) modal.classList.remove('open');
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
       8. SMOOTH SCROLL & ACTIVE NAV (HASH LINKS ONLY)
       ========================================= */

    const inPageSections = document.querySelectorAll('section[id]');
    const hashNavLinks = document.querySelectorAll('.navbar__link[href^="#"]');

    if (inPageSections.length > 0 && hashNavLinks.length > 0) {
        function updateActiveNav() {
            let current = '';
            inPageSections.forEach(section => {
                const sectionTop = section.offsetTop - 180;
                if (window.scrollY >= sectionTop) {
                    current = section.getAttribute('id');
                }
            });

            if (current) {
                hashNavLinks.forEach(link => {
                    if (link.getAttribute('href') === `#${current}`) {
                        link.classList.add('active');
                    } else {
                        link.classList.remove('active');
                    }
                });
            }
        }

        window.addEventListener('scroll', updateActiveNav);
        updateActiveNav();
    }


    /* =========================================
       9. EXECUTIVE TEAM POP-UP MODAL (ABOUT US PAGE)
       ========================================= */

    const teamCards = document.querySelectorAll('.about-team-grid .product-card');
    const teamModal = document.getElementById('team-modal');
    const teamModalClose = document.getElementById('team-modal-close');

    if (teamCards.length > 0 && teamModal) {
        teamCards.forEach((card, index) => {
            card.style.cursor = 'pointer';
            card.setAttribute('tabindex', '0');
            card.setAttribute('role', 'button');
            card.setAttribute('aria-label', `View details for manager ${index + 1}`);

            card.addEventListener('click', (e) => {
                // Prevent trigger if clicking directly on a mailto link
                if (e.target.tagName === 'A') return;

                const currentLang = localStorage.getItem('sababehpar-lang') || 'en';
                const pNameKey = `mgmt-p${index + 1}-name`;
                const pRoleKey = `mgmt-p${index + 1}-role`;
                const pBioKey = `mgmt-p${index + 1}-bio`;

                const dict = (typeof translations !== 'undefined' && translations[currentLang]) 
                    ? translations[currentLang] 
                    : (typeof translations !== 'undefined' ? translations['en'] : {});

                const imgEl = card.querySelector('img');
                const emailEl = card.querySelector('a[href^="mailto:"]');

                const nameVal = dict[pNameKey] || card.querySelector('h3').textContent;
                const roleVal = dict[pRoleKey] || card.querySelector('p[id$="-role"]').textContent;
                const bioVal = dict[pBioKey] || card.querySelector('p[id$="-desc"]').textContent;

                document.getElementById('team-modal-img').src = imgEl ? imgEl.src : '';
                document.getElementById('team-modal-img').alt = nameVal;
                document.getElementById('team-modal-name').textContent = nameVal;
                document.getElementById('team-modal-role').textContent = roleVal;
                document.getElementById('team-modal-bio').textContent = bioVal;

                if (emailEl) {
                    const modalEmailLink = document.getElementById('team-modal-email');
                    modalEmailLink.href = emailEl.href;
                    modalEmailLink.textContent = emailEl.href.replace('mailto:', '');
                }

                teamModal.style.display = 'flex';
                teamModal.setAttribute('aria-hidden', 'false');
                document.body.style.overflow = 'hidden';
            });

            card.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    
                    card.click();
                }
            });
        });

        function closeTeamModal() {
            teamModal.style.display = 'none';
            teamModal.setAttribute('aria-hidden', 'true');
            document.body.style.overflow = '';
        }

        if (teamModalClose) {
            teamModalClose.addEventListener('click', closeTeamModal);
        }

        teamModal.addEventListener('click', (e) => {
            if (e.target === teamModal) {
                closeTeamModal();
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && teamModal.style.display === 'flex') {
                closeTeamModal();
            }
        });
    }

});

