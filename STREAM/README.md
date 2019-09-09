STREAM
===

## Licensing
STREAM is licensed per http://www.cs.virginia.edu/stream/FTP/Code/LICENSE.txt.

## Description

STREAM is used to measure the sustainable memory bandwidth of high performance computers.
The code is available from [http://www.cs.virginia.edu/stream/ref.html](http://www.cs.virginia.edu/stream/ref.html)

We provide source code retrieved on : Tue Mar  7 13:09:56 MST 2017 

## How to Build

An example Makefile is provided in src/. In addition, an example `test.sh` script is included
that builds and runs the benchmark.

The STREAM Triad benchmark uses 3 arrays of size N.
This can be controlled with `-DSTREAM_ARRAY_SIZE=<array_size>` during compilation,
where `array_size` is the number of elements in the array. For double-precision floats,
then, total array memory (GB) = 3 * STREAM\_ARRAY\_SIZE * 8 (bytes/float) / 1000<sup>3</sup>.

The offeror will build at least cases (1) and (2) of the benchmark, with (3) where applicable:

(1)  default memory size defined in STREAM (_i.e._, not using `-DSTREAM_ARRAY_SIZE=<array_size>`; note that
     the Fortran source code has had a preprocessor definition added that sets the default array size
     to be consistent with the C version); and,

(2)  a case which uses 60% of the total DRAM available on a single node.

## How to Run

The STREAM Triad benchmark results must be returned for the following cases: 

 1. one thread
 2. one thread on each available physical core in a node utilizing all the available cores (C in the reporting spreadsheet).
 3. with minimum #threads required to achieve maximum bandwidth (M in the reporting spreadsheet).

## What to Consider

Look at the Triad bandwidth (GB/s) that is printed to the standard output. It is important to consider all runtime settings such as pinning threads to cores, utilizing specific NUMA domains, etc. that impact STREAM Triad results.

Output should indicate a valid solution, as in: 

`Solution Validates: avg error less than 1.000000e-13 on all three arrays`

