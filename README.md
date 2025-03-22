# LeadGen Scraper Tool 🚀

A smart Lead Generation scraping tool designed to extract valuable business leads from websites dynamically. Built using Flask, Selenium, Pandas, and Python, it allows you to scrape leads, download them as a CSV, and view them directly on a clean UI.

### ✨ Features
> Dynamic scraping using Selenium (handles JavaScript-heavy pages)

> Clean, intuitive UI for URL input & lead display

> Download scraped data as CSV

> Displays leads in a tabular format post-scraping

>  Duplicate removal and email validation ready (optional future improvements)


### 🛠️ Tech Stack
- Python 3.x
- Flask
- Selenium
- Pandas
- HTML + CSS (UI)
- BeautifulSoup


### 📁 Folder Structure

```csharp
Leadgen-Scraper/
├── app.py                 # Flask application
├── selinium_scrapper.py   # Selenium scraper logic
├── templates/
│   └── index.html         # Frontend HTML
├── leads_dynamic.csv      # Scraped leads dataset
├── README.md              # Project instructions
├── requirements.txt       # Python dependencies
└── static/                # (Optional: for CSS or JS files)

