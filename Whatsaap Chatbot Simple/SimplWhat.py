"""
A simple Web Automation that Sends Message to the
searched person or group in Whatsaap.
There needs to be Selenium Installed on the Machine.
There should be a moderate to good Internet Connection.
The Webdriver should be of the same version as that of the chrome you are using.(8.3)
The User needs to scan the Web whatsaap , when the login portion Comes. This is a manual login
and will not be enabled automatically.
"""
from selenium import webdriver
import time

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("https://web.whatsapp.com/")
time.sleep(15)
search_name=browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search_name.send_keys("<name of the group/person>")#Give the Name of the Person / Group In Whatsaap which you want to Search

time.sleep(5)
name1=browser.find_element_by_class_name("_3j7s9")
time.sleep(2)
name1.click()

time.sleep(3)
msg=browser.find_element_by_class_name("_1Plpp")
#Type the Message that you want to send to the particular person/group.
msg.send_keys("<Message to be sent to the Desired Person /Groupin Whatsaap>")
time.sleep(3)
button=browser.find_element_by_class_name("_35EW6")
button.click()


