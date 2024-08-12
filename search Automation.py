from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://python.org/');

search = driver.find_element(By.NAME, 'q');
search.clear();
search.send_keys("pycon");
search.send_keys(Keys.RETURN);
time.sleep(4)

driver.close();
