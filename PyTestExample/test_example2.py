import pytest
import allure
from allure_commons.types import Severity
from allure_commons.types import AttachmentType




# from selenium import webdriver
#
@pytest.mark.usefixtures("driver")
@allure.epic("Accounts")
@allure.feature("Login")
@allure.story("Pages")
class TestLogin:
#
#     def setup_method(self):
#         self.driver = webdriver.Chrome()
    @pytest.mark.smoke
    @allure.title("Open login page")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence/login", name="Documents")
    def test_open_login_page(self):

        with allure.step("Open page. step 1"):
            self.driver.get("https://demoqa.com/login")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Login page",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Assert page. Step 2"):
            assert  self.driver.current_url == "https://demoqa.com/login", ".ошибка"

    @pytest.mark.smoke
    @allure.title("Open book page")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence/books", name="Documents")
    def test_open_books_page(self):
        self.driver.get("https://demoqa.com/books")
        assert  self.driver.current_url == "https://demoqa.com/bks", ".ошибка books_page"

    @pytest.mark.profile
    @allure.title("Open profile page")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence/profile", name="Documents")
    def test_open_profile_page(self):
        self.driver.get("https://demoqa.com/profile")
        assert  self.driver.current_url == "https://demoqa.com/profile", ".ошибка profile_page"
#
    def teardown_method(self):
        self.driver.quit()