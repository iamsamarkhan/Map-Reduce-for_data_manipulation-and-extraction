#!/usr/bin/env python3
from operator import itemgetter
import sys
current_key=None
current_count=0
key=None
order=[]
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
        if current_key:
            order.append([current_count,current_key])
        current_count=count
        current_key=key
print("The top 10 package used are given below")
if current_key==key:
    order.append([current_count,current_key])
sorted_reverse_list=sorted(order, reverse=True)
for i in range(10):
    print(sorted_reverse_list[i][1])