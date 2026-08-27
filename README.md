# Real Estate Dashboard (Demo)

This repository contains sample CSV data and a static GitHub Pages demo for a Real Estate Advisor dashboard.

What I added

- data/
  - properties.csv (30 dummy properties)
  - deals.csv (12 dummy deals)
  - parties.csv (buyers/sellers/agents)
  - documents.csv
  - payments.csv
  - earnings_splits.csv
- index.html — static dashboard that loads the CSVs client-side using PapaParse and shows KPIs, a map (Leaflet), and simple tables.

How to view

1. GitHub Pages
   - To publish the dashboard, enable GitHub Pages for this repository: go to Settings → Pages and select the `main` branch (root) as the source. After a minute the site will be available at:
     `https://Vinxvins.github.io/ideas/`

2. Local testing
   - You can also open `index.html` locally, but some browsers block local Ajax requests. Run a simple local server instead:
     - Python 3: `python -m http.server 8000` then open `http://localhost:8000/`

Next steps I can do for you

- Improve the front-end (filters, charts, deal detail pane, document uploads).
- Add sample seed data in JSON or SQL if you want to load into a database.
- Wire up GitHub Actions to auto-publish Pages.

If you want, I can enable GitHub Pages for you (requires repo settings permission) or walk you through enabling it.
