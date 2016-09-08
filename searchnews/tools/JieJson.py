#-*-coding:utf-8-*-
import urllib
import urllib2
import re
import os
from pyquery import PyQuery as pq
import time
import json

for i in range(2001,2017):
    for j in range(1,13):
        f = file('json/' + str(i) + '_' + str(j) + '.json', 'r')
        s = f.read()
        arr = json.loads(s)
        for k in range(1,32):
            if arr["data"].has_key(str(k)) == True:
                '''print "Value : %s" % arr["data"].has_key(str(k))
                print k'''
                for l in range(0,len(arr["data"][str(k)])):
                    name = "http://news.tsinghua.edu.cn/"+arr["data"][str(k)][l]["htmlurl"]
                    print str(i) + '_' + str(j) + '_' + str(k) + '_' + str(l)
                    print name
                    if name[-10:-5] == "index":
                        print "empty"
                    else:
                        response = urllib2.urlopen(name[0:-5]+"_.html")
                        m = file('html/' + str(i) + '_' + str(j) + '_' + str(k) + '_' + str(l) + '.html', 'w')                      
                        m.write(response.read())

        
