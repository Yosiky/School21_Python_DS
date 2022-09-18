import sys

def find_price_company(arg):
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }
    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }
    arg = arg.strip()
    arg = arg[0].upper() + arg[1:].lower()
    if arg in COMPANIES:
        print(STOCKS[COMPANIES[arg]])
    else:
        print("Unknown company")

if __name__ == '__main__':
    count = len(sys.argv)
    if count == 2:
        find_price_company(sys.argv[1])

