from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('http://127.0.0.1:8000/')
time.sleep(3)
elem = browser.find_element_by_link_text('Register')
elem.click()
time.sleep(3)

inputElement = browser.find_element_by_name("username")
inputElement.send_keys('ryan')
time.sleep(3)

inputElement = browser.find_element_by_name("email")
inputElement.send_keys('ryan@gmail.com')
time.sleep(3)

inputElement = browser.find_element_by_name("password1")
inputElement.send_keys('Password321')
time.sleep(3)

inputElement = browser.find_element_by_name("password2")
inputElement.send_keys('Password321')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/form/div/button")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_name("username")
inputElement.send_keys('ryan')
time.sleep(3)

inputElement = browser.find_element_by_name("password")
inputElement.send_keys('Password321')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div[2]/form/div/button")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/div[1]/a/img")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/div[1]/a/img")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/form/p/input")
inputElement.send_keys("Ryan's portfolio")
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/form/button")
inputElement.click()
time.sleep(3)

browser.get('http://127.0.0.1:8000/')

# inputElement = browser.find_element_by_xpath("/html/body/main/div/div/form/button")
# inputElement.click()
# time.sleep(2)


# browser.find_elements(By.XPATH, "/html/body/header/nav/div/div/div[2]/a[1]")