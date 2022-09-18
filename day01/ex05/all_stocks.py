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
        return STOCKS[COMPANIES[arg]]
    else:
        return None

def find_company_stocks(arg):
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
    arg = arg.strip().upper()
    LIST = list(COMPANIES.values())
    if arg in LIST:
        indx = LIST.index(arg)
        return list(COMPANIES.keys())[indx], STOCKS[arg]
    else:
        return None

if __name__ == '__main__':
    count = len(sys.argv)
    if count == 2:
        parse_line = list(map(lambda x: x.strip(), sys.argv[1].split(',')))
        flag = 0
        for i in parse_line:
            if len(i) == 0:
                flag = 1
                break
        if not flag:
            for i in parse_line:
                res = find_price_company(i)
                if res == None:
                    res = find_company_stocks(i)
                    if res == None:
                        print(f"{i} is an unknown company or an unknown ticker symbol")
                    else:
                        print(f"{i} is a ticker symbol for {res[0]}")
                else:
                    print(f"{i} stock price is {res}")
        else:
            print()


