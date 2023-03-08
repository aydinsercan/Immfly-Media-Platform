
# Immfly Django App

Django project is designed as an example of Immfly media platform, which provide display contents and channels in a hierarchical structure.









## Endpoints
Now, you can send requests to the application according to the following endpoints

#### All channels which have no parent

```http
   localhost:8000/channels/
```

#### List of subchannels for given parent channel

```http
  localhost:8000/channels/id/
```

#### Retrieve channel contents

```http
  localhost:8000/channels/id/content/
```

## Docker 
Usage of docker to run the services

```http
   docker build --tag python-django .
   docker run --publish 8000:8000 python-django
```



## Project Structure

```bash
├── core
│   ├── management
│   │   ├── commands
│   │   │   └── exportCSV.py
│   │   └── utils
│   │       └── channel_rate.py
│   ├── migrations
│   ├── test
│   │   ├── test_rating.py
│   │   └── test_urls.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── ImmflyMediaPlatform
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates
│   ├── base.html
│   ├── channels.html
│   └── content.html
├── uploads
│   └── channels
├── README.md
├── manage.py
├── RatingOfChannels.csv
├── Dockerfile
└── db.sqlite3

```
## Tool set

- Django
- sqlite3
- Docker
- Postman
- Mypy

## Example Case

![ExampleCase](https://user-images.githubusercontent.com/32304725/223745516-c986ad64-9cb6-4ffd-9521-0618a418fa61.JPG)


##
__*Happy developing!*__

  