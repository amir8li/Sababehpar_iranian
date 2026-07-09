# Sababehpar Iranian Mining Company 🏭

A modern, high-performance, and fully responsive corporate website built for a leading B2B mineral processing and mining company. The site is designed with a premium, corporate aesthetic, featuring advanced micro-interactions, responsive grids, and full bilingual support (English & Farsi/RTL).

## 🚀 Technologies Used
Built with a lightweight stack for maximum speed, readability, and easy maintenance:
*   **HTML5** - Semantic structure and SEO-friendly markup.
*   **CSS3** - Custom styling, CSS Grid/Flexbox layouts, glassmorphism effects, and smooth animations (no external libraries like Tailwind or Bootstrap).
*   **Vanilla JavaScript (ES6)** - Lightweight DOM manipulation, custom carousels, animated statistics, and modal handling.

## 📁 Project Structure

```text
/
├── index.html            # Main entry point: Contains the layout structure, semantic tags, and SVG icons.
├── styles.css            # Stylesheet: Includes the design system, animations, media queries, and RTL support.
├── script.js             # Interactions: Logic for the hero slideshow, industry carousel, modal popups, and number counters.
├── lang.js               # Localization: Lightweight custom translation engine for EN/FA switching and dynamic DOM updates.
└── assets/               
    └── images/           # Industrial imagery (optimized).
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
- [ ] **Multi-Page Architecture:** Expand the single-page layout into individual routed pages (`/products`, `/news`, `/about`) for deeper SEO indexing.
- [ ] **Backend CMS (Django):** As proposed, integrate a Django backend to dynamically serve News Articles and update Product KPIs without modifying HTML.
- [ ] **Asset Minification:** Set up a simple build pipeline (e.g., Webpack or Vite) to minify CSS and JS files for final production deployment.

## 🛠️ How to Run
Since this is a static website, no build step or node environment is required for development.
Simply open `index.html` in your favorite browser, or serve it using a local live server (like VS Code Live Server).
