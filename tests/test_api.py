import pytest
from main.app import create_app


@pytest.fixture
def test_client():
    app = create_app(testing=True)
    return app.test_client()


def test_groups_with_less_equals_students(test_client):
    response = test_client.get('/groups')
    assert response.status_code == 200


def test_students_by_course_name(test_client):
    response = test_client.get('/students/course/Chinese')
    assert response.status_code == 200


def test_add_student(test_client):
    response = test_client.post('/students/new_student', json={
        'group_id': 3,
        'first_name': 'Sarah',
        'last_name': 'Connor'
    })
    assert response.status_code == 201
    assert response.get_json() == {'message': 'Student added successfully',
                                   'student': {'first_name': 'Sarah',
                                               'group_id': 3,
                                               'id': 3,
                                               'last_name': 'Connor'}}, 201


def test_delete_student(test_client):
    response = test_client.delete('/students/delete/2')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Student deleted successfully',
                                   'student': {'first_name': 'Romana',
                                               'group_id': 2,
                                               'id': 2,
                                               'last_name': 'Conti'}}, 200


def test_add_student_to_course(test_client):
    response = test_client.post('/students/add_to_course/2', json={
        'course_id': 2
    })
    assert response.status_code == 200
    assert response.get_json() == {'course': {'id': 2, 'name': 'Chinese'},
                                   'message': 'Student added successfully',
                                   'student': {'first_name': 'Romana',
                                               'group_id': 2,
                                               'id': 2,
                                               'last_name': 'Conti'}}, 200


def test_remove_student_from_course(test_client):
    response = test_client.delete('/students/1/1')
    assert response.status_code == 200
    assert response.get_json() == {'course': {'id': 1, 'name': 'Biochemistry'},
                                   'message': 'Student removed successfully',
                                   'student': {'first_name': 'John', 'group_id': 1, 'id': 1, 'last_name': 'Doe'}}, 200
