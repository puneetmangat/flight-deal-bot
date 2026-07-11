from modules.flights import get_departure_airport, get_destination
from modules.analyzer import analyze_trip


def create_trip():
    departure = get_departure_airport()
    destination = get_destination()

    analysis = analyze_trip()

    return f"""✈️ Smart Travel Engine

From: {departure}
To: {destination}

{analysis}
"""
