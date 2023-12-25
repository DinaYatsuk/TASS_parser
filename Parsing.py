from bs4 import BeautifulSoup
import time
import  requests


def processing_links(link):
    time.sleep(1)
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.find('h1', class_=['tass_pkg_title-xVUT1', 'news-header__title']).text
        lead = soup.find('div', class_=['news-header__lead', 'NewsHeader_lead__6Z9If']).text
        text = ''.join([p.text for p in soup.find_all('p')])
        tags = ', '.join([tag.text for tag in soup.find_all('a', class_="Tags_tag__tRSPs")])
        info = {"url": str(link), "title": str(title), "lead": str(lead),
                "text": str(text), "tags": str(tags)}
        return info
    except AttributeError as e:
        print(f"Error processing link {link}: {e}")
        return None
