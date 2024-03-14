#!/usr/bin/env python3
import sys
import csv
for line in sys.stdin:
    fields = line.strip()
    fields =fields.split(",")
    package = fields[6]
    print('%s\t%s' % (package, 1))
