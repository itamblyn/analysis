#!/usr/bin/env python

import sys
import numpy
import Gnuplot, Gnuplot.funcutils

nband = input('Number of bands? ') 
#natom = 128  # old line
#nedos = 1001 # old line
natom = int(input('Number of atoms? '))
nedos = int(input('NEDOS? '))

print 'usage: ' + sys.argv[0] + ' input_filename(s)'

average_dos = numpy.zeros((nedos,2), dtype=float)

dos = numpy.zeros((nedos,2), dtype=float)

for i in numpy.arange(1, len(sys.argv)):

    input_filename = sys.argv[i]

    inputFile = open(input_filename, 'r')

    for j in range(nedos):
        line = inputFile.readline()
        for k in range(2):
            dos[j][k] = float(line.split()[k])
        idos = float(line.split()[2])

    normal = sum(dos)[1] 

    for j in range(nedos):

        dos[j][1] *= (2*float(nband)/(normal*float(natom)))

    average_dos += dos

########

average_dos /= float(len(sys.argv) - 1) 

gnuplot = Gnuplot.Gnuplot()

gnuplot('set title "DOS"')
gnuplot('set data style linespoints')
gnuplot('set yrange [0:*]')
gnuplot('set xrange [*:*]')
gnuplot.plot(average_dos)

raw_input('Press any key to continue\n')


def write_dos(average_dos):
    sum = 0.0

    outputFile = open('dos_average.dat', 'w')
    for row in average_dos:
        for element in row:
            outputFile.write(str(element) + ' ')
        sum += row[1]
        outputFile.write(str(sum) + ' ')
        outputFile.write('\n')
    outputFile.close()
    return

write_dos(average_dos) 
