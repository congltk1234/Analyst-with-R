from selenium import webdriver
PATH = 'chromedriver.exe'
from selenium.webdriver.common.keys import Keys
user_name="suthanhcong172@gmail.com"
password = 'Stc170202'
driver = webdriver.Chrome(PATH)
driver.get('https://www.facebook.com')
email=driver.find_element_by_id('email')
passwd = driver.find_element_by_id('pass')
email.send_keys(user_name)
passwd.send_keys(password)
passwd.send_keys(Keys.RETURN)