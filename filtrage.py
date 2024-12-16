#!/usr/bin/python2

import csv 
import sys 

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t', quotechar='"',quoting = csv.QUOTE_ALL)
for line in reader: 
    i = line[4]
    if not (len(i)==0 or (i.count('.') +    i.count('!') + i.count('?')) > 1):
        writer.writerow(line)