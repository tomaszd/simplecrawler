import re
from sys import argv
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

script, website_address = argv


def get_all_links(url):
    domain = urlparse(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_links = list()
    get_slash = soup.find_all("a", href=re.compile("^/"))
    for tag in get_slash:
        all_links.append(domain.scheme + "://" + domain.netloc + tag['href'])
    all_tags = soup.find_all("a", href=re.compile(url))
    for tag in all_tags:
        all_links.append(tag['href'])
    return all_links


def get_site_title(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    find_title = soup.find_all("title")
    return find_title[0].string


def create_site_map(url):
    visited_websites = set()
    websites_to_visit = [url]
    site_map = dict()
    while websites_to_visit:
        single_site = websites_to_visit.pop(0)
        if single_site in visited_websites:
            continue
        else:
            print("Checking website: {}".format(single_site))
            links = get_all_links(single_site)
            websites_to_visit.extend(links)
            visited_websites.add(single_site)
            site_map[single_site] = {
                'title': get_site_title(single_site),
                'links': set(links)
            }
    return site_map


print(create_site_map(website_address))
