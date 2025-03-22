from bs4 import BeautifulSoup
import pandas as pd

def scrape_leads_from_file(file_path):
    with open("C:/Users/Aasrith/OneDrive/Desktop/Leadgen_scraper/1.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    leads = []
    for lead in soup.find_all('div', class_='lead-info'):
        name = lead.find('h2').text.strip()
        email = lead.find('a', href=True)['href'].replace("mailto:", "")
        phone = lead.find('span', class_='phone').text.strip()
        leads.append({"Name": name, "Email": email, "Phone": phone})

    df = pd.DataFrame(leads)
    df.to_csv("leads.csv", index=False)
    print("Leads saved to leads.csv")

# Example usage
scrape_leads_from_file("C:/Users/Aasrith/OneDrive/Desktop/Leadgen_scraper/1.html")
