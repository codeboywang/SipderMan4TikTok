from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class mySelenium(object):
    def __init__(self):
        self.opts = Options()
        self.opts.add_argument("user-agent=['Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) ' \
                                                                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Mobile Safari/537.36']")

        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        self.DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/chromedriver")


    def craw_html(self,url):
        self.browser = webdriver.Chrome(executable_path=self.DRIVER_BIN, chrome_options=self.opts)
        self.browser.get(url)
        soup = BeautifulSoup(self.browser.page_source)
        self.browser.close()
        print("mySelenium craw successful！\n")
        return soup

# unexplainable failure
# headlines = browser.find_elements_by_name("shareTitle")
#
# for headline in headlines:
#     print(headline.get_attribute('innerHTML'))
#
# headline = browser.find_element_by_name("shareTitle")
# print(headline.get_attribute('innerHTML'))
