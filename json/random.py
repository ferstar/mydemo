#!/usr/bin/env python
# encoding: utf-8

import random

def blankReplace(a):
    s=str(a)[1:-1]
    while(s.find(' ')!=-1):
        s=s.replace(' ','')
    return s

file=open(r'E:\rand_data.txt','w')
for j in range(1000):
    data=[random.randint(0,3) for i in range(1000)]
    strdata=blankReplace(data)
    file.write('user'+str(j+1)+','+strdata+'\n')
file.close()