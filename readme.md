# Project MARADMIN Search - 2021

## Technology

1. Django for the backend
2. Graphql to provide an API endpoint
3. Flutter for the frontend

## Graphql query string example

```api
query {
  allMaradmins(body_Icontains: "officer") {
    edges {
      node {
        id,
        number
        title
      }
    }
  }
}
```


test if `docker-compose up --build` is running correctly
```bash
$ docker-compose logs 'web'
$ docker-compose logs 'celery'
$ docker-compose logs 'celery-beat'
$ docker-compose logs 'redis'
```

## Test

[IW]

## Reference

1. [https://www.fullstacklabs.co/blog/django-graphene-rest-graphql](https://www.fullstacklabs.co/blog/django-graphene-rest-graphql)
2. [Running Scrapy spiders in a Celery task](https://www.javaer101.com/en/article/3255456.html)
3. [Asynchronous Tasks With Django and Celery](https://realpython.com/asynchronous-tasks-with-django-and-celery/)
4. [Making a Web Scraping Application with Python, Celery, and Django](https://codeburst.io/making-a-web-scraping-application-with-python-celery-and-django-23162397c0b6)
5. [Walking over the site we want to scrape](https://resbazsql.github.io/lc-webscraping/05-scraping-multiple-pages-with-scrapy/)
6. [Django + Scrapy](https://ginopalazzo.github.io/scraper/django-scrapy.html)
7. [Getting scrapy project settings when script is outside of root directory](https://stackoverflow.com/questions/31662797/getting-scrapy-project-settings-when-script-is-outside-of-root-directory)
