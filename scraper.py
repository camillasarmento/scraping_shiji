import re
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup
import csv

@dataclass
class Item:
    section: str
    address: str
    name: str

response = requests.get('https://reviewpro.shijigroup.com/team')
soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

def scrape_contacts_customer_support_section():
    section_title = 'Customer Support'
    result = []

    section_h3 = soup.find('h3', string=section_title, recursive=True)
    team_title_div = section_h3.next_sibling.next_element
    team_title = team_title_div.get_text(strip= True).replace('Contact our ', '')

    section_div = section_h3.find_parent('div')
    section_links = section_div.find_all('a', href=re.compile('mailto'))

    # get all contacts from section
    for link in section_links:
        email = link['href'].replace('mailto:', '')

        def get_zone():
            link_prev_sibling = link.find_previous_sibling()

            # 'Australia & New Zealand' is not like the others...
            if link_prev_sibling is not None:
                return link_prev_sibling.get_text(strip= True)

            div_link = link.parent
            div_zone = div_link.find_previous_sibling()

            return div_zone.get_text(strip= True)

        team = f"{team_title} - {get_zone()}"

        result.append(Item(section=section_title, address=email, name=team))

    return result

def scrape_contact_section(section_title):
    result = []

    section_h3 = soup.find('h3', string=section_title, recursive=True)
    team_title_div = section_h3.next_sibling.next_element
    team_title = team_title_div.get_text(strip= True).replace('Contact our ', '')
    section_div = section_h3.find_parent('div')
    section_link = section_div.find('a', href= re.compile('mailto'))

    # get contact from section
    email = section_link.text.strip()
    result.append(Item(section = section_title, address= email, name= team_title))

    return result
    
def scrape_products_section(title):
    result = []

    blue_title_div = soup.find('div', string= title, attrs= {'class': 'text-color-blue'}, recursive= True)
    section_div = blue_title_div.parent.parent

    links = section_div.find_all('a')

    # get all products from section
    for link in links:
        url = link['href']
        name = link.text.strip()
        result.append(Item(section= title, address= url, name= name))

    return result

def scrape_contacts():
    contacts = []

    # get all customer support contacts
    contacts.extend(scrape_contacts_customer_support_section())

    # get sales inquiries contact
    contacts.extend(scrape_contact_section('Sales Inquiries'))

    # get partnership opportunities contact
    contacts.extend(scrape_contact_section('Partnership Opportunities'))

    # get press contact
    contacts.extend(scrape_contact_section('Press'))

    # get billing issues contact
    contacts.extend(scrape_contact_section('Billing Issues'))

    return contacts

def scrape_products():
    products = []

    # get all "regular" products:
    products.extend(scrape_products_section('Products'))

    # get all "essential" products:
    products.extend(scrape_products_section('Essentials'))

    return products

def save_to_csv(items, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Section', 'Address', 'Name'])

        for item in items:
            writer.writerow([item.section, item.address, item.name])

    print(f"Data successfully saved to '{filename}'.")

print(f"Scraping site...")

data = scrape_contacts()
data.extend(scrape_products())

save_to_csv(data, 'data.csv')
