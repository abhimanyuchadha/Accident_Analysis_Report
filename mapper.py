#!/usr/bin/env python
import sys
import csv


with sys.stdin as csvfile:
    reader = csv.reader(csvfile, delimiter =',')
    reader.next()
    for line in reader:
        line = line[-5:]
        filteredLine = filter(None, line)
        for items in filteredLine:
            print '%s\t%s' % (items,1)
