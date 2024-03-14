#!/usr/bin/env python3
from operator import itemgetter
import sys
current_key=None
current_count=0
key=None
h_count=0
h_rOs=None
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
            h_rOs=current_key
        current_count=count
        current_key=key
if h_rOs=='"mingw32"':
    print (h_rOs)
    print(" The above os is WINDOWS OS")
else:
    print(h_rOs,)
    print("The above os is MAC OS")