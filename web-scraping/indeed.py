import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

conn = sqlite3.connect('job.db')
c = conn.cursor()
#c.execute(''' CREATE TABLE jobs(title TEXT, company TEXT, salary TEXT, rating TEXT, summary TEXT, post_days TEXT)''')

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    url =f'https://in.indeed.com/jobs?q=python+developer&l=Pune,+Maharashtra&start={page}'
    r = requests.get(url,headers)
    soup = BeautifulSoup(r.content,'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a', class_='jobtitle turnstileLink').text.strip()
        company = item.find('span', class_='company').text.strip()
        try:
            salary = item.find('span', class_='salaryText').text.strip()
            rating = item.find('span', class_='ratingsContent').text.strip()
        except:
            salary = ''
            rating = ''
        summary = item.find('div', class_='summary').text.strip().replace('\n','')
        post_days = item.find('span', class_='date date-a11y').text.strip()

        job = {
            'title':title,
            'company': company,
            'salary':salary,
            'rating':rating,
            'summary':summary,
            'post_days':post_days,
        }
        joblist.append(job)
    return

joblist = []
for i in range(0, 20, 10):
    print(f'Getting page, {i}')
    c = extract(i)
    transform(c)

df = pd.DataFrame(joblist)

for row in df.itertuples():
    c.execute('''INSERT INTO jobs (title, company, salary, rating, summary, post_days) VALUES(?,?,?,?,?,?)''',
        print(row.title, row.company, row.salary, row.rating, row.summary, row.post_days)
    )
conn.commit()
print('Complete..')