from flask import Flask, request, jsonify
from app.models import db, Hero, Power, HeroPower

from app import create_app
app = create_app()

#GET HEROES

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes])

#CREATE HEROES
@app.route('/heroes', methods=['POST'])
def create_hero():
    data = request.get_json()
    if 'name' not in data or 'super_name' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    new_hero = Hero(name=data['name'], super_name=data['super_name'])
    db.session.add(new_hero)
    db.session.commit()
    return jsonify({"id": new_hero.id, "name": new_hero.name, "super_name": new_hero.super_name}), 201

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

#powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([{'id': power.id, 'name': power.name, 'description': power.description} for power in powers])

#create power


@app.route('/powers', methods=['POST'])
def create_power():
    data = request.get_json()
    if 'name' not in data or 'description' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    new_power = Power(name=data['name'], description=data['description'])
    db.session.add(new_power)
    db.session.commit()
    return jsonify({"id": new_power.id, "name": new_power.name, "description": new_power.description}), 201

# GET /powers/:id
@app.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = Power.query.get(power_id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    return jsonify({'id': power.id, 'name': power.name, 'description': power.description})

# PATCH /powers/:id
@app.route('/powers/<int:power_id>', methods=['PATCH'])
def update_power(power_id):
    power = Power.query.get(power_id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    
    data = request.get_json()
    description = data.get('description')
    if not description or len(description.strip()) == 0:
        return jsonify({'errors': ['Validation error: description is required']}), 400
    
    power.description = description
    db.session.commit()
    return jsonify({'id': power.id, 'name': power.name, 'description': power.description})

# POST /hero_powers
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    strength = data.get('strength')
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')
    
    if not strength or not hero_id or not power_id:
        return jsonify({'errors': ['Validation error: Missing required fields']}), 400
    
    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)
    
    if not hero or not power:
        return jsonify({'errors': ['Validation error: Hero or Power does not exist']}), 400
    
    hero_power = HeroPower(strength=strength, hero_id=hero_id, power_id=power_id)
    db.session.add(hero_power)
    db.session.commit()
    
    return jsonify({
        'id': hero_power.id,
        'strength': hero_power.strength,
        'hero_id': hero_power.hero_id,
        'power_id': hero_power.power_id,
        'hero': {
            'id': hero.id,
            'name': hero.name,
            'super_name': hero.super_name
        },
        'power': {
            'id': power.id,
            'name': power.name,
            'description': power.description
        }
    }), 201

