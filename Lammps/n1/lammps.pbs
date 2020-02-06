#!/bin/bash 
#PBS -l walltime=4:00:00             # WALLTIME
#PBS -l nodes=1:ppn=24                # Number of nodes and processes per node
#PBS -N lmp1
#PBS -o std.out
#PBS -e std.err

cd $PBS_O_WORKDIR

module purge
module use /nopt/nrel/apps/modules/candidate/modulefiles
module load impi-intel/5.1.3-16.0.2 mkl/16.2.181 lammps/17Nov2016

#For debugging the node: Print out which nodes are using
#cat $PBS_NODEFILE > node.log

time mpirun -n 24 lmp_mpi -in small.in -l small.out 
time mpirun -n 24 lmp_mpi -in medium.in -l medium.out
time mpirun -n 24 lmp_mpi -in large.in -l large.out

#For 16 and 64 nodes runs only
#time mpirun -n XXX lmp_mpi -in medium_numerical_test.in -l medium_numerical_test_16.out

#Generate performance report
echo "Final Report:" > report.out
echo "Small:" >> report.out
grep "Loop time" small.out >> report.out
grep "Performance" small.out >> report.out
echo >> report.out
echo "Medium:" >> report.out
grep "Loop time" medium.out >> report.out
grep "Performance" medium.out >> report.out
echo >> report.out
echo "Large:" >> report.out
grep "Loop time" large.out >> report.out
grep "Performance" large.out >> report.out



