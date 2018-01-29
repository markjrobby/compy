import subprocess
from selenium import webdriver
from subprocess import call

var = input("Please enter website url (e.g 'www.google.com'): ")
call(['wget', '-r', var])
output = subprocess.check_output(['find', var]).splitlines()

for i in range(len(output)):
    browser = driver = webdriver.Firefox()
    browser.get('https://'+str(output[i]))
    browser.maximize_window()
    browser.get_screenshot_as_file(str(output[i])+'.png')
    browser.quit()
