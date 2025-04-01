

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    super_name = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    # relationship with super powers

    hero_powers = db.relationship('HeroPower', backref='hero')


