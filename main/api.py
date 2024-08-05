from flask_restful import Resource
from flask import jsonify, request
from sqlalchemy import func
from main.models import CourseModel, StudentModel, GroupModel, db


class GroupsWithLessEqualsStudents(Resource):
    def get(self):
        student_count = request.args.get('student_count', type=int, default=0)
        query = db.session.query(
            GroupModel.id,
            func.count(StudentModel.id).label('student_count')
        ). \
            outerjoin(StudentModel, GroupModel.id == StudentModel.group_id). \
            group_by(GroupModel.id). \
            having(func.count(StudentModel.group_id) <= student_count)

        return jsonify([{'group_id': group.id, 'student_count': group.student_count} for group in query])


class StudentsByCourseName(Resource):
    def get(self, course_name):
        course = CourseModel.query.filter_by(name=course_name).first()
        if course:
            return jsonify([student.to_dict() for student in course.students])
        return {'error': 'Course not found'}, 404


class AddStudent(Resource):
    def post(self):
        data = request.get_json()
        group_id = data.get('group_id')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        if not group_id or not first_name or not last_name:
            return {'error': 'Student group_id and first_name and last_name are required'}, 400
        new_student = StudentModel(group_id=group_id, first_name=first_name, last_name=last_name)
        db.session.add(new_student)
        db.session.commit()
        response_data = {
            'message': 'Student added successfully',
            'student': new_student.to_dict()
        }

        return response_data, 201


class DeleteStudent(Resource):
    def delete(self, student_id):
        student = StudentModel.query.get(student_id)
        if student:
            db.session.delete(student)
            db.session.commit()
            response_data = {
                'message': 'Student deleted successfully',
                'student': student.to_dict()
            }
            return response_data, 200
        return {'error': 'Student not found'}, 404


class AddStudentToCourse(Resource):
    def post(self, student_id):
        data = request.get_json()
        student = StudentModel.query.get(student_id)
        course = CourseModel.query.get(data['course_id'])
        if student and course:
            student.courses.append(course)
            db.session.commit()
            response_data = {
                'message': 'Student added successfully',
                'student': student.to_dict(),
                'course': course.to_dict()
            }
            return response_data, 200
        return {'error': 'Student or course not found'}, 404


class RemoveStudentFromCourse(Resource):
    def delete(self, student_id, course_id):
        student = StudentModel.query.get(student_id)
        course = CourseModel.query.get(course_id)
        if student and course in student.courses:
            student.courses.remove(course)
            db.session.commit()
            response_data = {
                'message': 'Student removed successfully',
                'student': student.to_dict(),
                'course': course.to_dict()
            }
            return response_data, 200
        return {'error': 'Student or course not found'}, 404
