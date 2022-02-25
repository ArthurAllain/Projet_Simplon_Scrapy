import scrapy


# A spider is a class that subclasses scrapy.Spider
# This class is used to scrape data from the urls in the "urls" list
class QuotesSpider(scrapy.Spider):
    
    name = "quotes" # This is the name of the spider. It is used to reference the spider in the command line.

    def start_requests(self):   # This function is called by the Scrapy framework and iterates over the urls in the "urls" list.
        # Creating a list of urls to scrape.
        urls = [
            "http://quotes.toscrape.com/page/1/",
            "http://quotes.toscrape.com/page/2/"
        ]
        # This is the Scrapy framework calling the `start_requests` function and iterating over the
        # urls in the "urls" list.
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        # This is getting the page number from the url.
        page = response.url.split("/")[-2]
        # This is a string formatting operation. It is creating a filename using the page number from
        # the url.
        filename = f'quotes-{page}.html'
        # This is a context manager. It is opening the file and writing the response body to the file.
        with open(filename, 'wb') as f:
            f.write(response.body)              # Writing the response body to the file.
        self.log(f'Saved file {filename}')      # This is a logging function. It is logging the string to the terminal.