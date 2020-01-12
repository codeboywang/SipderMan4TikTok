from bs4 import BeautifulSoup
class HtmlParser(object):

    def _get_new_data(self,page_url, soup):
        print ('in parse def _get_new_data')
        res_data = {}
        #url
        res_data['url'] = page_url

        tmp = soup.find_all("p", class_="count")
        tmp1 = soup.find("p", class_="bottom-user")
        tmp2 = soup.find("p", class_="bottom-desc")

        try:
            res_data['like'] = tmp[0].get_text()
        except:
            print("get like fail")
            pass

        try:
            res_data['comment'] = tmp[1].get_text()
        except:
            print("get comment fail")
            pass

        try:
            res_data['user'] = tmp1.get_text()
        except:
            print("get title fail")
            pass

        try:
            res_data['describe'] = tmp2.get_text()
        except:
            print("get describe fail")
            pass

        print ('get_over')
        return res_data

    def parse(self,page_url,soup):
        print ("in html_parser def parse")
        new_data = self._get_new_data(page_url,soup)
        print ('paser pver')
        return new_data


