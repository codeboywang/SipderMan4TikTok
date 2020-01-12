class HtmlOutputer(object):

    def __init__(self):
        self.data = []

    def collect_data(self,data):
        print ('in html_outputer def collect_data')
        if data is None:
            return
        self.data.append(data)

    def output_html(self):
        print ('in html_outputer def output_html')

        font = open('output.txt', 'w',encoding = "utf-8")

        # ASCII
        count = 1
        for data in self.data:
            font.write("No."+str(count)+"\n")
            try:
                font.write("UerName: " + data['user']+"\n")
            except:
                print("no Title")
                pass
            try:
                font.write("Describe: " + data['describe']+"\n")
            except:
                print("no Describe")
                pass
            try:
                font.write("VideoUrl: " + data['url']+"\n")
            except:
                print("no url")
                pass
            try:
                font.write("Likes: " + data['like']+"\n")
            except:
                print("no like")
                pass
            try:
                font.write("Comments: " + data['comment']+"\n")
            except:
                print("no comment")
                pass
            font.write("-----------------\n")
            count += 1
