import requests
from bs4 import BeautifulSoup

def search_incruit(keyword):
    
    pages = 1
    jobs = []

    for page in range(pages):
        i = page * 30

        url = f'https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={i}'

        r = requests.get(url, timeout=10)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, 'html.parser')

        lis = soup.find_all('li', class_='c_col')

        print(f'{page+1} 페이지 크롤링 중')

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

    return jobs