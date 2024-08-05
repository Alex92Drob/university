from os import environ as env


class DevConfig:
    SQLALCHEMY_DATABASE_URI = env.get(
        "DATABASE_URI", default="postgresql://admin:password@localhost:5432/university?sslmode=disable"
    )


class TestConfig:
    SQLALCHEMY_DATABASE_URI = env.get(
        "TEST_DATABASE_URI", default="postgresql://admin:password@localhost:5452/test?sslmode=disable"
    )
