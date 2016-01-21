# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:07:26 2016

@author: ning
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import lxml.html
url='http://world.chinadaily.com.cn/2015-12/01/content_22593520.htm'#chageable url
htmltree = lxml.html.parse(url)
p_tags = htmltree.xpath('//p')
p_content = [p.text_content() for p in p_tags]
for i in range(len(p_content)):
    if '\n' in p_content:
        p_content.remove('\n')
p_content=p_content[1:]

def getUniqueWords(allWords) :
    uniqueWords = [] 
    for i in allWords:
        if not i in uniqueWords:
            uniqueWords.append(i)
    return uniqueWords
    
listofwords=[]
for idx,line in enumerate(p_content):
    for item in line:
        listofwords.append(item)
uniquelistofwords=getUniqueWords(listofwords)
dictofwords={}
for item in uniquelistofwords:
    dictofwords[item]=0
    
for key in dictofwords:
    for item in listofwords:
        if item == key:
            dictofwords[key] += 1
    

