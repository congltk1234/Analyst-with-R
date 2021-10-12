from lxml import html
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HtmlGetter:

    def get_html(self, url):
        pass


class HtmlParseGetter(HtmlGetter):

    def __init__(self, subject):
        self.subject = subject

    def get_html(self, url):
        html_source = self.subject.get_html(url)
        html_element = html.fromstring(html_source)
        return html_element


class SeleniumHtmlGetter(HtmlGetter):
    def __init__(self, scroll_to_bottom=True):
        self.scroll_to_bottom = scroll_to_bottom

    def get_html(self, url):
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(url)

        if self.scroll_to_bottom:
            last = None
            for v in range(50):
                for k in range(5):
                    browser.find_element_by_xpath('//html').send_keys(Keys.DOWN)
                if last is not None and last == browser.execute_script('return window.pageYOffset;'):
                    break
                last = browser.execute_script('return window.pageYOffset;')

        html_source = browser.page_source
        browser.quit()
        return html_source


if __name__ == '__main__':
    url = 'https://tiki.vn/deal-hot?src=header_label&_lc=Vk4wMzQwMjAwMDM%253D&tab=now&page=1'
    html_getter = HtmlParseGetter(SeleniumHtmlGetter( ))
    html_tree = html_getter.get_html(url)
    count=0
    fieldnames = ['index', 'Product', 'Price', 'Discount', 'Available']
    with open('tiki.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
    for v in html_tree.xpath("//div[@class='styles__Wrapper-sc-6jfdyd-0 iNsGak']"):
        count+=1
        i={}
        i['index']=count
        i['Product']=v.xpath(".//div[@class='styles__ProductTitle-sc-6jfdyd-2 dxIljm']/text()").pop()
        i['Price']=v.xpath(".//div[@class='styles__DiscountedPrice-sc-6jfdyd-3 bXgYaR has-discount']/text()").pop()
        i['Discount']=v.xpath(".//div[@class='styles__DiscountPercentage-sc-6jfdyd-5 jWksYr']/text()").pop()
        #print(v.xpath("./div[@class='image']//img/@src"))
        i['Available']=v.xpath(".//div[@class='content']/p/text()").pop()
        with open('tiki.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(i)

        