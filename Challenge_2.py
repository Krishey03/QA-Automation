from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.selenium.dev/')

#element_id = driver.find_element(By.ID, 'gsc-iw-id1')
#element_name = driver.find_element(By.NAME, 'submit')
heading_xpath = driver.find_element(By.XPATH, "//h1[@class='d-1 fw-bold']")
#element_classname = driver.find_element(By.CLASS_NAME, 'selenium-backers')

#print(element_id)
#print(element_name)
print(heading_xpath)
#print(element_classname)

driver.close()
