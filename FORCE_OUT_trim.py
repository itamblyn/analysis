#! /usr/bin/env python

import sys
import numpy

print 'usage: ' + sys.argv[0] + ' filename' 

inputFilename = sys.argv[1]

inputFile = open(inputFilename, 'r')

a = []

for line in inputFile.readlines():
    a.append([float(line.split()[0]),float(line.split()[1])])

a = numpy.array(a)

outputFile = open('potential.dat', 'w')

for i in range(len(a)-3):

    if a[i+1][1] != a[i][1]: outputFile.write(str(a[i+3][0]) + ' ' + str(a[i+3][1]) + '\n')

