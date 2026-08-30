# About Us Page Specification & Layout Architecture 🏛️

This document details the exact layout structure, content sections, image assets, and interactive components implemented for the **Sababehpar Iranian Mining Company** About Us page (`sababehpar/about-us` route -> `about/index.html`).

---

## 📐 Page Structure & Section Breakdown

### 1. Header & Navigation Bar (Bilingual Support) 🌐
* **Utility Header**: Displays contact phone (`+98 21 8800 0000`), email (`info@sababehpar.com`), and an interactive language selector dropdown supporting **English (EN)**, **Farsi (FA)**, and **Arabic (AR)**.
* **Sticky Navbar**: Features the hexagonal Sababehpar brand logo, company title, mobile hamburger menu, and links to all primary pages (`Home`, `About Us`, `Products`, `Industries`, `News`, `Articles`, `Knowledge Center`, `Contact Us`).

---

### 2. Hero Section 🏞️
* **Background Asset**: High-resolution generated image (`assets/images/about_hero.jpg`) depicting the Aligoodarz white marble mining quarry and processing complex at golden hour.
* **Overlay & Typography**: Dark glassmorphic gradient overlay (`rgba(11,14,20,0.85)`), badge (`SABABEHPAR IRANIAN MINING CO.`), main headline (*"Pioneering Industrial Minerals & Powder Innovation"*), and introductory paragraph.

---

### 3. History & About Us Section 📜
* **Layout**: 2-Column Split Layout (`1fr 1fr`).
* **Left Column (5 Text Blocks)**:
  1. *Founding & Mining Rights (2010)*: Acquisition of mining extraction rights at Shaghez Aligoodarz marble quarry.
  2. *Vertical Integration Strategy*: Raw quarry block extraction, crushing, continuous ball mill micronizing, and automated packaging under one corporate umbrella.
  3. *Chemical Purity (99%+ CaCO3)*: Natural whiteness index exceeding 98.0% with minimal silica impurities.
  4. *Automated Micronizing & Coating*: 3 automated ball mill lines featuring continuous stearic acid coating units for polymer grades.
  5. *Scaled B2B Capacity (150,000+ Tons)*: Annual production capacity serving polymer, coating, dry-mix mortar, and paper industries.
* **Right Column (Generated Image)**:
  * Asset: `assets/images/about_history.jpg` displaying automated wire-saw extraction of white calcium carbonate blocks in Shaghez quarry.

---

### 4. Executive Management Team Section 👨‍💼
* **Layout**: 5 Cards in a Row (`repeat(auto-fit, minmax(200px, 1fr))`).
* **Card Details**: Each card includes an avatar icon, member name, executive role in the company, short bio, and direct LinkedIn / Email contact links:
  1. **Eng. M. Rezaei** — *Board Chairman & CEO* (Executive Leadership)
  2. **Dr. A. Ahmadi** — *Head of R&D & Quality* (Chief Chemical Engineer)
  3. **Eng. H. Ghasemi** — *Plant Operations Director* (Aligoodarz Facility Manager)
  4. **Eng. K. Hosseini** — *Mining & Exploration Lead* (Chief Geologist)
  5. **Ms. S. Karimi** — *International Sales Lead* (Export Director)
* **Section Footer**: A prominent **`Learn More About Executive Team →`** button linking to `about/management-team.html`.

---

### 5. Sustainability & ESG Section 🌿
* **Layout**: 2-Column Split Layout (`1fr 1fr`).
* **Left Column (5 Text Blocks)**:
  1. *Closed-Loop Water Recycling (95%+)*: Wash water clarifier filtration recycling 95%+ of water with zero chemical effluent discharge.
  2. *Energy Efficient Micronizing (22% Savings)*: Variable frequency drives on ball mill motors reducing electrical power per ton.
  3. *Progressive Quarry Land Restoration*: Wire-saw cutting eliminating blasting damage for topsoil revegetation.
  4. *Dust Containment & ISO 14001 Standards*: Enclosed pneumatic lines maintaining workplace dust emissions below 5 mg/m³.
  5. *UN SDG Alignment*: Corporate social responsibility roadmap aligned with UN SDGs 6, 7, 12, and 13.
* **Right Column (Generated Image)**:
  * Asset: `assets/images/about_sustainability.jpg` showcasing the eco-friendly green industrial complex with water recycling tanks and solar power installations.
* **5 Sustainability Report Cards**:
  1. 💧 **Water Recycling Report**: 95%+ closed-loop water recycling rate (`Sababehpar-Water-Report-2026.pdf`).
  2. ⚡ **Power Reduction Report**: 22% reduction in kWh per processed ton (`Sababehpar-Energy-Report-2026.pdf`).
  3. 🌿 **Zero Effluent Report**: Zero chemical discharge into local watersheds (`Sababehpar-Effluent-Report-2026.pdf`).
  4. 🏞️ **Land Restoration Report**: Progressive topsoil revegetation at Shaghez (`Sababehpar-Land-Report-2026.pdf`).
  5. 🌍 **UN SDG Audit Report**: Official UN SDG alignment audit certification (`Sababehpar-UN-SDG-Audit-2026.pdf`).

---

### 6. Corporate Footer 🏙️
* 4-column footer featuring company summary, quick navigation links, Knowledge Center links, and contact directory.
