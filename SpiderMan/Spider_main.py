import  html_outputer , html_parser, mySelenium
import time

class Spider_main(object):
    def __init__(self,video_url):
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.video_urls = video_url
        self.mySlelenium = mySelenium.mySelenium()

    def craw(self):
        count = 1
        for video_url in self.video_urls:
            print("craw %d:%s" % (count, video_url))
            try:
                soup = self.mySlelenium.craw_html(video_url)
                new_data = self.parser.parse(video_url,soup)
                self.outputer.collect_data(new_data)
            except:
                print ("craw failed")
            count += 1
        self.outputer.output_html()


if __name__ == "__main__":
    f = open("videoid.txt", encoding="utf-8")
    content = f.read()
    f.close()
    videoids = content.split('\n')

    video_url = []
    for videoid in videoids:
        video_url.append("https://www.iesdouyin.com/share/video/"+str(videoid)+
                         "/?u_code=hjdm8k44&region=CN&mid=6610679524466101005&schema_type=1&object_id="
                         "6610679501925911815&utm_campaign=client_scan_share&app=aweme&utm_medium=ios&tt_from=scan_share&iid=45561030398&utm_source=scan_share")

    obj_spider = Spider_main(video_url)
    obj_spider.craw()
