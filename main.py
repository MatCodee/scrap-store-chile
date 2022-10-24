from htmlparser import api_request
from scrap import scrap_falabella
from config import URLS

def start():
    for i in URLS: 
        result = api_request(i)
        scrap_falabella(result)


def main():
    start()

if __name__ == '__main__':
    main()
