import requests
from bs4 import BeautifulSoup

keyword = '파이썬'
url = f'https://search.incruit.com/list/search.asp?col=job&kw={keyword}'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

lis = soup.find_all('li', class_='c_col')

jobs = []

for li in lis:
    try:
        company = li.find('a', class_='cpname').text
        title = li.find('div', class_='cell_mid').find('a').text
        location = li.find('div', class_='cl_md').find_all('span')[0].text
        hyperlink = li.find('div', class_='cell_mid').find('a').get('href')

        job_data = {
            'company': company,
            'title': title,
            'location': location,
            'hyperlink': hyperlink
        }

        jobs.append(job_data)

    except AttributeError:
        pass

print(jobs)
print(len(jobs))