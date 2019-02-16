from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from secret_file import email_field_secret, password_field_secret
driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://clarkdotlaw.monday.com/boards/177178045');
email_field = driver.find_element_by_id("user_email")
email_field.send_keys(email_field_secret)
password_field = driver.find_element_by_id("user_password")
password_field.send_keys(password_field_secret)
# driver.quit()





# cd name_of_directory = change directory
#ls = see all files expect files starting with .
#ls -a + see all files including files starting with .
# mkdir name_of_directory = make new directory
# rmdir name_of_directory = remove direcotry
# rm name_of_file = remove file
# python3 name_of_file.py = run file
#
