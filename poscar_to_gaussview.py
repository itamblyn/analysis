#! /usr/bin/env python

import sys

print 'usage: ' + sys.argv[0] + ' filename' 

inputFilename = sys.argv[1]

############################
#############################
                            ##
num_x_trans = 1             ##
num_y_trans = 1             ##
num_z_trans = 1             ##
                            ##
#############################
############################

dim = 3


import sys
import numpy

inputFile = open(inputFilename, 'r')

element_name = []

for element in inputFile.readline().split():

    element_name.append(element)

print element_name

lattice_constant = float(inputFile.readline())

string = inputFile.readline().split()
a1 = numpy.array([float(string[0]),float(string[1]),float(string[2])]) 
string = inputFile.readline().split()
a2 = numpy.array([float(string[0]),float(string[1]),float(string[2])]) 
string = inputFile.readline().split()
a3 = numpy.array([float(string[0]),float(string[1]),float(string[2])]) 

string = inputFile.readline()

element_natom = []

for element in string.split():

    element_natom.append(int(element))

natom = sum(element_natom)

inputFile.readline()    # skip "Direct"

basis_atoms = numpy.zeros((natom, dim), dtype=numpy.float)

for i in range(natom):
    string = inputFile.readline().split()
    for j in range(dim):
        basis_atoms[i][j] = float(string[j]) 

lattice = []

for i in range(num_x_trans):
     for j in range(num_y_trans):
          for k in range(num_z_trans):
               for l in range(len(basis_atoms)):
                    lattice.append(i*a1 + j*a2 + k*a3 + basis_atoms[l][0]*a1 + basis_atoms[l][1]*a2 + basis_atoms[l][2]*a3)

filename = 'xred.dat'
filenameGaussview = 'POSCAR.gjf'

outputFile = open(filename,'w')
outputFileGaussview = open(filenameGaussview,'w')

outputFileGaussview.write('%chk=checkpoint.chk \n')
outputFileGaussview.write('%mem=1GB \n')
outputFileGaussview.write('%nproc=4 \n')
outputFileGaussview.write('#pbepbe/3-21g/auto \n')
outputFileGaussview.write('\n')
outputFileGaussview.write('Title Card \n')
outputFileGaussview.write('\n')
outputFileGaussview.write('0 1\n')

counter = 0
atom_name = 0

for natom in element_natom: 

    for i in range(natom):

        xcart = lattice_constant*lattice[counter][0]
        ycart = lattice_constant*lattice[counter][1]
        zcart = lattice_constant*lattice[counter][2]


        outputFile.write(' ' + repr(xcart) + '   ' + repr(ycart) + '   ' + repr(zcart) + '\n')
        outputFileGaussview.write(str(element_name[atom_name]) + ' ' + repr(xcart) + '   ' + repr(ycart) + '   ' + repr(zcart) + '\n')

        counter = counter + 1
    atom_name = atom_name + 1

a1 = lattice_constant*a1
a2 = lattice_constant*a2
a3 = lattice_constant*a3
 
outputFileGaussview.write('Tv ' + str(a1[0]) + ' ' + str(a1[1]) + ' ' + str(a1[2]) + '\n')
outputFileGaussview.write('Tv ' + str(a2[0]) + ' ' + str(a2[1]) + ' ' + str(a2[2]) + '\n')
outputFileGaussview.write('Tv ' + str(a3[0]) + ' ' + str(a3[1]) + ' ' + str(a3[2]) + '\n')

outputFile.close()
outputFileGaussview.close()

