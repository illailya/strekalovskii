# from selenium import webdriver
#
#
# class TestExample:
#     # locators
#     USERNAME_FILED = ("xpath", "//input[@id='userName']")
#     EMAIL_FIELD = ("xpath", "//input[@id = 'userEmail']")
#     CURRENT_ADDRESS_FIELD = ("xpath", "//textarea [@id='currentAddress']")
#     SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
#     OUTPUT_BLOCK = ("xpath", "//div[@id='output']")
#     # тестовый метод
#     def test_valid_data(self):
#
#         driver = webdriver.Chrome()
#         driver.get("https://demoqa.com/text-box")
#
#         username = driver.find_element(*self.USERNAME_FILED)
#         username.send_keys("Ilya")
#         assert username.get_attribute("value") == "Ilya"
#
#         email = driver.find_element(*self.EMAIL_FIELD)
#         email.send_keys("ilya@gmail.com")
#         assert email.get_attribute("value") == "ilya@gmail.com"
#
#         address = driver.find_element(*self.CURRENT_ADDRESS_FIELD)
#         address.send_keys("sovetska17")
#         assert address.get_attribute("value") == "sovetska17"
#
#         driver.find_element(*self.SUBMIT_BUTTON).click()
#
#         output = driver.find_element(*self.OUTPUT_BLOCK)
#         assert output.is_displayed() is True
#         assert ("Ilya" and "ilya@gmail.com" and "sovetska17") in output.text
from requests import options
