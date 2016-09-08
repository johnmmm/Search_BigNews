#-*-coding:utf-8-*-
import jieba
import jieba.posseg
from collections import Counter
import os
import codecs

fn = codecs.open('stop.txt', 'r', 'utf-8')
stopwords = fn.read().split('\n')
print stopwords

for i in range(2001,2017):
    for j in range(1,13):
        for k in range(1,32):
            for l in range(0,50):
                if not os.path.exists('txt/'+str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l)+'.txt'):
                    print 'no'
                    break
                else:
                    f = codecs.open('txt/'+str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l)+'.txt', 'r', 'utf-8')
                    s = f.read()
                    words = filter(lambda w:w not in stopwords and len(w)>1, jieba.cut_for_search(s))
                    count = Counter(words)
                    count = sorted(count.items(), key=lambda x:x[1], reverse=True)
                    o = open('jiebawords/'+str(i)+str(j)+str(k)+str(l)+'.txt', 'w')
                    pre = str(count)
                    o.write(pre)
                    '''for m in count:
                        o.write(m)
                        o.write("\n")'''
                    o.close()
                    
                
