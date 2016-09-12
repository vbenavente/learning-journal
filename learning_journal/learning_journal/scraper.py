import requests
from bs4 import BeautifulSoup


ENTRY_DOMAIN = "https://sea401d4.crisewing.com"
ENTRY_PATH = "/entry"
ENTRY_NUMBER = ""


def get_entry_page(entry_number):
    url = ENTRY_DOMAIN + ENTRY_PATH
    params = entry_number
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.content, response.encoding


def parse_source(html, encoding='utf-8'):
    parsed = BeautifulSoup(html, 'html5lib', from_encoding=encoding)
    return parsed
