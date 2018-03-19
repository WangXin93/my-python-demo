import scrapy

class EBooksSpider(scrapy.Spider):
    name = "ebooks"
    start_urls = [
        'http://www.allitebooks.com/page/1/',
    ]

    def parse(self, response):
        # Follow links to book pages
        for book_page in response.css('h2.entry-title a'):
            link = book_page.css('a::attr(href)').extract_first()
            yield response.follow(link, self.parse_book_urls)

        if len(response.url.split('/')) == 6:
            current_page = int(response.url.split('/')[-2])
        else:
            current_page = 1

        base_url = 'http://www.allitebooks.com/page/'
        next_url = base_url + str(current_page+1) + '/'
        yield response.follow(next_url, self.parse)

    def parse_book_urls(self, response):
        book_title = response.css('h1::text').extract_first()
        download_links = response.xpath("//span[@class='download-links']/a/@href").extract()
        with open('ebooks.txt', 'a') as f:
            f.write('Book title: %s\n' % book_title)
            f.write('Download link: %s\n' % download_links[0])
            f.write('Read link: %s\n' % download_links[1])
            f.write('\n')

