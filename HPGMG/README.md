Licensing
---------
The HPGMG benchmark is licensed under the 2-clause BSD license found in hpgmg-code/LICENSE.

Description
-----------
The HPGMG finite volume benchmark is important to certain combustion applications, and offers a more direct view of balanced system performance than does the traditional HPL floating-point operations-per-second metric. The code uses hybrid parallelism over both MPI ranks and OpenMP threads.

How to Build
------------
To build HPGMG, use the snapshot of the code provided in the `hpgmg-code` directory.

Edit the Makefile in the `hpgmg-code/build` directory as needed.

To build, use the command `make V=1`.

How to Run
----------
Once the HPGMG binary is compiled, a simple example of running it with OpenMPI on 24-core nodes with two CPU sockets and 12 threads per MPI rank with `X` MPI ranks would be carried out as such:

```
export OMP_NUM_THREADS=12; mpirun -np X --map-by ppr:2:node --bind-to socket ./hpgmg-fv 7 8
```

Another example of running the HPGMG benchmark is shown in `hpgmg-code/README.md`. The hpgmg-fv executable takes two positional arguments. The first is the base-2 logarithm of the box dimension; the second is the number of boxes per rank. The recommended values for these parameters are 7 and 8, respectively.

### Scaling Test
Performance for MPI rank counts of 64, 128, 256, 512, and 1024 as well as performance results for the full number, half, and one-quarter of the Offered nodes must be provided.

### Throughput Test
The HPGMG-FV benchmark runs for a fixed time, and reports performance as degrees of freedom per second (DOF/s). Fill the set of tested nodes with 8-12 concurrent HPGMG runs, with the specific choice made to maximize the aggregate metric (DOF/s) achievable. System throughput from these results is calculated as the sum of the DOF/s values from the concurrent jobs.

