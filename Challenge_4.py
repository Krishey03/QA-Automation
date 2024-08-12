import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://wiki.python.org/moin/FrontPage')

#Automate a Search Function
search = driver.find_element(By.ID, 'searchinput')
search.clear();
search.send_keys("Beginner")
search.send_keys(Keys.RETURN)
time.sleep(2)

#Automate the select Function
select = Select(driver.find_element(By.XPATH, "//select[@name='actionsmenu']"))
select.select_by_visible_text("Raw Text")

driver.close()
