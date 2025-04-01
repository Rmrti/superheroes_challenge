from flask import Flask, request, jsonify
from models import db, Hero, Power, HeroPower

app = Flask(__name__)

#GET HEROES

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes])

# GET /heroes/:id

@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = Hero.query.get(hero_id)
    if not hero:
        return jsonify({'error': 'Hero not found'}), 404
    return jsonify({
        'id': hero.id,
        'name': hero.name,
        'super_name': hero.super_name,
        'hero_powers': [
            {
                'id': hp.id,
                'strength': hp.strength,
                'hero_id': hp.hero_id,
                'power_id': hp.power_id,
                'power': {
                    'id': hp.power.id,
                    'name': hp.power.name,
                    'description': hp.power.description
                }
            } for hp in hero.hero_powers
        ]
    })
