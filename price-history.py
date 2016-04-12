#coding=utf-8
import urllib
import re

def getHtml(url):
  page = urllib.urlopen(url)
  html = page.read()
  return html

html = getHtml("http://sh.lianjia.com/chengjiao/q5011000016922")

#print html

m = re.findall('<div class="div-cun">(.*?)<span>元/平</span></div>', html)

print m

m = re.findall('<div class="div-cun">(\d+-\d+-\d+)</div>', html)

print m

