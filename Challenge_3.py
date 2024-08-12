from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.python.org/')

element_id = driver.find_element(By.ID, 'submit')
print(element_id)

element_name = driver.find_element(By.NAME, 'submit')
print(element_name)

element_xpath = driver.find_element(By.XPATH, "/html/body/div/header/div/h1/a/img")
print(element_xpath)

content = driver.find_element(By.CLASS_NAME, 'search-button')
print(content)

driver.close()
