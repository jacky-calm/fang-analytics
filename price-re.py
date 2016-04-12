#coding=utf-8
import urllib
import re

def getHtml(url):
  page = urllib.urlopen(url)
  html = page.read()
  return html

html = getHtml("http://sh.lianjia.com/ershoufang/rs%E9%BB%84%E6%B5%A6%E8%8A%B1%E5%9B%AD")

#print html

m = re.findall('<div class="price-pre">(.*?)元/平</div>', html)

print m


