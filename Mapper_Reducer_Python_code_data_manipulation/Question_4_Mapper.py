#!/usr/bin/env python3
import sys
import csv
package=None
for rows in sys.stdin:
    fields = rows.strip()
    fields =fields.split(",")
    country=fields[8]
    if country == '"IE"':
        package = fields[6]
        print('%s\t%s' % (package, 1))