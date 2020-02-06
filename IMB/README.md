Intel MPI Benchmarks
===
## Licensing
The Intel MPI Benchmarks package (IMB) is licensed under the Common Public License Version 1.0, as described at https://software.intel.com/en-us/articles/intel-mpi-benchmarks (Tue Mar 28 11:25:00 MDT 2017).

## Description
IMB is used to measure application-level latency and bandwidth, particularly over a high-speed interconnect, associated with a wide variety of MPI communication patterns with respect to message size. We supply source code retrieved on : Tue Mar  7 13:16:50 MST 2017. 

For the current purpose, we are interested in these tests:

	- PingPong
	- Sendrecv
	- Exchange
	- Barrier
	- Uniband
	- Biband
	- Allreduce
	- Alltoall
	- Allgather
	
## How to Build
The source code for IMB may be found in `imb/src`. 

To build the binary needed for testing,

   1. `% cd imb/src`
   2. `% make` (this will create the IMB-MPI1 binary that will be used for testing)

If needed, please refer to further information in `imb/ReadMe_IMB.txt`, or at [https://software.intel.com/en-us/articles/intel-mpi-benchmarks](https://software.intel.com/en-us/articles/intel-mpi-benchmarks).

## How to Run
An example run script is provided as imb/test.pbs, and illustrates how to run a targeted selection of tests and rank counts with Intel MPI.

Additional details can be found in the IMB User's Guide in the imb/doc directory.
