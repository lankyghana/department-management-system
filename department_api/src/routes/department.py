from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from src.models.department import Department
from src.models import db
from marshmallow import Schema, fields, ValidationError


department_bp = Blueprint('department', __name__)

class DepartmentSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str()

department_schema = DepartmentSchema()

@department_bp.route('/departments', methods=['GET'])
@cross_origin()
def get_departments():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 6))
    except ValueError:
        return jsonify({'error': 'Invalid pagination parameters'}), 400
    pagination = Department.query.paginate(page=page, per_page=per_page, error_out=False)
    departments = [department.to_dict() for department in pagination.items]
    return jsonify({
        'departments': departments,
        'total': pagination.total,
        'page': pagination.page,
        'pages': pagination.pages
    })

@department_bp.route('/departments', methods=['POST'])
@cross_origin()
def create_department():
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    try:
        data = department_schema.load(request.json)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    department = Department(
        name=data['name'],
        description=data.get('description', '')
    )
    try:
        db.session.add(department)
        db.session.commit()
        return jsonify(department.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        if 'UNIQUE constraint' in str(e):
            return jsonify({'error': 'Department name already exists'}), 409
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

@department_bp.route('/departments/<int:department_id>', methods=['GET'])
@cross_origin()
def get_department(department_id):
    department = Department.query.get(department_id)
    if not department:
        return jsonify({'error': f'Department with id {department_id} not found'}), 404
    return jsonify(department.to_dict())

@department_bp.route('/departments/<int:department_id>', methods=['PUT'])
@cross_origin()
def update_department(department_id):
    department = Department.query.get(department_id)
    if not department:
        return jsonify({'error': f'Department with id {department_id} not found'}), 404
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    try:
        data = department_schema.load(request.json, partial=True)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    try:
        department.name = data.get('name', department.name)
        department.description = data.get('description', department.description)
        db.session.commit()
        return jsonify(department.to_dict())
    except Exception as e:
        db.session.rollback()
        if 'UNIQUE constraint' in str(e):
            return jsonify({'error': 'Department name already exists'}), 409
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

@department_bp.route('/departments/<int:department_id>', methods=['DELETE'])
@cross_origin()
def delete_department(department_id):
    department = Department.query.get(department_id)
    if not department:
        return jsonify({'error': f'Department with id {department_id} not found'}), 404
    try:
        db.session.delete(department)
        db.session.commit()
        return jsonify({'message': f'Department {department_id} deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

