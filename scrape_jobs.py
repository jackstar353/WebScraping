import pip._vendor.requests as requests

from bs4 import BeautifulSoup

import pandas as pd


def extract(page):
    #google 'my user agent' and copy the string into headers variable
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
    #paste whatever url of the website you want to scrape
    url=f'https://ie.indeed.com/jobs?q=python%20Developer&l=Ireland&vjk={page}'
    response =requests.get(url, headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ ='job_seen_beacon')
    for item in divs:
        title = item.find('h2').text.strip()
        company = item.find('span', class_ ='companyName').text.strip()
        companyLocation =item.find('div',class_='companyLocation').text.strip()
        try:
            companySalary=item.find('div', class_='metadata salary-snippet-container').text.strip()
        except:
            companySalary =''
        summary = item.find('div',class_='job-snippet').text.strip().replace('\n','')

        jobResults ={
            'title': title,
            'company': company,
            'Location':companyLocation,
            'salary': companySalary,
            'summary':summary
        }
        joblist.append(jobResults)
    return

    #return len(divs)
joblist=[]

for i in range(0,40,10):
    print(f'Getting page, {i}')
    c = extract(0)
    transform(c)
    #print(len(joblist))

df=pd.DataFrame(joblist)
print(df.head())
df.to_csv('pythonjobs.csv',encoding='utf-8')
