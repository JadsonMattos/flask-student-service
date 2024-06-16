from flask import Blueprint, jsonify, request
from models.student_model import StudentModel

student_controller = Blueprint("students", __name__)


def _get_students():
    students = StudentModel.find()
    return [student.to_dict() for student in students]


@student_controller.route("", methods=["GET"])
def get_students():
    students = _get_students()
    if students is None:
        return jsonify({"error": "No students available"}), 404
    return jsonify(students), 200


@student_controller.route("/<enrollment>", methods=["GET"])
def get_student(enrollment):
    student = StudentModel.find_one({"enrollment_number": enrollment})
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student.to_dict()), 200


@student_controller.route("", methods=["POST"])
def create_student():
    data = request.json
    if "name" not in data or "enrollment_number" not in data:
        return jsonify({"error": "Missing name or enrollment_number \
in request body"}), 400
    new_student = StudentModel(data)
    new_student.save()
    return jsonify(new_student.to_dict()), 201


@student_controller.route("/<enrollment>", methods=["DELETE"])
def delete_student(enrollment):
    student = StudentModel.find_one({"enrollment_number": enrollment})
    if not student:
        return jsonify({"error": "Student not found"}), 404
    student.delete()
    return "", 204


@student_controller.route("/<enrollment>", methods=["PUT"])
def update_student(enrollment):
    student = StudentModel.find_one({"enrollment_number": enrollment})
    if student is None:
        return '', 404
    data = request.json
    student.update(data)
    return jsonify(student.to_dict()), 200
