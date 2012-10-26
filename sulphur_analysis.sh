#!/bin/bash

alat=`head -2 POSCAR | tail -1`
alat_half=`head -2 POSCAR | tail -1 | awk '{print $1/2}'`
alat_bohr=`head -2 POSCAR | tail -1 | awk '{print $1/.529177}'`

# cbn
  tail -102000 TRAJEC.xyz > TRAJEC.1000.xyz 
  echo "TRAJEC.1000.xyz" > cbn.in
  echo "$alat_bohr, $alat_bohr, $alat_bohr" >> cbn.in
  ~/analysis/fortran/cbn_from_xyz_cpmd.osx < cbn.in
  rm -f cbn.in
  rm -f TRAJEC.1000.xyz 

# cnn
  ~/analysis/nn_distance/nn_distance_distributions_cnn.py 100 $alat_bohr $alat_bohr $alat_bohr TRAJEC.1000.xyz
  echo "TRAJEC.xyz" > nn_dist.in
  echo "$alat, $alat, $alat">> nn_dist.in
  echo "200" >> nn_dist.in
  echo "64" >> nn_dist.in
  ~/analysis/fortran/nn_dist/nn_dist.osx < nn_dist.in
  rm nn_dist.in

# rdf
  echo "TRAJEC.xyz" > RDF.in
  echo "RDF.dat"    >> RDF.in
  echo "S" >> RDF.in
  echo "S" >> RDF.in
  echo "$alat_half" >> RDF.in
  echo "0.025" >> RDF.in
  echo "0" >> RDF.in
  echo "$alat, $alat, $alat" >> RDF.in

  ~/analysis/fortran/RDF/RDF.osx < RDF.in

# unwrap
  echo "TRAJEC.xyz" > unwrap.in
  echo "$alat, $alat, $alat" >> unwrap.in
  ~/analysis/fortran/unwrap_PBC.osx < unwrap.in
  rm -f unwrap.in
# msd
  echo "unwrapped.xyz" > msd.in
  ~/analysis/fortran/msd.osx < msd.in
  rm -f msd.in


# bonding
rm -rf correlators
mkdir correlators
  ~/analysis/bonding_lifetime/bonding_lifetime_n_body.py TRAJEC.cnn 1  100 &
  ~/analysis/bonding_lifetime/bonding_lifetime_n_body.py TRAJEC.cnn 2  100 &
  ~/analysis/bonding_lifetime/bonding_lifetime_n_body.py TRAJEC.cnn 3  100 &
  ~/analysis/bonding_lifetime/bonding_lifetime_n_body.py TRAJEC.cnn 4  100 &
  ~/analysis/bonding_lifetime/bonding_lifetime_n_body.py TRAJEC.cnn 5  100 &
  ~/analysis/bonding_lifetime/bonding_lifetime_n_body.py TRAJEC.cnn 6  100 &
  ~/analysis/bonding_lifetime/bonding_lifetime_n_body.py TRAJEC.cnn 7  100 &
  ~/analysis/bonding_lifetime/bonding_lifetime_n_body.py TRAJEC.cnn 8  100 &
  ~/analysis/bonding_lifetime/bonding_lifetime_n_body.py TRAJEC.cnn 9  100 &
  ~/analysis/bonding_lifetime/bonding_lifetime_n_body.py TRAJEC.cnn 10 100 &
  ~/analysis/bonding_lifetime/bonding_lifetime_n_body.py TRAJEC.cnn 11 100 &
  ~/analysis/bonding_lifetime/bonding_lifetime_n_body.py TRAJEC.cnn 12 100 &
wait

mv correlator_*nn.dat correlators/

rm -f peak_correlator.tmp
for correlator in correlators/correlator_?nn.dat correlators/correlator_??nn.dat
do
tail -1 $correlator| awk '{print $NF}' >> peak_correlator.tmp
done 

awk '{n+=1; print n, $1}' peak_correlator.tmp > peak_correlator.dat
rm -f peak_correlator.tmp
