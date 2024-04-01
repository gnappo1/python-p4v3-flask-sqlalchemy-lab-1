# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route("/")
def index():
    body = {"message": "Flask SQLAlchemy Lab 1"}
    return make_response(body, 200)


# Add views here
@app.route("/earthquakes/<int:id>")
def earthquake_by_id(id):
    try:
        earthquake = Earthquake.query.get_or_404(id)
        return earthquake.as_dict(), 200
    except Exception as e:
        return {"message": f"Earthquake {id} not found."}, 404
    # try:
    #     if earthquake := db.session.get(Earthquake, id):
    #         return earthquake.as_dict(), 200
    #     return {"message": f"Earthquake {id} not found."}
    # except Exception as e:
    #     return e


@app.route("/earthquakes/magnitude/<float:magnitude>")
def earthquake_by_magnitude(magnitude):
    try:
        earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude)
        serialized_quakes = [earthquake.as_dict() for earthquake in earthquakes]
        return {
            "count": len(serialized_quakes),
            "quakes": serialized_quakes,
        }, 200
    except Exception as e:
        return {"message": f"Earthquake {id} not found."}, 404


if __name__ == "__main__":
    app.run(port=5555, debug=True)
