# Project MARADMIN Search - 2021

## Technology

1. Django for the backend
2. Graphql to provide an API endpoint
3. Vue3 for the frontend

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
docker-compose logs 'web'
docker-compose logs 'celery'
docker-compose logs 'celery-beat'
docker-compose logs 'redis'

docker-compose logs -f "celery"
```

## Test

[IW]

## Useful Commands
1. `docker-compose exec web python manage.py createsuperuser`
2. `docker-compose exec web python manage.py maradmin_crawl` manually start web scraper
3. `docker-compose exec web python manage.py makemigrations`
4. `docker-compose exec web python manage.py migrate`

## Reference

1. [https://www.fullstacklabs.co/blog/django-graphene-rest-graphql](https://www.fullstacklabs.co/blog/django-graphene-rest-graphql)
2. [Running Scrapy spiders in a Celery task](https://www.javaer101.com/en/article/3255456.html)
3. [Asynchronous Tasks With Django and Celery](https://realpython.com/asynchronous-tasks-with-django-and-celery/)
4. [Making a Web Scraping Application with Python, Celery, and Django](https://codeburst.io/making-a-web-scraping-application-with-python-celery-and-django-23162397c0b6)
5. [Walking over the site we want to scrape](https://resbazsql.github.io/lc-webscraping/05-scraping-multiple-pages-with-scrapy/)
6. [Django + Scrapy](https://ginopalazzo.github.io/scraper/django-scrapy.html)
7. [Getting scrapy project settings when script is outside of root directory](https://stackoverflow.com/questions/31662797/getting-scrapy-project-settings-when-script-is-outside-of-root-directory)
8. [Handling Periodic Tasks in Django with Celery and Docker](https://testdriven.io/blog/django-celery-periodic-tasks/)
9. [Flutter - Instant search with Firestore](https://www.youtube.com/watch?v=0szEJiCUtMM)
10. [Django Search + Flutter](https://medium.com/flutter-community/django-search-flutter-1cb3e8a5db1a)
11. [How To Serve A Flutter Web App From A Docker Container](https://www.jarednelsen.dev/posts/how-to-serve-a-flutter-web-app-from-a-docker-container)
