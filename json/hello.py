#!/usr/bin/env python
# encoding: utf-8

file = open(r'./hello.txt','w')
for i in range(1000):
    s ='song'+str(i+1)+' float,'+'\n'
    file.write(s)
file.close()

