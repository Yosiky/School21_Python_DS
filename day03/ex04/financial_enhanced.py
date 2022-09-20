from bs4 import BeautifulSoup
import sys
from urllib.request import urlopen, Request

def finance(ticket, field):
    name_file = 'webpage.html'
    urlToRead = 'https://finance.yahoo.com/quote/msft/financials?p=msft'
    page = urlopen(Request(urlToRead, headers={'User-Agent': 'Mozilla/5.0'})).read()
    page_parse = BeautifulSoup(page, 'html.parser')
    if page_parse.title.string == 'Symbol Lookup from Yahoo Finance':
        raise Exception('Wrong ticket')
    tags = page_parse.find_all(attrs={'data-test': 'fin-row'})
    rows = [tag.find(class_='Va(m)').get_text() for tag in tags]
    if field not in rows:
        raise Exception('Error with field')
    elems = tags[rows.index(field)].find_all('span')
    return tuple(elem.get_text() for elem in elems)

if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            raise Exception("Not valid count arguments")
        print(finance(sys.argv[1], sys.argv[2]))
    except Exception as some:
        print(some)
