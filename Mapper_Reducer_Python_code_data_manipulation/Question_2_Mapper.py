#!/usr/bin/env python3
import sys
import csv
for rows in sys.stdin:
    fields = rows.strip()
    fields =fields.split(",")
    country = fields[8]
    print('%s\t%s' % (country, 1))