import scrapy
import os #?
import re
from urllib.parse import urljoin

class BrickSetSpider(scrapy.Spider):
    name = 'brick_spider'
    start_urls = ['https://enjoybooks.pw/page/4/']
    #start_urls = ['https://enjoybooks.pw/']

    def parse(self, response):
        SET_SELECTOR = '.tagdiv-module-wrap'
        for bookset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h3 ::text'
            AUTOR_SELECTOR = 'a[class="author"] ::text'
            BOOK_URL_SELECTOR = 'h3 > a[href^="https"]'
            book_url = bookset.css(BOOK_URL_SELECTOR).extract_first()
            urls_book = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', book_url)
            TEXT_SELECTOR = 'p ::text'
            yield {
                'book': bookset.css(NAME_SELECTOR).extract_first(),
                'author': bookset.css(AUTOR_SELECTOR).extract_first(),
                'urls': urls_book,
                'text': bookset.css(TEXT_SELECTOR).extract_first(),
            }

        NEXT_PAGE_SELECTOR ='//a[@class="next page-numbers"]/@href'
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )












# ~/djangotih/searchpj/searchenv source bin/activate
# ~/djangotih/searchpj/searchenv/search_project/searchpj python manage.py runserver

# ~/djangotih/searchpj/searchenv/search_project/searchpj/my_scraper
# scrapy runspider scraper.py
# scrapy runspider scraper.py -o output.csv -t csv
# scrapy runspider scraper.py -o output.json
