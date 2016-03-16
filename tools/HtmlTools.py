#-*-coding:utf8-*-
import requests
from urllib import request

class HtmlTools:
    def __init__(self):
        self._head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}

    def getByUrllib(self,url):
        try:
            webPage = request.urlopen(url)
            html = webPage.read()
            return html
        except:
            return None
    def getByRequests(self,url):
        try:
            webPage = requests.get(url, headers=self._head)
            html = webPage.text
            return html
        except:
            return None





if __name__ == '__main__':
    url = "http://tieba.baidu.com/home/main?un=怪怪盗鲁邦&fr=ibaidu&ie=utf-8"
    url2 = "http://tieba.baidu.com/home/main?un=他未走灬&fr=ibaidu&ie=utf-8"
    tool = HtmlTools()
    h1 = tool.getByRequests(url)
    h2 = tool.getByUrllib(url2)
    print(h1)