#!/usr/bin/env python3
# server/seed.py

from app import app
from models import db, Earthquake, Planet

with app.app_context():

    # Delete all rows in the "earthquakes" table
    Earthquake.query.delete()
    Planet.query.delete()
    # Add several Planet instances to the "planets" table
    db.session.add(Planet(name="Mars"))
    db.session.add(Planet(name="Earth"))
    # Add several Earthquake instances to the "earthquakes" table
    db.session.add(Earthquake(magnitude=9.5, location="Chile", year=1960, planet_id=1))
    db.session.add(Earthquake(magnitude=9.2, location="Alaska", year=1964, planet_id=1))
    db.session.add(Earthquake(magnitude=8.6, location="Alaska", year=1946, planet_id=1))
    db.session.add(Earthquake(magnitude=8.5, location="Banda Sea", year=1934, planet_id=2))
    db.session.add(Earthquake(magnitude=8.4, location="Chile", year=1922, planet_id=2))

    # Commit the transaction
    db.session.commit()
