import scrapy
import html2text
from datetime import datetime
from ..items import MaradminScraperItem
from backend_api.models import Maradmin


class MaradminSpider(scrapy.Spider):
    name = "maradminspider"
    allowed_domains = ['marines.mil']
    start_urls = ["https://www.marines.mil/News/Messages/MARADMINS.aspx/?Page=1"]
    # Maradmin.objects.all().delete()

    def parse(self, response):
        yield from self.scrape(response)

    def scrape(self, response):
        for resource in response.css('div.item'):
            item = MaradminScraperItem()
            item['number'] = resource.css(".msg-num.msg-col a::text").extract_first()
            item['title'] = resource.css(".msg-title.msg-col a span::text").extract_first()
            raw_date = resource.css(".msg-pub-date.msg-col::text").extract_first()
            item['date'] = datetime.strptime(raw_date, '%m/%d/%Y')
            # print(f'{raw_date} = {item["date"]}')
            item["status"] = resource.css( ".msg-status.msg-col::text").extract_first()
            bodypage = resource.css(".msg-title.msg-col a::attr(href)").extract_first()
            item['url_link'] = bodypage

            request = scrapy.Request(bodypage, callback=self.get_body)
            request.cb_kwargs['item'] = item
            yield request
        selected_counter = response.css(
            "div.pager div.number-pager ul.pagination li a span.pages::text"
        ).getall()[-1]
        print('------------------')
        print(f'Selected Counter: {selected_counter}')
        max_counter = int(selected_counter)
        for num in range(2, max_counter + 1):
            print(f'Number: {num}')
            next_page_url = (
                f"https://www.marines.mil/News/Messages/MARADMINS.aspx/?Page={num}"
            )
            if next_page_url is not None:
                yield scrapy.Request(response.urljoin(next_page_url))
    
    def get_body(self, response, item):
        item = item
        body = response.css('.body-text').extract_first()
        converter = html2text.HTML2Text()
        converter.ignore_links = True
        item['body'] = converter.handle(body)
        yield item