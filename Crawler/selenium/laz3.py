from lxml import html
from selenium import webdriver
class HtmlGetter:
   def get_html(self, url):
       pass
class HtmlParseGetter(HtmlGetter):
   def __init__(self, subject):
       self.subject = subject
   def get_html(self, url):
       html_source = self.subject.get_html(url)
       html_element = html.fromstring(html_source)
       print(html_element)
       return html_element
class SeleniumHtmlGetter(HtmlGetter):
   def __init__(self, scroll_to_bottom=False):
       self.scroll_to_bottom = scroll_to_bottom
   def get_html(self, url):
       browser = webdriver.Chrome()
       browser.maximize_window()
       browser.get(url)
       html_source = browser.page_source
       return html_source
if __name__ == '__main__':
   url = 'https://tiki.vn/deal-hot?src=header_label&_lc=Vk4wMzQwMjAwMDM%253D&tab=now&page=1'
   html_getter = HtmlParseGetter(SeleniumHtmlGetter( ))
   html_tree = html_getter.get_html(url)
   for v in html_tree.xpath("//a[@class='List__Wrapper-sc-1ap7nsk-0 cEBRuU styles__FlashDealItemList-sc-1466pn8-4 hvXODY']"):
       print(v.xpath("./div[@class='styles__Wrapper-sc-6jfdyd-0 iNsGak']/text()"))
       print(v.xpath(".//span[@class='styles__OriginalPrice-sc-6jfdyd-4 kJlkgX']/text()"))
       print(v.xpath(".//div[@class='styles__DiscountedPrice-sc-6jfdyd-3 bXgYaR has-discount']/text()"))
       print('------------------------------\n')