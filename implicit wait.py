from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.python.org')
driver.implicitly_wait(10)

driver.get('https://www.python.org')
myDynamicElement = driver.find_element(By.ID, 'start-shell')

driver.close()
