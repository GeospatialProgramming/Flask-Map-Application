from geoalchemy2.types import Geometry

from . import db
from . import config


class Airports(db.Model):
    __tablename__ = 'airports'

    ogc_fid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    iata = db.Column(db.String)
    icao = db.Column(db.String)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    country = db.Column(db.String)
    alt = db.Column(db.String)

    wkb_geometry = db.Column(Geometry(geometry_type='Point', srid=4326))


class Flights(db.Model):
    __tablename__ = 'flights'

    prim_key = db.Column(db.Integer, primary_key=True)

    id = db.Column(db.String)
    icao_24bit = db.Column(db.String)
    heading = db.Column(db.Integer)
    altitude = db.Column(db.Integer)
    ground_speed = db.Column(db.Integer)
    squawk = db.Column(db.Integer)
    aircraft_code = db.Column(db.String)
    registration = db.Column(db.String)
    time = db.Column(db.Integer)
    origin_airport_iata = db.Column(db.String)
    destination_airport_iata = db.Column(db.String)
    number = db.Column(db.String)
    airline_iata = db.Column(db.String)
    on_ground = db.Column(db.Integer)
    vertical_speed = db.Column(db.Integer)
    callsign = db.Column(db.String)
    airline_icao = db.Column(db.String)

    geometry = db.Column(Geometry(geometry_type='Point', srid=4326))