# Flask Map Application - Video 2

To install pg_tileserv, we ran: 

```
docker run --network="pgnet" -dt -e DATABASE_URL=postgresql://postgres:fr24Password@postgis/flightradar -p 7800:7800 pramsey/pg_tileserv:latest
```

To start the app, open up the command line and navigate to this folder. Run

```
set FLASK_APP=app
```

```
set FLASK_ENV=development
```

```
flask run
```
