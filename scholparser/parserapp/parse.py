import json

import bs4
import requests


from .parse_utils import get_keywords_handler

def get_keywords(url):

    res = requests.get(url)
    res.raise_for_status()
    html = res.text
    keywords = get_keywords_handler(html)


    return keywords