HPL
===
HPL is a software package that solves a (random) dense linear system in double precision (64-bit) arithmetic on distributed-memory computers. It can thus be regarded as a portable as well as freely available implementation of the High Performance Computing Linpack Benchmark.

## Licensing
HPL is licensed per the COPYRIGHT notice in the hpl-2.2 folder.

## Description
We are providing source code retrieved on Tue Mar  7 13:18:25 MST 2017.

## How to Build
Full instructions are found in the `hpl-2.2/INSTALL` file. In short,

* Copy a template "Make.<arch>" file from the `setup` directory into the top-level directory. In this distribution, that is the `HPL/hpl-2.2` directory.
* Rename this file to whatever is convenient, _e.g._, Make.myarch. Canonically this reflects the architecture, but can be anything unique.
* Change variable TOPdir in this Make.myarch file to reflect the location of hpl-2.2.
* Change variable ARCH in this Make.myarch file to whatever suffix has been chosen (_i.e._, myarch in this example).
* Modify the file as needed to create binaries optimized for the Offered architecture.
* `make arch=myarch`

More information may be found at "http://www.netlib.org/benchmark/hpl/". 

## How to Run
The values of #MPI\_tasks\_per\_node, #Threads\_per\_node, N, NB, P, and Q should be chosen to achieve maximum performance.
 
## Result validation
All output should show that tests passed successfully, as in: 

```
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=        0.0013190 ...... PASSED

```
