# Sababehpar Iranian Mining Company - Approved Homepage Structure

This document outlines the final approved structure and layout specifications for the homepage of **Sababehpar Iranian Mining Company** (شرکت معدنی صبابهپر ایرانیان) as presented to the board of directors.

---

## 🎨 Design Theme & Brand Colors

The website design utilizes a professional, modern corporate mining theme. The color palette consists of three primary tokens:
* ⬜ **White / Light Gray (`#FFFFFF` / `#F8F9FA`)**: Used for page backgrounds, clean content panels, and readable copy boxes.
* 🟦 **Dark Blue / Navy (`#0B0E14` / `#121620`)**: Represents stability and depth. Used for section titles, headers, footers, card backgrounds, and main brand blocks.
* 🟧 **Light Orange / Gold (`#D4AF37` / `#E5A93B`)**: Represents industrial premium quality and mineral extraction. Used for navigation buttons, active links, KPIs, hover borders, and visual callouts.

---

## 📐 Section-by-Section Homepage Structure

### 1. Sticky Navigation Bar & Header
The header is pinned to the top of the viewport (`position: sticky; top: 0; z-index: 1000`) and consists of two sub-bars:
* **Top Utility Header (Dark Blue)**:
  * **Contact Details**: Pinned phone number (`+98 21 8800 0000`) and official email address (`info@sababehpar.com`).
  * **Social Media Links**: Clickable icons linking to official channels (**LinkedIn, Instagram, Telegram**) and local messengers (**Eitaa, Bale**).
  * **Trilingual Language Selector**: Switches the entire website DOM dynamically between **Farsi (فارسی)**, **English (EN)**, and **Arabic (العربية)**.
* **Main Navigation Bar (White Background / Blur Effect)**:
  * **Brand Identity**: logo icon (gem/quarry marker) and company title.
  * **Navigation Links**: Home, About Us, Products, Industries, News, Knowledge Center.
  * **Contact Us CTA**: Styled as a high-contrast **light orange button** with dark text (`#121620`), standing out from the rest of the inline menu.

---

### 2. Hero Section (Slideshow)
A fullscreen visual introduction containing:
* **Slideshow Cycler**: A fading image slideshow cycling through high-quality photos of geological mining quarries, lab test environments, and product bagging lines.
* **Animated Typography Overlay**: Bold headlines and descriptive paragraphs that fade in.
* **CTA Button**: A gold outline button linking to the company overview.

---

### 3. About Us Summary Section
A split two-column section bridging the brand story:
* **Visual Frame**: High-resolution image of the Aligoodarz production facility.
* **Narrative Copy**: Summary of history, mission, and the commitment to high-purity mineral powders.
* **Action CTA**: A clean text link (`Learn More` / `بیشتر بخوانید`) directing users to the full About Us page.
* **Key Stats Counters**: Integrated statistics details displaying:
  * **Workers / Staff**: `120+` professionals.
  * **Production Lines**: `3` fully automated packaging and processing lines.
  * **Annual Capacity**: `150,000+ Tons` of micronized powder.

---

### 4. Featured Products (5 Grades Grid)
Displays the exact 5 core products manufactured by Sababehpar Iranian:
1. **Stearic Coated Calcium Carbonate (GCC Coated)**
2. **Micronized Talc Powder (Industrial & Cosmetic)**
3. **Ultra-Fine Calcium Carbonate (GCC Uncoated)**
4. **Paper-Grade Calcium Carbonate Filler**
5. **Paint & Coating White CaCO3 Filler**

* **Interactive Grid Layout**: Structured as a 5-card grid with:
  * **KPI Badges**: Display of quality indices on each card (e.g. `98.5% CaCO3 Purity`, `96% Whiteness Index`, `D50 particle sizes`).
  * **Micro-Animations**: Smooth cards elevate, scale up (`scale(1.03)`), and glow with an orange/gold border highlight upon mouse hover.
  * **Contact CTA**: Individual link buttons directing to `/contact` pre-populated with the selected product category.

---

### 5. News & Articles Cards
A grid-based section displaying company announcements and research:
* **Card Layout**: Each card contains:
  * **Image Thumbnail**: Visual representing the news/article.
  * **Meta Info**: Publication date and category tag (News vs. Technical Papers).
  * **Headline**: Bold title.
  * **Excerpt**: Short text summary.
  * **Individual CTA**: A bottom-aligned action button (`Read Article` / `Download PDF`) for every card.

---

### 6. Served Industries (3D Carousel Slider)
Highlights the primary sectors served by Sababehpar products (Plastics, Paint & Coatings, Adhesive & Mastic, Paper, Construction):
* **3D Slider Layout**: An interactive carousel track that displays 5 industry cards side-by-side.
* **Navigation Buttons**: Left and Right arrows to slide and rotate cards horizontally.
* **Popup Modals**: Clicking an industry card opens an overlay modal showing detailed application briefs, recommended mesh sizes, and physical raw attributes.

---

### 7. Shared Footer
A deep dark blue footer providing structural anchors:
* **Brand Summary**: Company logo, title, and a brief profile.
* **Products Links**: Quick links to the 5 manufactured grades.
* **Contact Details**: Addresses for the Tehran sales office and Aligoodarz processing plant, phone lines, email addresses, and social icons.

---

### 8. Floating Sticky Phone Widget
Pushed to the **bottom-left** of the display across all pages to ensure constant visibility:
* **CSS properties**: `position: fixed; bottom: 2rem; left: 2rem; z-index: 1000;`
* **Trigger Button**: A floating circular button with a phone icon.
* **Expandable Chatbox**: Clicking the trigger expands a glassmorphic popup box listing quick telephone lines (Office & Factory) and messaging buttons (WhatsApp, Telegram, Eitaa, Bale) for rapid mobile access.
