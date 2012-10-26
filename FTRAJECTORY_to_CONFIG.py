#! /usr/bin/python

# Designed to take FTRAJECTORY files and make DL_POLY CONFIG files

import os, sys

ftraj = 'FTRAJECTORY'

f = open(ftraj,'r')
lines = f.readlines()
f.close()
natoms = 128
atom = 'H'
imcon = 1
levcfg = 0
ang = 0.529177249
a = 12.99828860880973 * ang # lattice constant in Ang
a = float(str(a)[:10])

# Write header info into CONFIG
g = open('CONFIG','w')
g.write('DL_POLY TEST: '+atom+'\n')
g.write('         '+str(levcfg)+'         '+str(imcon)+'\n')

a1 = [a,'0.00000000','0.00000000']
a2 = ['0.00000000',a,'0.00000000']
a3 = ['0.00000000','0.00000000',a]
g.write('        '+str(a1[0])+'        '+str(a1[1])+'        '+str(a1[2])+'\n')
g.write('        '+str(a2[0])+'        '+str(a2[1])+'        '+str(a2[2])+'\n')
g.write('        '+str(a3[0])+'        '+str(a3[1])+'        '+str(a3[2])+'\n')

for i in range(natoms):

    t,x,y,z,vx,vy,vz,fx,fy,fz = lines[i].split()

    # Convert the units (Note: 1 bohr = 0.529177249 angstrom)
    #                   (Note: 1 fs = 0.002418884326505 au) no it doesn't
    

    x = str(float(x)*ang)
    y = str(float(y)*ang)
    z = str(float(z)*ang)
    
    if x.split('.')[0] == '0':
        x = '.'+x.split('.')[1]
    if x.split('.')[0] == '-0':
        x = '-.'+ x.split('.')[1]       
    if y.split('.')[0] == '0':
        y = '.'+y.split('.')[1]
    if y.split('.')[0] == '-0':
        y = '-.'+ y.split('.')[1]
    if z.split('.')[0] == '0':
        z = '.'+z.split('.')[1]
    if z.split('.')[0] == '-0':
        z = '-.'+ z.split('.')[1]
    
    if x[0] == '-':
        x = x[:12]
    else: x = x[:11]
    if y[0] == '-':
        y = y[:12]
    else: x = x[:11]
    if z[0] == '-':
        z = z[:12]
    else: x = x[:11]

#    au = 24.18884326505 # per ps
#    t = 16. * au

#    vx = str(float(vx)/ang / au)
#    vy = str(float(vy)/ang / au)
#    vz = str(float(vz)/ang / au)
    
    g.write(atom+'              '+str(i+1)+'\n')
    if levcfg >= 0:
        g.write('    '+x+'        '+y+'        '+z+'\n')
    if levcfg >= 1:
        g.write('    '+vx+'        '+vy+'        '+vz+'\n')
    if levcfg >=2:
        g.write('    '+fx+'        '+fy+'        '+fz+'\n')
    
g.close()

#os.system('mv CONFIG ~/dl_poly_2.16/execute/CONFIG')
