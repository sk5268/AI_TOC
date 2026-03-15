# 🧭 AI Assistant TOC

> A browser extension that adds a beautiful, floating **Table of Contents** to your AI assistant conversations — so you never lose track of what you asked.

Supports **ChatGPT**, **Google Gemini**, **Perplexity AI**, **Claude**, and **Grok** — all with a single unified extension.

---

## ✨ Features

### 🌐 Multi-Platform Support
Works seamlessly across the most popular AI assistants:
| Platform | URL |
|---|---|
| ChatGPT | `chatgpt.com` |
| Google Gemini | `gemini.google.com` |
| Perplexity AI | `perplexity.ai` |
| Anthropic Claude | `claude.ai` |
| Grok (xAI) | `grok.com`|

---

### 📋 Live Table of Contents
- Automatically detects and lists **all your user queries** in the current conversation as clickable TOC entries.
- Each entry is **numbered** and **truncated** to a clean, readable length.
- Clicking an entry **smoothly scrolls** to that exact message in the conversation.
- The TOC **updates automatically** every 5 seconds (heartbeat polling) and also refreshes immediately when you submit a new prompt.

---

### ✏️ Inline Entry Renaming
Hover over any TOC entry to reveal a **edit icon**. Click it to rename that entry with a custom label:
- Press **Enter** to save the new name.
- Press **Escape** to cancel without saving.
- Click away (blur) to auto-save.
- Custom names are **persisted per-conversation** across page refreshes using `localStorage`.

---

### 🔍 Live Search / Filter
A built-in search bar lets you **filter TOC entries in real time** as you type:
- Matches are case-insensitive.
- Non-matching entries are hidden instantly.
- A **clear (×) button** appears when there is text in the search box to reset the filter with one click.

---

### 🖱️ Drag to Reposition
The entire TOC panel is **freely draggable** anywhere on the screen:
- Click and drag the header to move it.
- A 3-pixel movement threshold prevents accidental drags when clicking.
- The panel is kept within the **viewport bounds** at all times.
- Position is **saved to `localStorage`** and restored on the next page load.

---

### ↔️ Resizable Panel
Resize the TOC panel from any edge or corner using **8 resize handles** (N, S, E, W, NE, NW, SE, SW):
- Minimum size: **260 × 200 px**
- Maximum size: **800 × 90% of viewport height**
- Resizing from the left or top edge simultaneously repositions the panel to keep the opposite edge fixed.
- Size is **saved to `localStorage`** and restored on the next page load.

---

### 🔘 Collapsible to a Floating Button
Click the **toggle button** (chevron) in the TOC header to minimize the entire panel into a small floating circle:
- Collapses to a **32 × 32 px** circular button so it stays out of the way.
- Click the circle again to **expand** it back to full size, repositioning intelligently so the panel doesn't jump off-screen.
- On screens **≤ 1024 px wide**, the TOC starts collapsed by default.

---

### 💾 Persistent State
All user preferences are saved to `localStorage` per-platform and restored automatically:
| Saved State | Storage Key |
|---|---|
| TOC panel position | `{platform}-toc-position` |
| TOC panel size | `{platform}-toc-size` |
| Custom entry names | `{platform}-toc-custom-names` |

---

### 🎨 Glassmorphism UI
The TOC panel features a premium, modern **glassmorphism** design:
- **Frosted glass** background with `backdrop-filter: blur`.
- Vibrant **cyan-to-blue gradient** accent color (`#00f2fe` → `#4facfe`).
- Subtle **glowing node markers** on the connector timeline.
- Smooth hover effects with `translateX` slide and glow on list items.
- Custom **thin scrollbar** for the entry list.
- Fully **responsive** with a mobile breakpoint at 900 px.
- Hidden automatically when **printing**.

---

## 🛠️ Project Structure

```
AI_TOC/
├── code.js                 # Core extension logic (platform detection, TOC, drag, resize, search)
├── code.css                # Glassmorphism styles and all UI theming
├── chrome_manifest.json    # Manifest V3 for Chrome / Edge / Brave
├── firefox_manifest.json   # Manifest V2 for Firefox
├── icons/
│   ├── icon48.png
│   └── icon128.png
└── zip.py                  # Script to package chrome.zip and firefox.zip
```

---

## 📦 Loading the Extension

### Chrome / Edge / Brave
1. Go to `chrome://extensions` (or `edge://extensions`).
2. Enable **Developer Mode** (top-right toggle).
3. Click **Load unpacked** and select the project folder (where `chrome_manifest.json` is located).
   > **Note:** Temporarily rename `chrome_manifest.json` → `manifest.json` before loading, or load from the extracted `chrome.zip`.

### Firefox
1. Go to `about:debugging#/runtime/this-firefox`.
2. Click **Load Temporary Add-on**.
3. Select `firefox_manifest.json` (or the `manifest.json` inside the extracted `firefox.zip`).

---