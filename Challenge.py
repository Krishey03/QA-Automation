from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://seleniumhq.org/')

element_id = driver.find_element(By.ID, 'q')
element_name = driver.find_element(By.NAME, 'q')
heading_xpath = driver.find_element(By.XPATH, "//*[@class='row']/h2[1]")
element_classname = driver.find_element(By.CLASS_NAME, 'selenium sponsors')

print(element_id)
print(element_name)
print(heading_xpath)
print(element_classname)

driver.close()
