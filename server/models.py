from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


# Add models here
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"

    id =  db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, nullable=False)
    magnitude =  db.Column(db.Float, nullable=False)
    year =  db.Column(db.Integer, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey("planets.id"))
    
    planet = db.relationship("Planet", back_populates="quakes")

    def __repr__(self):
        return f"""
            <Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>
        """

    def as_dict(self):
        return {
            "id": self.id,
            "location": self.location,
            "magnitude": self.magnitude,
            "year": self.year,
        }


class Planet(db.Model, SerializerMixin):
    __tablename__ = "planets"

    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    quakes = db.relationship("Earthquake", back_populates="planet")
    
    def __repr__(self):
        return f"""
            <Planet #{self.id}, {self.name}>
        """

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
