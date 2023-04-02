from app.model import Airports, Flights
from flask import render_template, Blueprint, request

map_bp = Blueprint('map', __name__)


@map_bp.route("/", methods=['GET', 'POST'])
def index():
    iata = "ALW"
    if request.method == 'POST':
        req_iata = request.form.get("selectAirport")
        if req_iata:
            iata=req_iata.strip()

    airport = Airports.query.filter_by(iata=iata).first()
    row_count = Flights.query.filter_by(origin_airport_iata=iata).count()

    airports = Airports.query.filter_by(country="United States");
    return render_template("index.html", selected_airport=airport, row_count=row_count, airports=airports)
