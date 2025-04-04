from flask import Blueprint, request, jsonify
from app.models import db, Hero

heroes_bp = Blueprint('heroes_bp', __name__)

@heroes_bp.route('', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes])

@heroes_bp.route('', methods=['POST'])
def create_hero():
    data = request.get_json()
    if 'name' not in data or 'super_name' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    new_hero = Hero(name=data['name'], super_name=data['super_name'])
    db.session.add(new_hero)
    db.session.commit()
    return jsonify({"id": new_hero.id, "name": new_hero.name, "super_name": new_hero.super_name}), 201
