#! /usr/bin/env python

import sys
import commands
import numpy

print 'usage: ' + sys.argv[0] + ' input_filename'

input_filename = sys.argv[1]

command_line_counter = commands.getoutput('wc -l ' + input_filename).split()

if len(command_line_counter) != 2:
    print 'Error determining file size'
else:
    number_of_lines = int(command_line_counter[0])


outputFile = open('dos_md.dat', 'w')

inputFile = open(input_filename, 'r')

for i in range(5):       # skips header
    inputFile.readline()

inline = inputFile.readline()

emax = float(inline.split()[0])
emin = float(inline.split()[1])
enum = int(inline.split()[2])
efermi = float(inline.split()[3]) # should i be subtracting this off?

number_of_configurations = (number_of_lines - 5)/(enum + 1)

print number_of_configurations

dos = numpy.zeros((enum, 3), dtype = numpy.float) # E, dos, idos

for j in range(enum):
    inline_total = inputFile.readline().split()
    dos[j][0] = float(inline_total[0]) 
    dos[j][1], dos[j][2] = float(inline_total[1]), float(inline_total[2])

for row in dos:
    for element in row:
        outputFile.write(str(element) + ' ')
    outputFile.write('\n')

