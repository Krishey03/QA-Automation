import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Initialize the WebDriver and open the webpage
driver = webdriver.Firefox()
driver.get('http://jqueryui.com/droppable')

# Switch to the iframe containing the drag and drop elements
driver.switch_to.frame(0)

# Create an ActionChains object
action_chains = ActionChains(driver)

# Locate the source (draggable) and target (droppable) elements
source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')

# Perform a drag-and-drop operation by offset (100, 100)
action_chains.drag_and_drop_by_offset(source, 100, 100).perform()
time.sleep(2)

# Perform a drag-and-drop operation to the target element
action_chains.drag_and_drop(source, target).perform()
time.sleep(2)

# Close the browser
driver.close()
