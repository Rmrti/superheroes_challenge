from flask import Flask, request, jsonify
from models import db, Hero, Power, HeroPower

app = Flask(__name__)

#GET HEROES

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes])
