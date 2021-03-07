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

## Test

[IW]

## Reference

1. [https://www.fullstacklabs.co/blog/django-graphene-rest-graphql](https://www.fullstacklabs.co/blog/django-graphene-rest-graphql)
2. [Running Scrapy spiders in a Celery task](https://www.javaer101.com/en/article/3255456.html)
3. [Asynchronous Tasks With Django and Celery](https://realpython.com/asynchronous-tasks-with-django-and-celery/)
4. [Making a Web Scraping Application with Python, Celery, and Django](https://codeburst.io/making-a-web-scraping-application-with-python-celery-and-django-23162397c0b6)