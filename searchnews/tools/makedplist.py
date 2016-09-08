#-*-coding:utf-8-*-
import sqlite3
import os

conn = sqlite3.connect('dplist.db')
print 'success'
conn.execute('''CREATE TABLE dplist
        (UNI  TEXT  PRIMARY KEY  NOT NULL,
        ID   TEXT    NOT NULL);''')
print 'success 2'

flag = False
dict = {}

for i in range(2001,2002):
    for j in range(1,13):
        for k in range(1,32):
            for l in range(0,50):
                if not os.path.exists('jiebawords/'+str(i)+str(j)+str(k)+str(l)+'.txt'):
                    print 'no'
                    break
                else:
                    global flag
                    fp = open('jiebawords/'+str(i)+str(j)+str(k)+str(l)+'.txt', 'r')
                    arr = []
                    ss = fp.read()
                    arr = eval(ss)
                    for aa in range(0, len(arr)):
                        if not dict.has_key(arr[aa][0]):
                            dict[arr[aa][0]] = str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l)
                        else:
                            dict[arr[aa][0]] += ','+str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l)
                    print str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l)
for mm in range(0,len(dict)):
    conn.execute("INSERT INTO dplist (UNI, ID) \
    VALUES (?, ?)", (dict.keys()[mm], dict.values()[mm]))
    print mm
conn.commit()
'''在此处进行对数据库的录入
    cursor = conn.execute("SELECT UNI, ID from dplist")
    conn.execute("UPDATE dplist set ID = ? where UNI=?", (row[1]+','+str(i)+str(j)+str(k)+str(l), row[0]))
    conn.commit()
    conn.execute("INSERT INTO dplist (UNI, ID) \
    VALUES (?, ?)", (arr[aa][0], str(i)+str(j)+str(k)+str(l)))'''

'''                        flag = False
                        for row in cursor:
                            if arr[aa][0] == row[0]:
                                flag = True
 
                                break
                                print ids
                        if not flag:'''
                        
                    
                    
