#-*-coding:utf-8-*-
import urllib
import urllib2
import re
import os
from pyquery import PyQuery as pq
import time
import json
import sqlite3

conn = sqlite3.connect('conlist.db')
print 'success'
conn.close()

for i in range(2001,2017):
    for j in range(1,13):
        if not os.path.exists('json/' + str(i) + '_' + str(j) + '.json'):
            print 'no'
            continue;
        f = file('json/' + str(i) + '_' + str(j) + '.json', 'r')
        s = f.read()
        arr = json.loads(s)
        for k in range(1,32):
            if arr["data"].has_key(str(k)) == True:
                for l in range(0,len(arr["data"][str(k)])):
                    name = "http://news.tsinghua.edu.cn/"+arr["data"][str(k)][l]["htmlurl"] 
                    if name[-10:-5] == "index":
                        print "empty"
                    else:
                        cursor = conn.execute("SELECT ID, HREF from conlist")
                        conn.execute("UPDATE conlist set HREF = ? where ID = ?", (name, str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l)))
                        print str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l)
                        conn.commit()

