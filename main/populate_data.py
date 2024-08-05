import random
from main.models import db, GroupModel, StudentModel, CourseModel
from main.gen_data import gen_groupmodel_data, gen_coursemodel_data, gen_studentmodel_data


def populate_dev_data():
    GroupModel.query.delete()
    StudentModel.query.delete()
    CourseModel.query.delete()

    groups_data = gen_groupmodel_data()
    courses_data = gen_coursemodel_data()
    students_data = gen_studentmodel_data()

    all_data = groups_data + courses_data + students_data
    db.session.add_all(all_data)
    db.session.commit()

    for student in students_data:
        for _ in range(random.randint(1, 3)):
            course = random.choice(courses_data)
            student.courses.append(course)
    db.session.commit()


def populate_test_data():
    group1 = GroupModel(name='BK-49')
    group2 = GroupModel(name='KB-10')
    group3 = GroupModel(name='IT-11')
    student1 = StudentModel(group_id=1, first_name='John', last_name='Doe')
    student2 = StudentModel(group_id=2, first_name='Romana', last_name='Conti')
    course1 = CourseModel(name='Biochemistry',
                           description='A course about the chemical processes within and related to living organisms.')
    course2 = CourseModel(name='Chinese',
                           description='A course about the Chinese language, including speaking, reading, and writing.')

    db.session.add_all([group1, group2, group3, student1, student2, course1, course2])

    db.session.commit()

    for student in [student1]:
        for course in [course1]:
            student.courses.append(course)
    db.session.commit()
