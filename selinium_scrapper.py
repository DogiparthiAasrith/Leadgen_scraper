from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def scrape_leads_dynamic(url):
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()  # No executable_path argument needed
    driver.get(url)

    leads = []
    elements = driver.find_elements(By.CLASS_NAME, "lead-info")

    for el in elements:
        name = el.find_element(By.TAG_NAME, "h2").text
        email = el.find_element(By.TAG_NAME, "a").get_attribute("href").replace("mailto:", "")
        phone = el.find_element(By.CLASS_NAME, "phone").text
        leads.append({"Name": name, "Email": email, "Phone": phone})

    df = pd.DataFrame(leads)
    df.to_csv("leads_dynamic.csv", index=False)
    print("Leads saved to leads_dynamic.csv")

    driver.quit()

# Example usage
scrape_leads_dynamic("C:/Users/Aasrith/OneDrive/Desktop/Leadgen_scraper/1.html")
