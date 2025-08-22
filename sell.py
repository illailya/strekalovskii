# import time
#
# from selenium import webdriver
# from selenium.webdriver import Keys
#
#
# driver = webdriver.Chrome()
# driver.get("http://the-internet.herokuapp.com/key_presses")
#
# filed = driver.find_element("xpath", "//input[@id='target']")
# filed.send_keys("hello")
# time.sleep(3)
# filed.send_keys(Keys.CONTROL+"A")
# time.sleep(3)
# filed.send_keys(Keys.BACK_SPACE)
# time.sleep(3)
#
# # first_name_filed = driver.find_element("xpath", "//input[@placeholder='Full Name']")
# # first_name_filed.send_keys("Илья")
# # first_name_filed.get_attribute("value")
# # assert first_name_filed.get_attribute("value") == "Илья", "error in first_name"
# #
# # Email_filed = driver.find_element("xpath", "//input[@id='userEmail']")
# # Email_filed.send_keys("frf@jg.com")
# # Email_filed.get_attribute("value")
# # assert Email_filed.get_attribute("value") == "frf@jg.com", "error in Email_filed"
# #
# # Adres_filed = driver.find_element("xpath", "//textarea[@id='currentAddress']")
# # Adres_filed.send_keys("lenina")
# # Adres_filed.get_attribute("value")
# # assert Adres_filed.get_attribute("value") == "lenina", "error in Adres_filed"
# # time.sleep(3)
#
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# # options.add_argument("--headless")
# # options.add_argument("--incognito")
# # options.add_argument("--ignore-certificate-errors")
# options.add_argument("--window-size=1920,1080")
# # options.page_load_strategy = "eager"
#
# FILE_UPLOAD = ("xpath", "//input[@id='uploadFile']")
#
#
# driver = webdriver.Chrome(options=options)
# driver.get("https://demoqa.com/upload-download")
#
# fild_field = driver.find_element(*FILE_UPLOAD)
# fild_field.send_keys(r"D:\pyton\example.jpeg")
# time.sleep(3)
# import time
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
#
# options = webdriver.ChromeOptions()
# options.add_argument("--windows-size=1920,1080")
#
# VISIBLE_AFTER = ("xpath", "//button[@id='visibleAfter']")
# ANABLE_AFTER = ("xpath", "//button[@id='enableAfter']")
#
# driver = webdriver.Chrome(options=options)
# driver.get("https://demoqa.com/dynamic-properties")
#
# wait = WebDriverWait(driver, 10, poll_frequency=1)
#
# wait.until(EC.element_to_be_clickable(ANABLE_AFTER))
#
# time.sleep(5)
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import  WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# options = webdriver.ChromeOptions()
# options.add_argument("--windows-size=1920, 1080")
# options.add_argument("--disable-dlink-features=AutomationControlled")
# options.add_experimental_option("excludeSwitches",["enable-automation"])
# options.add_experimental_option("useAutomationExtension",False)
from lesson1 import weight


# driver = webdriver.Chrome(options=options)
# wait = WebDriverWait(driver,10,1)
# driver.get("https://demoqa.com/alerts")
#
# driver.find_element("xpath","//button[@id='promtButton']").click()
# alert = wait.until(EC.alert_is_present())
# time.sleep(3)
# alert.send_keys("ilua")
# time.sleep(3)
# alert.accept()
#
# time.sleep(3)

# import json
# import time
# from cookies_manager import CookieManager
#
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# options.add_argument("--window-size=1920,1080")
#
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.freeconferencecall.com/ru/ru/login")
#
#
#
# cookies_manager = CookieManager(driver)
# cookies_manager.load()
# time.sleep(3)
#
#
