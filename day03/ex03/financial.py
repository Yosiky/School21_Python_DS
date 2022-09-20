from bs4 import BeautifulSoup
import time
import sys
import requests

def finance(ticket, field):
    name_file = 'webpage.html'
    urlToRead = 'https://finance.yahoo.com/quote/msft/financials?p=msft'
    page = requests.get(urlToRead, headers={'User-Agent': 'Custom'})
    if (page.status_code != 200):
        raise Exception("Site not work")
    page_parse = BeautifulSoup(page.text, 'html.parser')
    if page_parse.title.string == 'Symbol Lookup from Yahoo Finance':
        raise Exception('Wrong ticket')
    tags = page_parse.find_all(attrs={'data-test': 'fin-row'})
    rows = [tag.find(class_='Va(m)').get_text() for tag in tags]
    if field not in rows:
        raise Exception('Error with field')
    elems = tags[rows.index(field)].find_all('span')
    time.sleep(5)
    return tuple(elem.get_text() for elem in elems)

if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            raise Exception("Not valid count arguments")
        print(finance(sys.argv[1], sys.argv[2]))
    except Exception as some:
        print(some)
