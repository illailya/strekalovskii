# import pytest
# faker = Faker()
# from selenium import webdriver
#
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
import os

# @pytest.fixture()
# def user_data(request):
#     request.cls.login = faker.user_name()
#     request.cls.password = faker.password()

# @pytest.fixture(name="wdi")
# def webdriver_init(request):
#     driver = webdriver.Chrome()
#     request.cls.driver = driver

#пример
# import pytest
# import sqlite3
#
#
# @pytest.fixture(name="db")
# def connect_db():
#     connection = sqlite3.connect('test.db')
#     yield
#     connection.close()

# import pytest
# from selenium import webdriver
#
#
# @pytest.fixture(autouse=True)
# def driver(request):
#
#     driver = webdriver.Chrome()
#     request.cls.driver = driver
#     print("до")
#     yield
#     driver.quit()
#     print("после")

# import pytest
# from faker import Faker
# faker = Faker()
#
# @pytest.fixture()
# def user():
#     username = faker.user_name()
#     return  username

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver(request):


    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(autouse=True)
def setup_environment_properties():
    properties = {
        "STAGE": os.environ["STAGE"],
        "BROWSER": os.environ["BROWSER"]
    }
    with open("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")