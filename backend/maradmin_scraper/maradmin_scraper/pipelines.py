# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import logging
from itemadapter import ItemAdapter
from backend_api.models import Maradmin

class MaradminScraperPipeline:
    print('---------INSIDE MARADMIN SCRAPER PIPELINE-----------')
    def process_item(self, item, spider):
        logging.info('MaradminScraperPipeline: Processing Item')
        print('MaradminScraperPipeline: Processing Item')
        adapter = ItemAdapter(item)
        number = adapter.get('number')
        title = adapter.get('title')
        date = adapter.get('date')
        status = adapter.get('status')
        url_link = adapter.get('url_link')
        body = adapter.get('body')

        print(f'Items: {number}: {date}: {status}')

        obj, created = Maradmin.objects.get_or_create(
            number=number,
            title=title,
            date=date,
            status=status,
            url_link=url_link,
            body=body
            )
        return item
