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
