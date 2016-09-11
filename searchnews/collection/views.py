from django.shortcuts import render
from django.shortcuts import get_object_or_404
import sqlite3
import jieba
import jieba.posseg
from collections import Counter
import os
import json
import codecs

keys = ''

def index(request):
    return render(request, 'index.html')

def query(request):
    query_words = request.POST['q'].strip().split(' ')
    
    qwords = []
    dict={}
    fn = codecs.open('stop.txt', 'r', 'utf-8')
    stopwords = fn.read().split('\n')
    for aa in range(0, len(query_words)):
        words = jieba.cut_for_search(query_words[aa])
        qwords += words

    keywords = qwords[0]
    for bb in range(1, len(qwords)):
        keywords += '_' + qwords[bb]
    dict['keywords']=keywords
    global keys
    keys=keywords

    results = []
    num1 = []
    numn = []
    flag = 0
    newnum = 0
    conn = sqlite3.connect('dplist.db')
    for aa in range(0, len(qwords)):
        cursor = conn.cursor()
        cursor.execute('SELECT * from dplist where UNI = ?', (qwords[aa],))
        for item in cursor:
            if len(qwords) == 1:
                idss = item[1].split(',')
                for bb in range(0, len(idss)):
                    numn.append(idss[bb])
            if not len(qwords) == 1:
                idss = item[1].split(',')
                if not flag == 0:
                    numn = set(idss)&set(num1)
                if flag == 0: 
                    num1 = idss                 
                    flag = 1                                   
        cursor.close()
    conn.close()
    conn = sqlite3.connect('conlist.db')
    numn = list(numn)
    for aa in range(0, len(numn)):
        cursor = conn.cursor()
        cursor.execute('SELECT * from conlist where ID = ?', (numn[len(numn)-1-aa],))
        for item in cursor:
            lists = item[0].split('_')
            newnum += 1
            results.append({'title':item[1], 'id':item[0], 'time':lists[0]+'.'+lists[1]+'.'+lists[2], 'keywords':keywords})
        cursor.close()
        if newnum > 540:
            break
    conn.close()
    return render(request, 'query.html', { 'results':results, 'dict': json.dumps(dict) })
def news(request):
    id_ = request.path.split('/')[2]
    page = {}
    conn = sqlite3.connect('conlist.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * from conlist where ID = ?', (id_,))
    for item in cursor:        
        page['title'] = item[1]
        page['content'] = item[2]
        page['refs'] = item[3][0:-5]+'_.html'
    global keys
    dict={}
    dict['keywords']=keys
    return render(request, 'news.html', { 'page':page, 'dict': json.dumps(dict) })
