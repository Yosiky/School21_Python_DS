import os

if __name__ == "__main__":
    try:
        if os.environ.get('VIRTUAL_ENV') is None:
            raise Exception("Not virtual env PATH")
        os.system("pip3 install beautifulsoup4 pytest")
        os.system("pip3 freeze")
        os.system("pip3 freeze > requirements.txt")
    except Exception as some:
        print(some)

