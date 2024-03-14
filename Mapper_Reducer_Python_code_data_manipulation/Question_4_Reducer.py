#!/usr/bin/env python3
from operator import itemgetter
import sys
current_key=None
current_count=0
key=None
h_count=0
h_package=None
for line in sys.stdin:
    line= line.strip()
    key,count=line.split('\t',1)
    try:
        count=int(count)
    except ValueError:
        continue
    if current_key==key:
        current_count +=count
    else:
        if current_count>h_count:
            h_count=current_count
            h_package=current_key
        current_count=count
        current_key=key

print("The most popular package in Ireland is given below ")
print (h_package)