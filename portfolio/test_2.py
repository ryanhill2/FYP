from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('http://127.0.0.1:8000/')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/header/nav/div/div/div[2]/a[1]")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_name("username")
inputElement.send_keys('admin')
time.sleep(3)

inputElement = browser.find_element_by_name("password")
inputElement.send_keys('admin')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/form/div/button")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/div[4]/a/img")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/div[1]/a/img")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/header/nav/div/a")
inputElement.click()
time.sleep(3)

browser.get('http://127.0.0.1:8000/portfolio/addstock/')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/form/p[1]/input")
inputElement.send_keys('FB')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/form/p[2]/input")
inputElement.send_keys('5')
time.sleep(3)


inputElement = browser.find_element_by_xpath("/html/body/main/div/div/form/button")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/header/nav/div/a")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/div[4]/a/img")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/div[1]/a/img")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/form/p/textarea")
inputElement.send_keys('AIB KO')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/form/button")
inputElement.click()
time.sleep(3)