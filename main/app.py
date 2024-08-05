from flask import Flask
from flask_restful import Api

from main.models import db
from main.config import DevConfig, TestConfig
from main.populate_data import populate_dev_data, populate_test_data
from main.api import GroupsWithLessEqualsStudents, StudentsByCourseName, AddStudent, DeleteStudent, AddStudentToCourse, \
    RemoveStudentFromCourse


def create_app(testing=None):
    app = Flask(__name__)
    api = Api(app)
    if testing:
        app.config.from_object(TestConfig)
    else:
        app.config.from_object(DevConfig)
    db.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()
        if testing:
            populate_test_data()
        else:
            populate_dev_data()

    api.add_resource(GroupsWithLessEqualsStudents, '/groups')
    api.add_resource(StudentsByCourseName, '/students/course/<string:course_name>')
    api.add_resource(AddStudent, '/students/new_student')
    api.add_resource(DeleteStudent, '/students/delete/<int:student_id>')
    api.add_resource(AddStudentToCourse, '/students/add_to_course/<int:student_id>')
    api.add_resource(RemoveStudentFromCourse, '/students/<int:student_id>/<int:course_id>')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='localhost', port=5001)
