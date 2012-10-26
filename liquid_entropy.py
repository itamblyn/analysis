#!/usr/bin/env python

import sys
import numpy
from scipy import integrate
import Gnuplot, Gnuplot.funcutils

print 'usage: ' + sys.argv[0] + ' RDF.dat'

inputFile = open(sys.argv[1], 'r')

r_array = []
gr_array = []

for line in inputFile.readlines():

    r_array.append(float(line.split()[0]))
    gr_array.append(float(line.split()[1]))

rsize = r_array[-1] - r_array[-2]
rmax = r_array[-1]

for i in range(10):
    r_array.append(rmax + (i+1)*rsize)
    gr_array.append(1.0)

r_array = numpy.array(r_array, dtype=float)
gr_array = numpy.array(gr_array, dtype=float)

integrand_array = numpy.zeros(len(r_array), dtype=float)

for i in range(len(r_array)):
    r = r_array[i]
    gr = gr_array[i]
    if gr != 0:  integrand_array[i] = (r**2)*gr*numpy.log(gr)
    else: integrand_array[i] = 0

plot_gr = numpy.zeros((len(r_array),2), dtype=float)
plot_integrand = numpy.zeros((len(r_array),2), dtype=float)

for i in range(len(r_array)):
    plot_gr[i][0], plot_gr[i][1] = r_array[i],gr_array[i]
    plot_integrand[i][0], plot_integrand[i][1] = r_array[i],integrand_array[i]

gnuplot = Gnuplot.Gnuplot()
gnuplot('set title "entropy"')
gnuplot('set data style lines')
gnuplot('set yrange [*:*]')
gnuplot('set xrange [*:*]')
gnuplot.plot(plot_gr)
raw_input('Press any key to continue\n')
gnuplot.plot(plot_integrand)
raw_input('Press any key to continue\n')

trapz = integrate.trapz(integrand_array, r_array)
simps = integrate.simps(integrand_array, r_array)

print trapz, simps
