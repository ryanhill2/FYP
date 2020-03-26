from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
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

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/div[1]/a/img")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/div[2]/a/img")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/a[1]")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/div[1]/a/img")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/form/p[1]/input")
inputElement.send_keys('AIB')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/form/p[2]/input")
inputElement.send_keys('10')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/form/button")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/form/p[1]/input")
inputElement.send_keys('KO')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/form/p[2]/input")
inputElement.send_keys('2')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/form/button")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/form/a")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/div[2]/a/img")
inputElement.click()
time.sleep(5)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/a")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/header/nav/div/a")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/div[2]/a/img")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/a[2]")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/form/fieldset/div[1]/div/input")
inputElement.send_keys('The biggest crash is yet to come in 2020')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/form/fieldset/div[2]/div/textarea")
inputElement.send_keys('The biggest crash is yet to come in 2020 due to the american debt has reached over 23 trillion china and the american own most of this debt in the form of government bonds read more at www.cnn.com/theusbust')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/form/div/button")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/article[1]/div/h2/a")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/article/div/div/div/a[1]")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/form/fieldset/div[1]/div/input")
inputElement.clear()
inputElement.send_keys('The bull is back in wall street')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/form/fieldset/div[2]/div/textarea")
inputElement.clear()
inputElement.send_keys('The bull is back in wall street the following website is providing false info about the american debt www.cnn.com/theusbust')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/form/div/button")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/article/div/div/div/a[2]")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/form/div/button")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/article/div/h2/a")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/header/nav/div/a")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/div[3]/a/img")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/a")
inputElement.click()
time.sleep(3)


inputElement = browser.find_element_by_xpath("/html/body/header/nav/div/div/div[2]/a[1]")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/form/fieldset/div[1]/div/input")
inputElement.clear()
inputElement.send_keys('ryanhill')

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/form/div/button")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div[2]/form/fieldset/div[2]/div/input")
inputElement.clear()
inputElement.send_keys('ryanhill@mydit.ie')
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div[2]/form/div/button")
inputElement.click()
time.sleep(3)

inputElement = browser.find_element_by_xpath("/html/body/header/nav/div/a")
inputElement.click()
time.sleep(3)


#
# inputElement = browser.find_element_by_xpath("/html/body/main/div/div/div/form/fieldset/div[2]/div/textarea")
# inputElement.send_keys('The bull is back in wall street the following website is providing false info about the american debt www.cnn.com/theusbust')
# time.sleep(3)



# browser.find_elements(By.XPATH, "/html/body/header/nav/div/div/div[2]/a[1]")