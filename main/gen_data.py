from faker import Faker
import random
import itertools
import string

from main.models import GroupModel, StudentModel, CourseModel


def gen_coursemodel_data():
    name_courses = [
        ("Biochemistry", "A course about the chemical processes within and related to living organisms."),
        ("Chinese", "A course about the Chinese language, including speaking, reading, and writing."),
        ("Computer Science", "A course about the study of computers and computational systems."),
        ("Digital Humanities", "A course about the intersection of computing and the disciplines of the humanities."),
        ("Economics", "A course about the production, consumption, and transfer of wealth."),
        ("French", "A course about the French language and Francophone cultures."),
        ("Geography", "A course about the physical features of the earth and its atmosphere."),
        ("History", "A course about past events and civilizations."),
        ("Integrative Physiology", "A course about the function of biological systems from molecules to organisms."),
        ("Journalism", "A course about the gathering, assessing, creating, and presenting news and information.")
    ]
    return [CourseModel(name=name, description=desc) for name, desc in name_courses]


def gen_groupmodel_data():
    name_data = []
    for _ in range(10):
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        digits = ''.join(random.choices(string.digits, k=2))
        name_data.append(f"{letters}-{digits}")
    return [GroupModel(name=name) for name in name_data]


def gen_studentmodel_data():
    fake = Faker(['it_IT'])
    generator = random_number_generator()
    group_id = [next(generator) for _ in range(10, 30)]
    first_names = [fake.unique.first_name() for _ in range(20)]
    last_names = [fake.unique.last_name() for _ in range(20)]
    combinations = list(itertools.product(first_names, last_names))
    random.shuffle(combinations)
    names = [combinations.pop() for _ in range(200)]
    students = [(random.choice(group_id),) + name for name in names]

    return [StudentModel(group_id=gr_id, first_name=f_name, last_name=l_name) for gr_id, f_name, l_name in students]


def random_number_generator():
    while True:
        yield random.randint(1, 10)
