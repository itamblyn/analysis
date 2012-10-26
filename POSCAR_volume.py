#! /usr/bin/env python

import numpy
import sys
bohr = 0.529177


inputFile = open(sys.argv[1], 'r')

inputFile.readline()    # skips header

acell = float(inputFile.readline())

matrix = numpy.zeros((3,3), dtype=float)

for i in range(3):
    line = inputFile.readline()
    for j in range(3):
        matrix[i][j] = float(line.split()[j])*acell

V = numpy.abs(numpy.linalg.det(matrix))/bohr**3   # total cell volume in bohr^3

print 'Volume: ', V, ' bohr^3'

natom = float(inputFile.readline())

v = V/natom                                       # volume/ion in bohr

rs = ((3*v)/(4*numpy.pi))**(1./3.)                # rs, in bohr

print 'rs: ', rs
