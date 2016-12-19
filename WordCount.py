# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:07:26 2016

@author: ning
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
<<<<<<< HEAD
import csv
import pandas as pd
from itertools import chain
from requests import get
import numpy as np
from collections import Counter
print('start')
website= 'http://history.sina.com.cn/news/list/20.shtml'
=======
import urllib
import lxml.html

website= 'http://world.chinadaily.com.cn/node_1129342.htm'
>>>>>>> origin/master
webtoread=urlopen(website)
soup=BeautifulSoup(webtoread,"lxml")
T=soup.find_all('div',{'id':'main'})
Q = list(T)
R = Q[0]
S=R.find_all('script',{'type':'text/javascript'})
U = S[2]
V = list(U)
V=str(V).split('"url"')
links=[]
<<<<<<< HEAD
gatepass = True
for lines in V:
    try:
        #print(lines)
        links.append(lines[2:54])
    except:
        pass
links=pd.DataFrame(links)
links.columns=['links']
import time  
def readurl(url):
    starttime = time.time()
    while time.time() < starttime + 60:
        webtoread=urlopen(url);print('reading',end=',')
        soup = BeautifulSoup(webtoread,'lxml')
        return soup
=======
for link in soup.find_all('a'):
    h_link=link.get('href')
    links.append(h_link)
links=links[links.index('#'):]
#print(links)

>>>>>>> origin/master

cnt =1;p=[]
dictofwords={}
remove_targets='abcdefghijklmnopqrstuvxwyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ#,.{};"~/\@():+-_<>[], ：”“=$、&|┊▼。？，（）\\%《》, ﹒?～［］'
remove_targets=list(remove_targets)
for rows in links['links']:
    
    print(cnt)
    url = rows
    cnt += 1
    
    try:
        print('start to parse words')
        soup=readurl(url)
        if soup is None:
            print('timeout')
            pass
        print('done soup')    
        p=soup.get_text();
        
        for item in remove_targets:
            p.replace(item,'')
        p=p.replace('\n','');p=p.replace('\t','');p=p.replace('\r','')
        p=list(chain(p))
        print('done chain')
        
    except:
        
        print('cannot put in list')
        pass
    print('len of p',len(p))
    print('start dict')
    for words in p:
        try:
            dictofwords[words] +=1
        except:
            dictofwords[words] = 1
    p=[]    
    
import json
json.dump(dictofwords,open("dictofwords.txt",'w'))
input('type go on')


for item in remove_targets:
    try:
        del dictofwords[item]
    except:
        pass

some_target = '\xa0'
del dictofwords[some_target]
some_target='\u3000'
del dictofwords[some_target]
some_target='…'
del dictofwords[some_target]
some_target="’"
del dictofwords[some_target]
some_target='\u200b'
del dictofwords[some_target]
some_target='；'
del dictofwords[some_target]
some_target="'"
del dictofwords[some_target]
some_target="·"
del dictofwords[some_target]
some_target='】'
del dictofwords[some_target]
some_target='丨'
del dictofwords[some_target]
some_target='＂'
del dictofwords[some_target]

#print(len(dictofwords))
frequency =int(input('frequency: '))
wordstolearn=list({ key:value for key, value in dictofwords.items() if value >frequency}.keys())
print(wordstolearn)

input('type "end" to end the section')