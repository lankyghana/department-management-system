from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from src.models.user import User
from src.models import db
from marshmallow import Schema, fields, ValidationError


user_bp = Blueprint('user', __name__)

class UserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)

user_schema = UserSchema()

@user_bp.route('/users', methods=['GET'])
@cross_origin()
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user_bp.route('/users', methods=['POST'])
@cross_origin()
def create_user():
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    try:
        data = user_schema.load(request.json)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    try:
        user = User(username=data['username'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        if 'UNIQUE constraint' in str(e):
            return jsonify({'error': 'Username or email already exists'}), 409
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

# Update user endpoint
@user_bp.route('/users/<int:user_id>', methods=['PUT'], endpoint='user_update')
@cross_origin()
def user_update(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    try:
        data = user_schema.load(request.json, partial=True)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    try:
        db.session.commit()
        return jsonify(user.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        if 'UNIQUE constraint' in str(e):
            return jsonify({'error': 'Username or email already exists'}), 409
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

# Delete user endpoint
@user_bp.route('/users/<int:user_id>', methods=['DELETE'], endpoint='user_delete')
@cross_origin()
def user_delete(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

@user_bp.route('/users/<int:user_id>', methods=['GET'])
@cross_origin()
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': f'User with id {user_id} not found'}), 404
    return jsonify(user.to_dict())

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
@cross_origin()
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': f'User with id {user_id} not found'}), 404
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    try:
        data = user_schema.load(request.json, partial=True)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    try:
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        db.session.commit()
        return jsonify(user.to_dict())
    except Exception as e:
        db.session.rollback()
        if 'UNIQUE constraint' in str(e):
            return jsonify({'error': 'Username or email already exists'}), 409
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
@cross_origin()
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': f'User with id {user_id} not found'}), 404
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': f'User {user_id} deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500
