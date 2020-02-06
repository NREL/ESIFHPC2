Licensing
---------
Nalu is licensed under the Nalu 1.0 license, which may be found at https://github.com/NaluCFD/Nalu/blob/master/LICENSE.

Description
-----------
Nalu is a new CFD application we are using for wind farm modeling and it is important that we are able to run Nalu at a large scale. The individual Nalu benchmark runs as formulated measure strong scaling. In addition, we are interested in system throughput under load. To simulate this, we include a configuration that includes multiple simultaneous instances of Nalu. 

How to Build
------------
### Configuring Nalu and building dependencies
Official documentation for building Nalu is located at `http://nalu.readthedocs.io/en/latest/`. Given the relatively deep stack of dependencies that Nalu has, we use [Spack](https://github.com/LLNL/spack) to automate the build. Documentation for this is provided at `http://nalu.readthedocs.io/en/latest/source/build_spack.html`. All of the current build knowledge for Nalu and its dependencies have been implemented in Spack. For the purposes of this benchmark it may be easiest to manually build Nalu and its dependencies for finer control. A manual build can be done by following the detailed instructions given at `http://nalu.readthedocs.io/en/latest/source/build_manually.html`.

In general the third party library and Nalu versions must be the same ones used for generating NREL baseline results. The version numbers or git commit hashes used in the baseline were:

```
  nalu@master-f31225e37916665eb4c21f2304810bc441ddc3bd
  trilinos@develop-88a27743b402a6143ca39f64f6a08df244e42017
  boost@1.60.0
  netcdf@4.3.3.1
  parallel-netcdf@1.6.1
  xz@5.2.3
  bzip2@1.0.6
  yaml-cpp@0.5.3
  cmake@3.6.1
  libxml2@2.9.4
  zlib@1.2.11
  hdf5@1.8.16
  superlu@4.3
```
_NOTE: To checkout a specific version of a Git repository, the following workflow should be used (using Nalu as an example):_
```
  git clone https://github.com/NaluCFD/Nalu
  cd Nalu
  git checkout f31225e37916665eb4c21f2304810bc441ddc3bd
  git rev-parse HEAD
```

How to Run
----------
### Strong Scaling Test
There are two cases differing in mesh size (256 and 512) that are provided. We provide input files for these two problem sizes (in directories `abl_3km_256` and `abl_3km_512`, respectively). To run, simply specify the input file and log file names:

```
  mpirun -np 4 naluX -i abl_3km_256.i -o abl_3km_256.log
```

The input files cause writing of large output every 100 timesteps and writes checkpoint data every 1000 steps, with the entire case running for 2500 timesteps.

The `nalu_all_jobs.sh`, `nalu_all_jobs_throughput.sh` and `nalu_single_job.sh` scripts are provided to show how Nalu was run to obtain reference results. 

### Throughput Test
Run up to 100 instances of the 512 mesh benchmark. The particular number of instances may be chosen to reflect optimal capability of the Offered system. The number of jobs completed per time will ultimately be combined with an analogous value from the Nalu throughput benchmark to derive a final throughput metric.

Validating Output
-----------------
Validating output in Nalu requires checking the difference of the norms in the Nalu log file against our "gold" norms generated from our baseline test. Unfortunately Nalu results can be very sensitive to the BLAS and LAPACK libraries used, and compiler optimizations employed. To validate results, for the 256 mesh case on 192 ranks only, run `abl_3km_256/pass_fail.sh` on the log file with a 1e-3 tolerance, like:

```
./pass_fail.sh abl_3km_256_192 0.001
```

where `abl_3km_256_192` is the basename of the log file, and `0.001` is the tolerance. This will create a `.norm` file from the log file and check the differences against the "gold" norm file.  Note that running simulations with different numbers of ranks can cause deviations in the norms, as can be seen between the "gold" norm files provided. For a successful validation, the Offeror may match the number of MPI ranks used with the number of MPI ranks used in the "gold" norm files. Validation against a single "gold" norm for each case is sufficient to pass.

