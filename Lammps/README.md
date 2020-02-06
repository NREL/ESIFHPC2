## Licensing
LAMMPS is open-source software licensed under the GPLv2. 

Description
-----------
Source code for LAMMPS version "Nov 17, 2016" is supplied as a tarball file for the "As-is" tests. See _How to Build_ below for information concerning testing code optimization.

Directory `n1` has LAMMPS inputs and a sample PBS script `lammps.pbs` to run LAMMPS. 

We supply a LAMMPS snapshot file with name "data.begin.bz2", which should be unzipped before running. This file contains coordinates and velocities of ~0.7 million atoms in a cubic unit cell, ~20 nm on a side, representing a 35% LiCl solution pre-equlibrated to 300K and 1 atm. Larger unit cells for "medium" and "large" systems are generated programmatically from this input.

Three LAMMPS benchmarks are formulated, and input files `small.in`, `medium.in`, and `large.in` are provided. For `medium.in` and `large.in`, the unit cell decribed above is replicated to create larger cubic cells (via LAMMPS `replicate` commands).    

Directory `nrel_results` has reference results for validation. 

How to Build
------------
The benchmark results for "As-is" tests must be generated from the supplied source code. Optional libraries or packages included in the LAMMPS distribution (*e.g.*, OpenMP) may be used.

LAMMPS can be built by following the instructions at http://lammps.sandia.gov/doc/Section_start.html. For example, if the MPI environment is set up correctly, a pure-MPI build (*i.e.*, no optional packages) may be as simple as
`tar -xvzf lammps-17Nov16.tar.gz; cd lammps-17Nov16/src; make mpi`

How to Run  
----------
For each benchmark system size, the total simulation time is controlled via the input parameter `thermo` in the LAMMPS input scripts. As MPI rank counts are increased, `thermo` should be increased in order to maintain a simulation wall time ("Loop time") of 600 seconds or greater, and to keep the total number of simulation steps ("total-running-steps") equal to 10 times `thermo`. 

How to Validate
-------------------------
Numerical results vary somewhat with respect to the number of MPI ranks employed. In recognition of this, we are requesting validation only on two specific runs: using the `medium_numerical_test.in` input in directory `n1`, with 16 and 64 MPI ranks. The performance results from these validation runs are not to be entered into the reporting sheet.

A script named `validate.sh` is provided to validate system temperature and total energy data from the output of each of these runs against those obtained by NREL. The Offeror should run this script with the first argument as the path to the output file of a validation run, and the second argument the path to the provided directory `nrel_results` containing reference data. So,

`./validate.sh PATH_TO_OUTPUT/lammps_output PATH_TO_NREL_RESULTS/`

(Example: `./validate.sh n1_results/medium_numerical_test_16.out nrel_results/` ) 

This will produce a file called `thermo.dat` that contains time, temperature, and energy output for the run; and, a file `rms_errors.dat` that contains validation information. The first line in `rms_errors.dat` gives the average temperature and energy for the run. These should have values of approximately 300 and -8.9e+07, respectively. The second line gives the relative root-mean-squared deviation between the output provided by NREL (in `NREL_thermo.dat`) and the output from the test run. Reasonable relative deviations are less than 10<sup>-3</sup> for temperature and 10<sup>-5</sup> for energy. The validation script returns either "run validated" or "run not validated" on the third line of `rms_errors.dat`, depending on whether deviations are less than or greater than these thresholds, respectively.

