#-*-coding:utf8-*-
from MyCrawlerLib.tools.Analyiser import Analysiser
from MyCrawlerLib.tools.HtmlTools import HtmlTools

class AnalysiserCreater(object):
    def __init__(self,url):
        self.analysiser = None
        self.createAnalysiser(url)

    def createAnalysiser(self,url):
        try:
            htmltool = HtmlTools()
            self.analysiser = Analysiser(htmltool.getByRequests(url))
        except:
            print("Create Analysiser Error--url:"+url)

