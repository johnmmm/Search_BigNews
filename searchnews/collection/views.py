from django.shortcuts import render
from django.shortcuts import get_object_or_404
import sqlite3

def index(request):
    return render(request, 'index.html')

def query(request):
    query_words = request.POST['q'].strip().split(' ')
    results = []
    num1 = []
    numn = []
    flag = 0
    conn = sqlite3.connect('dplist.db')
    for aa in range(0, len(query_words)):
        cursor = conn.cursor()
        cursor.execute('SELECT * from dplist where UNI = ?', (query_words[aa],))
        for item in cursor:
            if len(query_words) == 1:
                idss = item[1].split(',')
                for bb in range(0, len(idss)):
                    numn.append(idss[bb])
            if not len(query_words) == 1:
                idss = item[1].split(',')
                if not flag == 0:
                    for bb in range(0, len(idss)):
                        if idss[bb] in num1:
                            if not idss[bb] in numn:
                                numn.append(idss[bb])
                if flag == 0:                  
                    for bb in range(0, len(idss)):
                        num1.append(idss[bb])
                        flag = 1                                   
        cursor.close()
    conn.close()
    conn = sqlite3.connect('conlist.db')
    for aa in range(0, len(numn)):
        cursor = conn.cursor()
        cursor.execute('SELECT * from conlist where ID = ?', (numn[len(numn)-1-aa],))
        for item in cursor:
            results.append({ 'title':item[1], 'id':item[0]})
        cursor.close()
    conn.close()
    return render(request, 'query.html', { 'results':results })
def news(request):
    id_ = request.path.split('/')[2]
    page = {}
    conn = sqlite3.connect('conlist.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * from conlist where ID = ?', (id_,))
    for item in cursor:        
        page['title'] = item[1]
        page['content'] = item[2]
        page['refs'] = item[3]
    return render(request, 'news.html', { 'page':page })
