IOR
===

## Licensing
IOR is licensed under GPLv2. Further information can be found at https://github.com/LLNL/ior.

## Description
IOR is designed to measure parallel file system I/O performance at both the POSIX and MPI-IO level. This parallel program performs writes and reads to/from files and reports the resulting throughput rates. We use this benchmark to understand the performance of the proposed file systems for POSIX IO. 

## How to Build
MPI and MPI-IO are required in order to build and run the code. The source code used for ESIFHPC2 is version 2.10.3. For benchmarking, the source code distributed here must be used.

To build the code, execute the following steps:

```% cd ior/src/C```

```% make mpiio ``` 

which will build both the MPI-IO and the POSIX versions of the benchmark into the resulting executable.
The resultant executable image is the file `IOR` and it will need to be moved up to the “run” subdirectory.. 

Compiler options, names, etc., are in the file ```src/C/Makefile.config```. 

## Run Definitions and Requirements

The following tests are expected:

* POSIX I/O to determine streaming performance 
* POSIX I/O to determine random I/O performance

These tests will be run for the following processor/node count conditions:

1. The number of processes on one node that yields the peak performance for each globally accessible file system for a single node of each user-accessible node type.
2. The number of processors on one node that yields the peak performance for the local storage on the big memory and DAV nodes. 
3. The number of fully subscribed standard nodes that yields the peak performance for each globally accessible file system. 

For more information on IOR, please read the User Guide included with the source distribution.

## How to Run

### Streaming I/O Test:

The following command line should be used to measure streaming performance:

`mpirun -np {NP} -wd {WorkingDir} -machinefile {MachineFile} {IOR Pathname}/IOR -v -a POSIX -i5 -g -e -w -r -b{Filesize}g -T 10 -F -C -t 4m`

The mpirun options should be modified as needed for the specific MPI implementation. The number of MPI tasks {NP} should be varied as needed. For single node performance tests, report results obtained for the value of NP that provides the maximum performance. For system peak performance tests, nodes should be fully subscribed and results for the node count that provides maximum performance should be reported. 

IOR options that may be changed:
* The {Filesize} must be set to be a multiple of the compute node's memory, to prevent cache effects. Record the value of this parameter.
* Results should be reported both for 4m transfers (-t 4m} and for a job with optimal transfer size (-t Xm). For each test run with an optimal transfer size, record the transfer size used.
 
### Random I/O Test:

The following command line should be used to measure random I/O performance: 

`mpirun -np {NP} -wd {WorkingDir} -machinefile {MachineFile} {IOR Pathname}/IOR -v -a POSIX -i5 -g -e -w -r -b{Filesize}g -T 10 -F -z -t 4k`

The mpirun options should be modified as needed for the specific MPI implementation. The number of MPI tasks {NP} should be varied as needed. For single node performance tests, report results obtained for the value of NP that provides the maximum performance. For system peak performance tests, nodes should be fully subscribed and results for the node count that provides maximum performance should be reported. 

IOR options that may be changed:
* The {Filesize} must be set to be a multiple of the node's memory to prevent cache effects.  

For each run the program does five repetitions of the write/read process. The maximum values are calculated and these values should be reported as the benchmark result.

## Run Rules

In addition to the general ESIFHPC2 benchmark rules, the following also apply:

Changes related to tuning must be practical for production utilization of the filesystem. For example, optimizations that are tuning hints that can be controlled by users on the system are permissible, but optimizations that would require superuser privilege (but are not part of the standard configuration of the filesystem) are not permissible. Details on any optimizations used to run these benchmarks should be documented.

## Benchmark test results to report and files to return
In addition to items enumerated in the General Benchmark Instructions, include commands used as well as a description of 
* client and server configurations (node and processor counts, processor models, memory size, speed, OS)
* client and server configuration settings including
  * client and server sysctl settings
  * driver options
* network interface options
* file system configuration options
* storage and storage configuration for each file system
* network fabric used to connect servers, clients and storage
* network configuration settings
