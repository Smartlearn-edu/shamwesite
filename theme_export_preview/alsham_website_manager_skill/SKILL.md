---
name: Al-Sham Website Manager
description: Skill for managing, modifying, and updating the Al-Sham Center landing page (HTML/Tailwind).
author: Antigravity
---

# Al-Sham Website Manager Skill

Welcome to the Al-Sham Website Manager skill. This instruction set is designed to help Antigravity manage the static HTML/Tailwind landing page for the Al-Sham Center for Culture and Education.

## 🎯 Architecture Overview
This is a static web application using standard HTML, Javascript (`app.js`), and Tailwind CSS.
- **`index.html`**: The main landing page.
- **`plans.html`**: The packages and pricing page.
- **`style.css`**: Contains custom UI overrides (Glassmorphism, Neon Shadows, Animations).
- **`input.css` & `tailwind-output.css`**: Tailwind directives and compiled output.
- **`app.js`**: Contains interactive logic, translation state, and Moodle integration logic.

## 🛠️ Environment & Build Process
Whenever you (Antigravity) are asked to modify colors, spacing, or add new tailwind classes, you **MUST** rebuild the CSS.
To compile the Tailwind CSS, run the following command in the project root:
```bash
npx tailwindcss -i ./input.css -o ./tailwind-output.css
```
*(Make sure Node.js is installed on the machine).*

## 📝 Common Modification Workflows

### 1. Updating Plans & Pricing (in `plans.html`)
The plans are located in the `<!-- PLANS SECTION -->` of `plans.html`.
- **Pricing**: Look for the `<span class="text-4xl font-extrabold text-white">25</span>` tags.
- **WhatsApp Links**: The CTA buttons use URL-encoded Arabic text. If the user asks to change the WhatsApp number or the message, remember to URL-encode the Arabic string before updating the `href` attribute. For example: `https://wa.me/491578303030?text=%D8%A7%D9%84%D8%B3%D9%84...`
- **Backgrounds & Glows**: Controlled by custom classes in `style.css` (`.plan-card-teal`, `.plan-card-amber`, `.plan-card-indigo`). Do NOT change the Tailwind shadow arbitrarily for these cards without checking `style.css`.

### 2. Modifying Text & Translations
The site uses a simple data attribute translation system.
- Static HTML elements use `data-i18n="key"` (e.g., `<h1 data-i18n="siteTitle">...</h1>`).
- To change text permanently across languages, you must update the translation dictionary inside `app.js` (look for the `translations` object containing `ar`, `en`, and `de` keys).
- If you add new text to the HTML, always add it to the dictionary in `app.js` and assign a `data-i18n` attribute so the language switcher works seamlessly.

### 3. Adding New Courses / Categories
The dynamic course grid in `index.html` is populated via Javascript.
- To modify the displayed courses or categories, check the data arrays inside `app.js`.
- The category filters use `data-category="key"`. If adding a new filter, ensure the HTML button matches the Javascript filtering logic.

## ⚠️ Strict Rules & Best Practices
1. **Never break the Glassmorphism**: The UI relies heavily on `.glass-panel` and `.glass-navbar`. Ensure any new containers use these classes.
2. **RTL First**: The default layout is Arabic (RTL). When adding absolute positioning or padding, use logical properties (`ltr:`, `rtl:`, `start`, `end`) or ensure it looks correct in `dir="rtl"`.
3. **No Database**: This is a static site. Do not attempt to write PHP or SQL unless explicitly instructed to migrate the architecture.
4. **Cache Busting**: If you heavily modify `style.css` or `app.js`, increment the version string in the HTML `<link>` or `<script>` tags (e.g., `?v=8`) to force clients to clear their cache.

## 🚀 Getting Started
When the user asks you to make changes:
1. Locate the HTML, CSS, or JS file in the project folder.
2. Make the edits strictly adhering to the Glassmorphism UI.
3. Inform the user what was changed.
