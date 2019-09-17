# mdtest
ESIFHPC2 mdtest Benchmark

## Licensing
mdtest is licensed under GPLv2, as detailed in file COPYRIGHT.

## Benchmark Description
mdtest is designed to characterize metadata performance of a filesystem. The intent of this benchmark is to measure the performance of file metadata operations on each proposed globally accessible file system.

## Build Instructions
Source code for version 1.8.3 is provided, and must be used to build the binaries from which benchmark data is reported.
The code is composed of one C file, mdtest.c.
MPI is used to coordinate operations and collect results, and is required in order to build and run the code.
More information about mdtest may be found at https://github.com/LLNL/mdtest or http://mdtest.sourceforge.net. 

After extracting the tar file,

>  cd mdtest

>  make -f Makefile.NREL CC=mpicc CFLAGS=-g

This will build the executable `mdtest`. 

## Required Runs

For each proposed globally accessible file system, the Offeror shall run the following tests:
* creating, statting and removing 1,048,576 files in a single directory
* creating, statting and removing 1,048,576 files in separate directories (one directory per MPI process)
* creating, statting and removing 1 file by multiple MPI processes

Each of these tests should be run at the following concurrency:

 1. A single MPI process
 2. The optimal number of MPI processes on a single compute node 
 3. The mimimal number of MPI processes on multiple compute nodes that achieves the peak results for the proposed system 
 4. The maximum number of MPI processes on the full set of nodes of each type, using one MPI process per physical core 

Each of these tests should be run for each node type.

Each of these tests should be run for each globally accessible file system. 

These tests are configured via command-line arguments, which are described in the _Running mdtest_ section below. 

## Run Rules
If the benchmarked filesystems include multiple file access protocols or
multiple tiers accessible by applications, benchmark results for mdtest shall be
provided for all protocols, tiers, and combinations thereof where appropriate. 

The benchmark is intended to measure the capability of the storage subsystem to
create and delete files and it contains features that minimize caching/buffering
effects. You should not utilize optimizations that cache or buffer file
metadata or metadata operations in compute node (client) memory. 

## Running mdtest
mdtest is executed as any standard MPI application would be, for example with
`mpirun`. The exact invocation depends on your MPI implementation. 

The following command-line flags will be used and MUST NOT be changed or omitted:

* `-F` only operate on files, not directories
* `-C` perform file create test
* `-T` perform file stat test
* `-r` perform file remove test

The following command-line flags should be set as appropriate for your runs:

 * `-np` the number of MPI processes. This is an argument to mpirun; the remaining options below are arguments to mdtest itself.
 * `-n` number of files per MPI process
 * `-d` absolute path to directory in which the test should be run
 * `-N tasks_per_node` This option provides the rank offset for the different phases of the test. This parameter must be equal to the number of MPI processes per node and you must ensure that MPI ranks are placed consecutively on nodes rather than round-robin across nodes. This ensures that each test phase (read, stat, delete) is performed on a different node (the task that deletes a file is on a different node than the task that created the file). 
 * `-u` This option causes each MPI process to write files into a unique directory. 
 * `-S` This option causes MPI processes to process shared files.

For the tests that create, stat and remove 1,048,576 files, you must specify the number of files _each_ process will create. 
For example, the command
>    mpirun -np 64 ./mdtest -F -C -T -r -n 16384 -d /scratch -N 16 

will use **64** **MPI** **processes**. Each MPI process will manipulate **16384** files for a **total** of **1048576** files (64 &times; 16384). 
 
To create, stat and remove files from a single directory using 64 MPI tasks on 4 nodes:
>    mpirun -np 64 ./mdtest -F -C -T -r -n 16384 -d /scratch -N 16 

To create, stat and remove files that are in separate directories using 64 MPI tasks on 4 nodes, add the -u option: 
>    mpirun -np 64 ./mdtest -F -C -T -r -n 16384 -d /scratch -N 16 -u
    
To create, stat and remove one file by multiple MPI processes (N processes:1 file), add the -S option:

>    mpirun -np 64 ./mdtest -F -C -T -r -n **1** -d /scratch -N 16 **-S**
 
The file create, stat and delete portions of the execution will be timed and the rate of file creation/statting/deletion are reported to stdout at the end of each test. 

## Reporting Results
The `File creation`, `File stat` and `File removal` rates from stdout should be
reported. The maximum values for these rates must be reported for all tests.
Reporting the maximum creation rates from one run and the maximum deletion rates
from a different run is NOT permitted. If the highest observed file creation
rate came from a different run than the highest observed deletion rate, report
the results from the run with the highest file creation rate. 
 * Provide all output files. If performance projections are made, all output files on which the projections are based must also be provided.
 * For each run reported, include the mdtest command line used and its correspondence to the associated rates. 

## Benchmark Platform Description
In addition to the information requested in the General Benchmark instructions, the benchmark report for mdtest should include 
 * the file system configuration and mount options
 * the storage media and configurations used for each tier of the storage subsystem
 * network fabric used to connect servers, clients and storage including network configuration settings and topology
 

