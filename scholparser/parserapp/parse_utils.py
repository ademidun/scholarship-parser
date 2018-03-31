import re

import bs4
import dateutil.parser as dparser

from .constants import SCHOOLS, PROGRAMS, COUNTRIES


def get_keywords_handler(html):
    keywords = {}

    keywords = get_title(html, keywords)
    keywords = get_deadline(html, keywords)
    keywords = get_programs(html, keywords)
    keywords = get_schools(html, keywords)
    keywords = get_locations(html, keywords)
    keywords = get_misc_keywords(html, keywords)

    return keywords


def get_title(html, keywords):
    soup = bs4.BeautifulSoup(html, "html.parser")

    for item in soup.find_all('h1'):
        keywords['title'] = item.text
        break

    return keywords


def get_deadline(html, keywords):
    soup = bs4.BeautifulSoup(html, "html.parser")

    deadlines = []
    for item in soup.find_all('li'):
        try:
            deadline = dparser.parse(item.text, fuzzy=True)
            deadlines.append(deadline.isoformat())
            print('item,item.text', item, item.text)
        except Exception as e:
            # print('exception', e)
            # print('traceback', traceback.format_exc())
            pass

    keywords['deadline'] = deadlines

    return keywords


def get_misc_keywords(html, keywords):
    if any(['female' in html.lower() or 'women' in html.lower() or 'woman' in html.lower()]):
        keywords['female_only'] = True

    if 'international student' in html.lower():
        keywords['international_student_eligible'] = True

    soup = bs4.BeautifulSoup(html, "html.parser")

    images = []
    for item in soup.find_all('img'):
        images.append(item['src'])
        break

    img_regex = r"\(.+\)"
    for div in [div for div in soup.find_all("div") if 'style' in div.attrs]:
        if 'background-image' in div.attrs['style']:
            test_str = div.attrs['style']
            image_match = re.search(img_regex, test_str)
            image_match = image_match.group(0)
            image_match = image_match[1:-1]  # remove starting
            images.append(image_match)

    keywords['images'] = images

    return keywords


def get_schools(html, keywords):
    schools = []

    for school in SCHOOLS:
        if school.lower() in html.lower():
            schools.append(school)

    keywords['schools'] = schools
    return keywords


def get_programs(html, keywords):
    programs = []

    for program in PROGRAMS:
        if program.lower() in html.lower():
            programs.append(program)

    keywords['programs'] = programs
    return keywords


def get_locations(html, keywords):
    countries = []

    for country in COUNTRIES:
        if country.lower() in html.lower():
            countries.append(country)

    keywords['country'] = countries

    return keywords
