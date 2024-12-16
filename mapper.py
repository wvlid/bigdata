#!/usr/bin/python2
import csv 
import sys 

a = []
b = []

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimeter='\t', quotechar='"',quoting = csv.QUOTE_ALL)

for line in reader: 
    if len(line[4]==0):
        continue
    else: 
        a.append(line)
#sort  by the longest body 
sort_a = sorted(a, key=lambda a: len(a[4]), reverse = True)

#Take 10 first longest body 
for i in range(0,10): 
    b.append(sort_a[i])
for bl in b: 
    writer.writerow(bl)
