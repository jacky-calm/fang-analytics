#coding=utf-8
import urllib
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class PriceHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
    	for attr in attrs:
          print "     attr:", attr
        print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    

def getHtml(url):
  page = urllib.urlopen(url)
  html = page.read()
  return html

html = getHtml("http://sh.lianjia.com/ershoufang/rs%E9%BB%84%E6%B5%A6%E8%8A%B1%E5%9B%AD")
parser = PriceHTMLParser()
parser.feed(html)

