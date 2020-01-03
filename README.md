# Web Crawler

A Web Crawler - Internet bot which helps in Web indexing.

### Summary

It crawls one page at a time through a website until all pages have been indexed and creates a map of the domain he is on. The mapping contain all the accessible pages within that domain.
Web Crawler helps in collecting information about a website and the links related to them, and also helps in validating the HTML code and hyperlinks. Web Crawler is also known as a Web Spider, automatic indexer or simply crawler.

### Requirements

- Python 3.6.4
- BeautifulSoup 4
- requests library

### Status

Small script ready to use.

### Usage

As mentioned, it is a ready-to-run script. You only need to download it and put the web url that you want to start crawling from in a place of `website_address` while running it.

`python WebCrawler.py website_address`

example:
`python WebCrawler.py http://marca.es`
