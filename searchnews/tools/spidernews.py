#-*-coding:utf-8-*-
import urllib
import urllib2
import re
import os
from pyquery import PyQuery as pq
import time

url = 'http://news.tsinghua.edu.cn/publish/thunews'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
headers = { 'User-Agent' : user_agent }
for i in range(2016,2017):
    for j in range(1,10):
        
        response = urllib2.urlopen('http://news.tsinghua.edu.cn/publish/thunews/newsCollections/d_'+str(i)+'_'+str(j)+'.json')
        print str(i)+'_'+str(j)
        f = file('json/' + str(i) + '_' + str(j) + '.json', 'w')
        f.write(response.read())
        time.sleep(1)
        '''print response.read()'''
