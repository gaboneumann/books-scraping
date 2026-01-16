# Simple web scraping project using Python 

This project is a beginner-friendly web scraping script built with Python.
It extracts book information from: https://books.toscrape.com/ for learning and practice purpose.

## Purpose
The purpose of this project is to understand the fundamentals of web scraping:
- Sending HTTP requests
- Parsing HTML content
- Extracting structured data using tags of HTML and CSS selectors

## Extracted data
- Title
- Price
- Stock availability
- Rating

## Technologies 
- Python
- Requests
- Beautifulsoup
- lxml

## How to run

### 1. Clone the repository
```bash
git clone https://github.com/gaboneumann/script_books.git
cd script_books

## 2. Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

## 3. Install dependencies

pip install -r requirements.txt

## 4. Run the scraper

python scraper.py