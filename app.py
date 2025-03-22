from flask import Flask, render_template, request, send_file
import pandas as pd
from selinium_scrapper import scrape_leads_dynamic  # Import the correct function

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scrape", methods=["POST"])
def scrape():
    url = request.form["url"]  # Get URL from the form
    scrape_leads_dynamic(url)  # Call the Selenium scraper function

    # Send the CSV file for download after scraping is done
    return send_file("leads_dynamic.csv", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)