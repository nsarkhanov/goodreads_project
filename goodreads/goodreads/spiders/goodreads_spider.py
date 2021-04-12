import scrapy


class GoodreadsSpider(scrapy.Spider):
    name = "goodreads"
    start_url = [
        "https://www.goodreads.com/list/show/1043.Books_That_Should_Be_Made_Into_Movies"]
