# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from backend_api.models import Maradmin

class MaradminScraperItem(DjangoItem):
    django_model = Maradmin
