#! /usr/bin/python

""" Script to convert the XDATCAR output file from VASP into xyz format. """

import os, sys, commands

global FNAME
global ATOM
global NATOM
global HEADER_LINES

FNAME = 'XDATCAR'
ATOM = 'N'
NATOM = 64
HEADER_LINES = 5

def main():
    
    """ Write the xyz file """

    try:
        acell = float(sys.argv[1])
    except IndexError:
        print '\nPlease provide the lattice constant.\n'
        sys.exit(0)
    
    f = open(FNAME,'r')
    for i in range(HEADER_LINES): f.readline()
    lines = f.readlines()
    f.close()
    
    out = open(FNAME+'.xyz','w')
    
    ntime = len(lines) / (NATOM + 1)  # +1 for the blank line in between each timestep
    
    for i in range(ntime):
    
        lines.pop(0) # Remove the blank line
        out.write(str(NATOM)+'\n')
        out.write(str(i+1)+'\n')
    
        for j in range(NATOM):
            
            row = lines.pop(0).split()
            for i in range(len(row)): row[i] = float(row[i])*acell
    
            out.write(ATOM+' '+str(row[0])+' '+str(row[1])+' '+str(row[2])+'\n')
    
    out.close()

if __name__ == "__main__":
    main()