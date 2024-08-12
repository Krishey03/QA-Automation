from selenium import webdriver
from selenium.webdriver.common.by import By

#Initialize the webdriver
driver = webdriver.Firefox()
driver.get("file:///D:/Automation%20test/Ex_Files_Python_Automation_Testing_Upd/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html")

#Find the login form using XPath strategies
content = driver.find_element(By.CLASS_NAME, 'content')

#Print the login forms
print("My class element is:")
print(content)

#close the web driver
driver.close()

