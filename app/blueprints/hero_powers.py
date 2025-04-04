from flask import Blueprint, request, jsonify
from app import db
from app.models import HeroPower, Hero, Power

hero_powers_bp = Blueprint('hero_powers', __name__)

# CREATE a new hero-power relationship
@hero_powers_bp.route('', methods=['POST'])
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

# GET all hero-power relationships
@hero_powers_bp.route('', methods=['GET'])
def get_hero_powers():
    hero_powers = HeroPower.query.all()
    return jsonify([
        {
            'id': hp.id,
            'strength': hp.strength,
            'hero_id': hp.hero_id,
            'power_id': hp.power_id,
            'hero': {'id': hp.hero.id, 'name': hp.hero.name, 'super_name': hp.hero.super_name},
            'power': {'id': hp.power.id, 'name': hp.power.name, 'description': hp.power.description}
        }
        for hp in hero_powers
    ])
