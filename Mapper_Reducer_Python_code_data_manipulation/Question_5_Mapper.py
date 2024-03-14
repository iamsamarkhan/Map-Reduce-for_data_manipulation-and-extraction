#!/usr/bin/env python3
import sys
import csv
for line in sys.stdin:
    fields = line.strip()
    fields =fields.split(",")
    r_os=fields[5]
    print('%s\t%s' % (r_os, 1))