# import time
#
# from  selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/radio-button")
#
# # checkbox = driver.find_element("xpath", "//label[@for='tree-node-home']")
#
# # checkbox.click()
# YES_LABAL = ("xpath", "//label[@for='yesRadio']")
# YES_RADIO = ("xpath", "//input[@id='yesRadio']")
#
# IMPRESSIVE_BUTTON =  ("xpath", "//input[@id='impressiveRadio']")
# NO_BUTTON = ("xpath", "//input[@id='noRadio']")
#
# # print(driver.find_element(*NO_BUTTON).is_enabled())
# driver.find_element(*YES_LABAL).click()
# print(driver.find_element(*YES_RADIO).is_selected())
# time.sleep(5)
# import time
#
# from selenium import webdriver
# from selenium.webdriver.support import select
# from selenium.webdriver.support.select import Select
# from selenium.webdriver import Keys
#
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/select-menu")
# # DROP_EL = ("xpath", "//select[@id='dropdown']")
# # drop = Select(driver.find_element(*DROP_EL))
# # drop.select_by_value("1")
# MULT_SEL = ("xpath", "//input[@id='react-select-4-input']")
# select = driver.find_element(*MULT_SEL)
# select.send_keys("Green")
# assert  select.get_attribute("value") == "Green", "Error in value green"
# select.send_keys(Keys.ENTER)
# time.sleep(3)
# select.send_keys(Keys.ESCAPE)
# time.sleep(3)
#
# select.send_keys("Blue")
# assert  select.get_attribute("value") == "Blue", "Error in value Blue"
# select.send_keys(Keys.ENTER)
# time.sleep(3)
# select.send_keys(Keys.ESCAPE)
# time.sleep(3)
#
# select.send_keys("Black")
# assert  select.get_attribute("value") == "Black", "Error in value Black"
# select.send_keys(Keys.ENTER)
# time.sleep(3)
# select.send_keys(Keys.ESCAPE)
# time.sleep(3)
#
#
# select.send_keys("Red")
# assert  select.get_attribute("value") == "Red", "Error in value Red"
# select.send_keys(Keys.ENTER)
# time.sleep(3)
# select.send_keys(Keys.ESCAPE)
# time.sleep(3)
# import time
#
# from selenium import webdriver
# from  selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
#
# SOURSE = ("xpath", "//div[@id='draggable']")
# DRAG = ("xpath", "//div[@id='droppable']")
#
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/droppable")
# wait = WebDriverWait(driver, 10, 1)
#
# SOURSE = driver.find_element(*SOURSE)
# TARGET = driver.find_element(*DRAG)
#
# action = ActionChains(driver)
#
# action.drag_and_drop(SOURSE, TARGET).perform()
#
#
# time.sleep(5)
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(5)