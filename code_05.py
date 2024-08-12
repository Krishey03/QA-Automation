from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://selenium.org')
time.sleep(2)

driver.close
