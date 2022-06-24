# jambopay-test

Jambopay Interview Project

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

To interact with the apis via swagger-ui:

  [http://74.207.232.253:8000/swagger/](http://74.207.232.253:8000/swagger/) 

Locally, you can also use the swagger-ui to interact with the apis after you have started the dev server via docker-compose:
  [http://0.0.0.0:8000/swagger/](http://0.0.0.0:8000/swagger/)

To run the tests via docker

```bash
docker-compose run --rm web python3 manage.py test books
```
