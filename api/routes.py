from flask import jsonify, request
from config import Db
from modelos.Student import Student


def init_api_routes(app):
    @app.route('/api/users', methods=['GET'])
    def get_users():
        students = Db.session.query(Student).all()
        student_list = [student.to_dict() for student in students]
        return jsonify(student_list)

    @app.route('/api/user_by_id/<int:id>', methods=['GET'])
    def get_user_by_id(id):
        student = Db.session.query(Student).filter_by(id=id).first()
        return jsonify(student.to_dict())

    @app.route('/api/user', methods=['POST'])
    def add_user():
        data = request.json
        student = Student(data['id'], data['name'], data['spec'], data['age'])
        Db.session.add(student)
        Db.session.commit()
        return jsonify(student.to_dict())

    @app.route('/api/user/<int:id>', methods=['PUT'])
    def update_user(id):
        student = Db.session.query(Student).filter_by(id=id).first()
        data = request.json
        student.name = data['name']
        student.spec = data['spec']
        student.age = data['age']
        Db.session.commit()
        return jsonify({"message": "User updated successfully", "user": student.to_dict()})

    @app.route('/api/user/<int:id>', methods=['DELETE'])
    def delete_user(id):
        student = Db.session.query(Student).filter_by(id=id).first()
        Db.session.delete(student)
        Db.session.commit()
        return jsonify({"message": "User deleted successfully", "user": student.to_dict()})

