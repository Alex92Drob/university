![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)

# University Application

## Description

This Flask-based application manages university data, including students, courses, and groups. It provides RESTful APIs
for efficient data management and retrieval.

## Features

* Student Management: Add, edit, delete students.
* Course Management: Add students to courses, remove them.
* Group Management: Manage groups and their students.
* Queries: Retrieve students by course name, groups with a certain number of students.

## Prerequisites

Ensure you have the following installed:

* Python 3.x
* Flask
* Flask-SQLAlchemy
* Flask-RESTful

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Alex92Drob/university.git
cd university
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

## Usage

The application runs on http://localhost:5001. Use the provided endpoints to manage students, courses, and groups.
Example endpoints:

* Get groups with a maximum number of students: /groups?student_count=<number>
* Get students by course name: /courses/<course_name>/students
* Add a student: /students
* Delete a student: /students/<student_id>
* Add student to a course: /students/<student_id>/courses
* Remove student from a course: /students/<student_id>/courses/<course_id>