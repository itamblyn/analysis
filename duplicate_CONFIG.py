#! /usr/bin/python

# Read in a text file and write out an identical text file
# Seems useless... BUT IT ISN'T

import os, sys

FILE = 'CONFIG'
f = open(FILE,'r')
#lines = f.readlines()
g = open('CONFIG_DUPLICATE','w')
#for line in lines:
#    g.write(line)

header = f.readline()
n,m = f.readline().split()
a1,a2,a3 = f.readline().split()
b1,b2,b3 = f.readline().split()
c1,c2,c3 = f.readline().split()

g.write(header)
g.write('         '+n+'         '+m+'\n')
g.write('         '+a1+'        '+a2+'        '+a3+'\n')
g.write('         '+b1+'        '+b2+'        '+b3+'\n')
g.write('         '+c1+'        '+c2+'        '+c3+'\n')

natoms = 1080
for i in range(natoms):
    atom_name, atom_index = f.readline().split()
    atom_name_line = atom_name+'              '+atom_index+'\n'
    atom_x,atom_y,atom_z = f.readline().split()
    atom_xyz = '    '+atom_x+'        '+atom_y+'        '+atom_z+'\n'

    g.write(atom_name_line)
    g.write(atom_xyz)

f.close()
g.close()
