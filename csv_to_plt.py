#!/bin/python
from optparse import OptionParser
usage = ''
parser = OptionParser(usage)
parser.add_option('--i', type='string', dest='filename', default='junk.csv')

(options, args) = parser.parse_args()

filename = options.filename

f = open(filename, 'r')
lines = f.readlines()
f.close()

lines.pop(0)
outfile = filename.replace('csv','plt')
f = open(outfile, 'w')
for line in lines:
    string = (line.replace(","," ")).replace('\n', '')
    f.write(string)
f.close()
