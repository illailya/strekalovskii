import pytest
from collections import namedtuple
from faker import Faker
faker = Faker()
from selenium import webdriver

# NewUser = namedtuple("_", ["login", "password"])
#
# user = NewUser(login=faker.user_name(), password=faker.password())
#
# print(user.password)
# @pytest.fixture()
# def user():
#     login = faker.user_name()
#     password = faker.password()
#     User = namedtuple("_", ["login", "password"])
#     return User(login, password)

# @pytest.fixture()
# def user_data(request):
#     request.cls.login = faker.user_name()
#     request.cls.password = faker.password()
@pytest.fixture(name="wdi")
def webdriver_init(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver