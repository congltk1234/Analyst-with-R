from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome()

url = "https://www.lazada.vn/laptop/"
driver.get(url)
time.sleep(3)

elements = driver.find_elements_by_css_selector("._8JShU")
product_name = [el.text for el in elements]
link = [el.get_attribute("href") for el in elements]
elements = driver.find_elements_by_css_selector(".LY2Vk")
price = [el.text for el in elements]
sale = driver.find_elements_by_css_selector(".Urvyd")

print(sale)
