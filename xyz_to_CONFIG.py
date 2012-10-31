#! /usr/bin/python

""" Script to covnvert .xyz files to DL_POLY CONFIG files """

import os, sys, commands

def main():

    """ Create CONFIG file """

    try:
        fname_xyz = sys.argv[1]
        acell = float(sys.argv[2])
    except IndexError:
        print 'Please provide name of .xyz file and lattice constant (angstrom)'
        sys.exit(0)

    file_xyz = open(fname_xyz,'r')
    natom = int( file_xyz.readline().strip() )
    tstep = int( file_xyz.readline().strip() )

    t4 = '     '
    t7 = '       '
    t3 = '   '

    out = open('CONFIG','w')
    out.write('DL_POLY: CONFIG file \n')
    out.write(t7+'0'+t4+t4+'1'+'\n')
    out.write(t7+' % .8f' % acell +t3+' % .8f' % 0.0 +t3+' % .8f' % 0.0 +'\n')
    out.write(t7+' % .8f' % 0.0 +t3+' % .8f' % acell +t3+' % .8f' % 0.0 +'\n')
    out.write(t7+' % .8f' % 0.0 +t3+' % .8f' % 0.0 +t3+' % .8f' % acell +'\n')

    lines = file_xyz.readlines()
    file_xyz.close()
    for i in range(len(lines)):

        row = lines[i].split()
        typat = row[0]

        out.write(typat+t7+t7+str(i+1)+'\n')
        out.write(t4+' % .8f' % float(row[1])+t4+' % .8f' % float(row[2])+t4+' % .8f' % float(row[3])+'\n')
    
    out.close()

if __name__ == '__main__':
    main()