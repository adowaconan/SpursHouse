# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:07:26 2016

@author: ning
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import lxml.html

website= 'http://world.chinadaily.com.cn/node_1129342.htm'
webtoread=urlopen(website)
soup=BeautifulSoup(webtoread,"lxml")

links=[]
for link in soup.find_all('a'):
    h_link=link.get('href')
    links.append(h_link)
links=links[links.index('#'):]
#print(links)


def getUniqueWords(allWords) :
    uniqueWords = [] 
    for i in allWords:
        if not i in uniqueWords:
            uniqueWords.append(i)
    return uniqueWords
    
dictofwords={}
for items in links:
    try:
        #print(items)
        #print(dictofwords)
        url=items
        htmltree = lxml.html.parse(url)
        p_tags = htmltree.xpath('//p')
        p_content = [p.text_content() for p in p_tags]
        for i in range(len(p_content)):
            if '\n' in p_content:
                p_content.remove('\n')
        p_content=p_content[1:]
        #print(p_content)
        
        listofwords=[]
        for idx,line in enumerate(p_content):
            for item in line:
                listofwords.append(item)
        uniquelistofwords=getUniqueWords(listofwords)
        
        for item in uniquelistofwords:
            if item not in dictofwords:
                dictofwords[item]=0
    
        for key in dictofwords:
            for item in listofwords:
                if item == key:
                    dictofwords[key] += 1
        
    except:
        print(items,'no cant do')
        
        
