SHOC 
===

This benchmark is only relevant for GPU-containing nodes only. 

## Licensing
The SHOC benchmark code is licensed per the LICENSE statements in the `src` directory.

## Description
Source code retrieved at Tue Mar  7 13:12:04 MST 2017 is provided.

A "GPU" is considered to be a GP-GPU package occupying a single socket. 

## How to Build
Build instructions may be found on [https://github.com/vetter/shoc/wiki/GettingStarted](https://github.com/vetter/shoc/wiki/GettingStarted). To build with the latest CUDA support, it may be necessary to modify the configure script to enable the specific GPU architecture being offered (*i.e.*, -gencode options).

## How to Run

### Level 0:

**BusSpeedDownload and BusSpeedReadback :** Measures the bandwidth of the PCIe bus by repeatedly transferring data of various sizes to and from the device. SHOC level 0 tests ignore -s sizing, and run cases from 1 kB through up to 512 MB. To run,

`bin/shocdriver -cuda -benchmark BusSpeedDownload`

`bin/shocdriver -cuda -benchmark BusSpeedReadback`

### Level 1:

**Triad :** a version of the STREAM Triad benchmark, measures bandwidth for a large vector dot product operation (including PCIe transfer). Note, SHOC Triad ignores the -s option, and runs cases from 64 kB - 16 MB per vector. 

To run,

`bin/shocdriver -cuda -benchmark Triad`

For all three tests, report results for 1 and 2 GPUs. For the latter, run this benchmark in parallel mode (_i.e._, ensure mpirun is available on `PATH`), and report the mean Triad bandwidth from the standard output or results.csv file. For example, to run the Triad test on a node with 2 GPUs, the command is

`bin/shocdriver -cuda -d 0,1 -benchmark Triad`

