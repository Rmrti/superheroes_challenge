from flask import Blueprint, request, jsonify
from app import db
from app.models import Power

powers_bp = Blueprint('powers', __name__)

# GET all powers
@powers_bp.route('', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([{'id': power.id, 'name': power.name, 'description': power.description} for power in powers])

# CREATE a new power
@powers_bp.route('', methods=['POST'])
def create_power():
    data = request.get_json()
    if 'name' not in data or 'description' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    new_power = Power(name=data['name'], description=data['description'])
    db.session.add(new_power)
    db.session.commit()
    return jsonify({"id": new_power.id, "name": new_power.name, "description": new_power.description}), 201

# GET a specific power by ID
@powers_bp.route('/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = Power.query.get(power_id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    return jsonify({'id': power.id, 'name': power.name, 'description': power.description})

# UPDATE (PATCH) a power's description
@powers_bp.route('/<int:power_id>', methods=['PATCH'])
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
