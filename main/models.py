from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base

Base = declarative_base()
db = SQLAlchemy(model_class=Base)

students_courses_association = db.Table(
    'students_courses',
    Base.metadata,
    db.Column('student_id', db.Integer, db.ForeignKey('students.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'))
)


class GroupModel(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)

    students = db.relationship('StudentModel', backref='group')


class StudentModel(db.Model):
    __tablename__ = 'students'
    __table_args__ = (
        db.UniqueConstraint("first_name", "last_name"),
    )
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    courses = db.relationship('CourseModel', secondary=students_courses_association, back_populates='students')

    def to_dict(self):
        return {
            'id': self.id,
            'group_id': self.group_id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }


class CourseModel(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)

    students = db.relationship('StudentModel', secondary=students_courses_association, back_populates='courses')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
