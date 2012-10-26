#! /usr/bin/env python

import numpy, matplotlib, pylab, sys

inputFile = open ('bands.out','r')

BAND_array = []
for line in inputFile.readlines():
     for i in line.split():
          BAND_array.append(float(i))
inputFile.close()

inputFile = open ('fermi.out','r')

FERMI_array = []
for line in inputFile.readlines():
     for i in line.split():
          FERMI_array.append(float(i))
inputFile.close()

print 'input read complete'

nbands = len(BAND_array)/len(FERMI_array)

print nbands

BAND_array = numpy.reshape(BAND_array,( len(BAND_array) ))

i = 0

while i < len(BAND_array):
     BAND_array[i] -= FERMI_array[i/nbands]
     i +=1

pylab.hist(BAND_array, 250, 1)
pylab.axis([-4,2.0,0,1.6])

pylab.savefig(sys.argv[1])
