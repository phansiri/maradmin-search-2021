import os
from django.core.management.base import BaseCommand
from maradmin_scraper.maradmin_scraper.spiders.maradmin_spider import MaradminSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class Command(BaseCommand):
    help = "Release the spiders"

    def __init__(self):
        settings_file_path = 'maradmin_scraper.maradmin_scraper.settings'
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        self.process = CrawlerProcess(get_project_settings())
        self.spider = MaradminSpider

    def handle(self, *args, **options):
        self.process.crawl(self.spider)
        self.process.start()