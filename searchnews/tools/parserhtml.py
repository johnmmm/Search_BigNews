#-*-coding:utf-8-*-
import urllib
import urllib2
import re
import os
from HTMLParser import HTMLParser
import HTMLParser
import codecs
from lxml import etree

text = ''
flag = False
flagt = False
flagh = True
flagh2 = False
tinum = 0


'''removeImg = re.compile('<img.*?>| {7}|')
removeAddr = re.compile('<a.*?>|</a>')
replaceLine = re.compile('<tr>|<div>|</div>|</p>')
replaceTD = re.compile('<td>')
replace = Para = re.compile('<p.*?>')
replaceBR = re.compile('<br><br>|<br>')
removeExtraTag = re.compile('<.*?>')'''
def replace(x):
    x = re.sub('<img.*?>| {7}|',"",x)
    x = re.sub('<a.*?>|</a>',"",x)
    x = re.sub('<tr>|<div>|</div>|</p>',"\n",x)
    x = re.sub('<td>',"\t",x)
    x = re.sub('<p.*?>',"\n    ",x)
    x = re.sub('br><br>|<br>',"\n",x)
    x = re.sub('<.*?>',"",x)
    return x.strip()

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
        if flagh2:
            if flagh:
                if len(data) == 4:
                    flagh = False     
        if flag:
            if flagt:
                text += data[0:len(data)]+'\n'
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
                    o = codecs.open('txt/'+str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l)+'.txt', 'w', 'utf-8')
                    '''text = replace(text)'''
                    print str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l)
                    o.write(text)
                    o.flush()
                    text = ''
                    global tinum
                    global falgh
                    tinum = 0
                    flagh = True
