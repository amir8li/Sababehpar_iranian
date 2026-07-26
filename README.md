# Sababehpar Iranian Mining Company 🏭

A modern, high-performance, and fully responsive corporate website built for a leading B2B mineral processing and mining company. The site is designed with a premium, corporate aesthetic, featuring advanced micro-interactions, responsive grids, and full bilingual support (English & Farsi/RTL).

## 🚀 Technologies Used
Built with a lightweight stack for maximum speed, readability, and easy maintenance:
*   **HTML5** - Semantic structure and SEO-friendly markup.
*   **CSS3** - Custom styling, CSS Grid/Flexbox layouts, glassmorphism effects, and smooth animations (no external libraries like Tailwind or Bootstrap).
*   **Vanilla JavaScript (ES6)** - Lightweight DOM manipulation, custom carousels, animated statistics, and modal handling.

## 📁 Project Structure & Multi-Page Foldering

```text
Sababehpar-Website/
├── index.html                           # Main entry point (Homepage Landing)
├── styles.css                           # Stylesheet: Design system, multi-color dark theme, RTL support
├── script.js                           # Vanilla JS: Navigation, hero slideshow, 3D carousel, counters, modals
├── lang.js                             # Localization Engine: Lightweight EN, FA, AR translation dictionary
├── assets/                             # Optimized industrial imagery & media
├── about/
│   ├── index.html                      # About Us (/about)
│   ├── management-team.html            # Executive Management Team (/about/management-team)
│   └── sustainability.html             # Sustainability & ESG Initiatives (/about/sustainability)
├── products/
│   ├── index.html                      # Products Catalog (/products)
│   ├── calcium-carbonate.html          # GCC Product Group Details (/products/calcium-carbonate)
│   └── talc.html                       # Talc Product Group Details (/products/talc)
├── industries/
│   └── index.html                      # Industries Served (/industries)
├── news/
│   └── index.html                      # News & Press Releases (/news)
├── articles/
│   └── index.html                      # Technical Articles & Whitepapers (/articles)
├── knowledge-center/
│   ├── index.html                      # Knowledge Center Hub (/knowledge-center)
│   ├── quality-control.html            # Quality Control Protocols (/knowledge-center/quality-control)
│   ├── labs.html                       # R&D Laboratories (/knowledge-center/labs)
│   └── certifications.html             # ISO Certifications & MSDS (/knowledge-center/certifications)
└── contact/
    └── index.html                      # Contact Us & Inquiry Directory (/contact)
```

## 🗺️ Sitemap Tree Architecture

Based on **`Sababehpar_Sitemap.pdf`**, the website follows a clean multi-page hierarchy:

```text
Sababehpar Sitemap Tree
├── HOME (/)
│   ├── Navbar (fixed)
│   ├── Hero Presentation Section
│   ├── Short About Us & Key Stats Banner
│   ├── Key Mineral Properties
│   ├── Products Showcase
│   ├── Key Stats
│   ├── News Slideshow
│   ├── Industries Slideshow
│   └── Footer
├── ABOUT US (/about)
│   ├── History of Company & 15-Year Growth Roadmap
│   ├── Management Team (/about/management-team) -> Team profiles and bios
│   ├── Sustainability (/about/sustainability) -> ESG initiatives, UN SDGs & water recycling
│   └── Key Stats & Properties Summary
├── PRODUCTS (/products)
│   ├── Calcium Carbonate (/products/calcium-carbonate) -> GCC specs, sieve analysis, TDS/COA PDF downloads
│   └── Talc (/products/talc) -> Industrial Talc specs, sieve analysis, TDS/COA PDF downloads
├── INDUSTRIES (/industries)
│   └── Industry Application Cards (Paint, Plastics, Mortar, Paper, Adhesives, Rubber) + Pop-up Modals
├── NEWS (/news)
│   └── Company News & R&D Expansion News
├── ARTICLES (/articles)
│   └── Technical Whitepapers & Research Guides with PDF Downloads
├── KNOWLEDGE CENTER (/knowledge-center)
│   ├── Quality Control (/knowledge-center/quality-control) -> 4-Step QC batch release workflow
│   ├── Labs (/knowledge-center/labs) -> Testing equipment (XRF, Malvern Laser PSD, Spectrophotometer)
│   └── Certifications (/knowledge-center/certifications) -> ISO 9001, 14001, 45001 certificates
└── CONTACT US (/contact)
    ├── Tehran Sales Office & Aligoodarz Plant Directories
    ├── Fast Quote & Sample Request Form
    └── Factory Tour Booking Widget
```

## 🏗️ Architectural Layers

1.  **Sticky Utility & Navigation Layer**
    *   Top bar with contact information and language switcher.
    *   Main navigation bar with scroll-blur (glassmorphism) and mobile hamburger menu.
2.  **Hero Presentation Layer**
    *   3-slide background fading carousel.
    *   Dynamic typography with staggered reveal animations.
3.  **About & Statistics Layer**
    *   Animated number counters (`IntersectionObserver` driven) that automatically switch between English and Farsi numeral systems.
4.  **Product Showcase Layer**
    *   Responsive CSS Grid displaying core mineral products with technical KPIs (Purity, Whiteness, D50 Size).
5.  **Interactive Industries Layer**
    *   Custom-built drag/click horizontal slider for industries.
    *   Dynamic modal generation: Injecting specific technical data based on user clicks.
6.  **Localization Layer (`lang.js`)**
    *   A custom dictionary-based translation script that injects translations into the DOM based on CSS selectors.
    *   Automatically flips the layout direction (`dir="rtl"`) and adjusts Flexbox alignment, specific font-families (Vazirmatn), and SVG arrow orientations for Farsi mode.

## 📋 To-Do List (Future Improvements)

- [ ] **Contact Form API Integration:** Connect the "Request Quote" buttons and floating phone widget to a backend mailer (e.g., Formspree or custom backend).
- [ ] **Arabic Language Support:** Add the Arabic translation dictionary to `lang.js` and map the appropriate selectors.
- [x] **Multi-Page Architecture:** Expand the single-page layout into individual routed pages (`/products`, `/news`, `/about`, `/knowledge-center`, etc.) for deeper SEO indexing.
- [ ] **Backend CMS (Django):** As proposed, integrate a Django backend to dynamically serve News Articles and update Product KPIs without modifying HTML.
- [ ] **Asset Minification:** Set up a simple build pipeline (e.g., Webpack or Vite) to minify CSS and JS files for final production deployment.

## 🛠️ How to Run
Since this is a static website, no build step or node environment is required for development.
Simply open `index.html` in your favorite browser, or serve it using a local live server (like VS Code Live Server).
