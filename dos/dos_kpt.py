#! /usr/bin/env python

import numpy
from eigenvalue_read import read_eigenvalues
import scipy.special
import pylab
import random
import sys
import Gnuplot, Gnuplot.funcutils

print 'Warning, this code is obsolete (and is probably incorrect)!!! Use the fortran version.'

eigenvalue_list = read_eigenvalues()

#for i in range(len(eigenvalue_list)):
#    eigenvalue_list[i] = random.random()

emin = min(eigenvalue_list)
emax = max(eigenvalue_list)
nedos = 301

dE = (emax - emin)/nedos
print dE

sigma = 0.2

dos = numpy.zeros((3,nedos), dtype=float)

for i in range(nedos):

    E = i*dE + emin    # this is the lower value

    for eigenvalue in eigenvalue_list:

        dos[0][i] += -(1.0/2.0)*numpy.sqrt(0.5*sigma)*numpy.sqrt(numpy.pi)*scipy.special.erf((eigenvalue - (E + dE))/(numpy.sqrt(0.5*sigma))) - -(1.0/2.0)*numpy.sqrt(0.5*sigma)*numpy.sqrt(numpy.pi)*scipy.special.erf((eigenvalue - E)/(numpy.sqrt(0.5*sigma)))
        dos[1][i] += -(1.0/2.0)*numpy.sqrt(1.0*sigma)*numpy.sqrt(numpy.pi)*scipy.special.erf((eigenvalue - (E + dE))/(numpy.sqrt(1.0*sigma))) - -(1.0/2.0)*numpy.sqrt(1.0*sigma)*numpy.sqrt(numpy.pi)*scipy.special.erf((eigenvalue - E)/(numpy.sqrt(1.0*sigma)))
        dos[2][i] += -(1.0/2.0)*numpy.sqrt(2.0*sigma)*numpy.sqrt(numpy.pi)*scipy.special.erf((eigenvalue - (E + dE))/(numpy.sqrt(2.0*sigma))) - -(1.0/2.0)*numpy.sqrt(2.0*sigma)*numpy.sqrt(numpy.pi)*scipy.special.erf((eigenvalue - E)/(numpy.sqrt(2.0*sigma)))

gnuplot = Gnuplot.Gnuplot()

gnuplot('set title "DOS"')
gnuplot('set data style linespoints')
gnuplot('set yrange [*:*]')
gnuplot('set xrange [*:*]')
gnuplot.plot(dos[0],dos[1], dos[2])

raw_input('Press any key to continue\n')

outputFile = open('dos_kpt.dat', 'w')
outputFile.write('# E, sigma/2.0, sigma, sigma*2.0 \n')

for i in range(nedos):

    E = i*dE + emin + dE/2
    outputFile.write(str(E) + ' ' + str(dos[0][i]) + ' ' + str(dos[1][i]) + ' ' + str(dos[2][i]) + '\n')

outputFile.close()
