import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def get_url (position, location):
    ''' Generate a url from position and location'''
    template = 'https://in.indeed.com/jobs?q={}&l={}'
    url = template.format(position, location)
    return url

def get_records(cards):
    """ Extract job data from a single record """
    atag = cards.h2.a
    job_title = atag.get('title')
    job_url = 'https://www.indeed.com' + atag.get('href')
    company = cards.find('span','company').text.strip()
    job_location = cards.find('div', 'recJobLoc').get('data-rc-loc')
    job_summary = cards.find('div', 'summary').text.strip()
    post_date = cards.find('span', 'date').text
    today = datetime.today().strftime('%Y-%m-%d')
    try:
        job_salary = cards.find('span', 'salaryText').text.strip()
    except AttributeError:
        job_salary = ''

    record = (job_title, job_url, company, job_location, job_summary, post_date, today, job_salary)

    return record

def main (position, location):
    """ Run the main program routine """
    record_list = []
    url = get_url(position, location)

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        cards = soup.find_all('div', class_ = 'jobsearch-SerpJobCard')

        for card in cards:
            item = get_records(card)
            record_list.append(item) 

        try:
            url = 'https://www.indeed.com' + soup.find('a', {'aria-label': 'Next'}).get('href')
        except AttributeError:
            break
        
        print(len(record_list))

        #save the job data
        # with open('results.csv', 'w', newline='', encoding='utf-8') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(['job_title', 'job_url', 'company', 'job_location', 'job_summary', 'post_date', 'today', 'job_salary'])
        #     writer.writerows(record_list)

#run the main function
main('python developer', 'india')
