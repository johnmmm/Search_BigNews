#-*-coding:utf-8-*-
import urllib
import urllib2
import re
import os
from HTMLParser import HTMLParser
import HTMLParser
import codecs
from lxml import etree
import sqlite3

text = ''
titext = ''
flag = False
flagt = False
flagh = True
flagh2 = False
tinum = 0

conn = sqlite3.connect('conlist.db')
print 'success'
conn.execute('''CREATE TABLE conlist
        (ID  TEXT  PRIMARY KEY  NOT NULL,
        TITLE  TEXT   NOT NULL,
        CONTENT   TEXT   NOT NULL,
        HREF   TEXT   NOT NULL);''')
print 'success 2'

class MyHTMLParser(HTMLParser.HTMLParser):
    def _init_(self):
        HTMLParser.HTMLParser._init_(self)
    def handle_starttag(self, tag, attrs):
        global flag
        global flagt
        global flagh
        global flagh2
        global tinum
        if tag == 'title':
            flagt = True
            if tinum == 0:
                tinum = 1
                flag = True
        if tag == 'p':
            flag = True
        if tag == 'h2':
            flagh2 = True
    def handle_data(self,data):
        global flag
        global flagt
        global flagh
        global flagh2
        global text
        global titext
        if flagh2:
            if flagh:
                if len(data) == 4:
                    flagh = False     
        if flag:
            if flagt:
                titext = data
            else:
                if flagh:
                    text += data[0:len(data)]
                    '''print len(data)
                    print data '''                 
    def handle_endtag(self,tag):
        global flag
        global flagt
        global flagh2
        if tag == 'title':
            flag = False
            flagt = False
        if tag == 'p':
            flag = False
        if tag == 'h2':
            flagh2 = False

for i in range(2001,2017):
    for j in range(1,13):
        for k in range(1,32):
            for l in range(0,50):
                if not os.path.exists('html/'+str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l)+'.html'):
                    print 'no'
                    break
                else:
                    f = codecs.open('html/'+str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l)+'.html','r','utf-8')
                    s = f.read()
                    parser = MyHTMLParser()
                    parser.feed(s)
                    conn.execute("INSERT INTO conlist (ID, TITLE, CONTENT, HREF) \
                    VALUES(?, ?, ?, ?)", (str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l), titext, text, ''))
                    print str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l)
                    text = ''
                    titext = ''
                    global tinum
                    global falgh
                    tinum = 0
                    flagh = True
conn.commit()
