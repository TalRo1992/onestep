import requests
from bs4 import BeautifulSoup
from models import CaseStudy, db

def scrape_case_studies():
    url = 'https://www.onestep.co/resources/case-studies'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    case_studies = []

    items = soup.find('div', class_='w-dyn-items')
    for item in items.find_all('div', class_='w-dyn-item'):
        title = item.find('h3', class_='heading-small').text.strip() 
        description = item.find('p', class_='main-paragraph description').text.strip()  
        date = item.find('div', class_='text-block').text.strip()
        link = item.find('a')['href'].strip()
       
        image_element = item.find('div', class_='wrapper-full-image').find('img')
        image_url = image_element['src'] if image_element else None
        case_studies.append({
            'title': title,
            'description': description,
            'date': date,
            'link': link,
            'image_url': image_url
        })

    return case_studies

def save_case_studies():
    case_studies = scrape_case_studies() 
    
    for cs in case_studies:
        case_study = CaseStudy(
            title=cs['title'],
            description=cs['description'],
            date=cs['date'],
            link=cs['link'],
            image_url=cs['image_url']
        )
        db.session.add(case_study)

    db.session.commit()
