
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

## Example Algorithm Case

![ExampleCase](https://user-images.githubusercontent.com/32304725/223745516-c986ad64-9cb6-4ffd-9521-0618a418fa61.JPG)

## Example Endpoints

![Ekran Görüntüsü (69)](https://user-images.githubusercontent.com/32304725/228171297-22e65ddf-8c59-46b3-bfc1-324e0d908a04.png)

![Ekran Görüntüsü (70)](https://user-images.githubusercontent.com/32304725/228171614-abca0f0d-6997-42d3-8d93-50a63636fcc1.png)

![Ekran Görüntüsü (71)](https://user-images.githubusercontent.com/32304725/228171681-cf669b65-f342-4244-839e-d54ba8dcd0fb.png)

##
__*Happy developing!*__

  
