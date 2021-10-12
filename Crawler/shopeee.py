from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome()
url = "https://tiki.vn/deal-hot"
driver.get(url)
time.sleep(3)
elements = driver.find_elements_by_css_selector(".styles__ProductTitle-sc-6jfdyd-2")
product = [el.text for el in elements]
elements = driver.find_elements_by_css_selector('.styles__OriginalPrice-sc-6jfdyd-4')


sale = [el.text for el in elements]
elements = driver.find_elements_by_css_selector(".styles__DiscountedPrice-sc-6jfdyd-3")
price = [el.text for el in elements]

print(sale)

item = {'Sản phẩm':product, 'Giá gốc':sale, 'Price':price}
import pandas as pd

a = pd.DataFrame.from_dict(item)
print(a.head())