#!/bin/bash

# User-defined setting for thread count leading to maximum performance, and number of physical cores
#   Assumes hyperthreading is off.
max_performing_threads=12
num_physical_cores=`grep -c processor /proc/cpuinfo`
# Calculating array size 
num_64bfloats_60percent=$(echo "0.6 * `grep MemTotal /proc/meminfo | awk '{print $2}'` * 1000 / 8 / 3" | bc)

rm results.${CC}.${FC}

echo "STREAM test run.." &>> results.${CC}.${FC}
echo "Checking Compilers.." &>> results.${CC}.${FC}
echo "  C compiler used ${CC} .." &>> results.${CC}.${FC}
echo "  Fortran compiler used ${FC} .." &>> results.${CC}.${FC}
echo "Running make clean .." &>> results.${CC}.${FC}
make clean 
echo "Building the default executable .." &>> results.${CC}.${FC}
make all CC=${CC} FC=${FC}

echo "Running the C executable with default memory, 1 thread.." &>> results.${CC}.${FC}
export OMP_DISPLAY_ENV=True
export KMP_AFFINITY=verbose
export OMP_NUM_THREADS=1
./stream_c.${CC}.exe  &>> results.${CC}.${FC}
echo "C executable test with default memory, 1 thread complete.." &>> results.${CC}.${FC}

echo "Running the C executable with default memory, $num_physical_cores OpenMP threads.." &>> results.${CC}.${FC}
export OMP_NUM_THREADS=$num_physical_cores
./stream_c.${CC}.exe  &>> results.${CC}.${FC}
echo "C executable test with default memory, $num_physical_cores threads complete.." &>> results.${CC}.${FC}

echo "running the C executable with default memory, $max_performing_threads OpenMP threads.." &>> results.${CC}.${FC}
export OMP_NUM_THREADS=$max_performing_threads
./stream_c.${CC}.exe  &>> results.${CC}.${FC}
echo "C executable test with default memory, $num_physical_cores threads complete.." &>> results.${CC}.${FC}

echo "running the Fortran executable with default memory, 1 thread.." >> results.${CC}.${FC}
export OMP_NUM_THREADS=1
./stream_f.${FC}.exe &>> results.${CC}.${FC}
echo "Fortran executable test with default memory, 1 thread complete.." &>> results.${CC}.${FC}

echo "Running the Fortran executable with default memory, $num_physical_cores OpenMP threads.." &>> results.${CC}.${FC}
export OMP_NUM_THREADS=$num_physical_cores
./stream_f.${FC}.exe  &>> results.${CC}.${FC}
echo "Fortran executable test with default memory, $num_physical_cores threads complete.." &>> results.${CC}.${FC}

echo "running the Fortran executable with default memory, $max_performing_threads OpenMP threads.." &>> results.${CC}.${FC}
export OMP_NUM_THREADS=$max_performing_threads
./stream_f.${FC}.exe  &>> results.${CC}.${FC}
echo "Fortran executable test with default memory, $num_physical_cores threads complete.." &>> results.${CC}.${FC}

echo "Running make clean .." &>> results.${CC}.${FC}
make clean 
echo "Building STREAM executable to use 60% of memory.." &>> results.${CC}.${FC}
make all CC=${CC} FC=${FC} CPPFLAGS="-DSTREAM_ARRAY_SIZE=$num_64bfloats_60percent"

echo "Running the C executable with 60% memory, 1 thread.." &>> results.${CC}.${FC}
export OMP_NUM_THREADS=1
./stream_c.${CC}.exe  &>> results.${CC}.${FC}
echo "C executable test with 60% memory, 1 thread complete.." &>> results.${CC}.${FC}

echo "Running the C executable with 60% memory, $num_physical_cores OpenMP threads.." &>> results.${CC}.${FC}
export OMP_NUM_THREADS=$num_physical_cores
./stream_c.${CC}.exe  &>> results.${CC}.${FC}
echo "C executable test with 60% memory, $num_physical_cores threads complete.." &>> results.${CC}.${FC}

echo "running the C executable with 60% memory, $max_performing_threads OpenMP threads.." &>> results.${CC}.${FC}
export OMP_NUM_THREADS=$max_performing_threads
./stream_c.${CC}.exe  &>> results.${CC}.${FC}
echo "C executable test with 60% memory, $num_physical_cores threads complete.." &>> results.${CC}.${FC}

echo "running the Fortran executable with 60% memory, 1 thread.." >> results.${CC}.${FC}
export OMP_NUM_THREADS=1
./stream_f.${FC}.exe &>> results.${CC}.${FC}
echo "Fortran executable test with 60% memory, 1 thread complete.." &>> results.${CC}.${FC}

echo "Running the Fortran executable with 60% memory, $num_physical_cores OpenMP threads.." &>> results.${CC}.${FC}
export OMP_NUM_THREADS=$num_physical_cores
./stream_f.${FC}.exe  &>> results.${CC}.${FC}
echo "Fortran executable test with 60% memory, $num_physical_cores threads complete.." &>> results.${CC}.${FC}

echo "running the Fortran executable with 60% memory, $max_performing_threads OpenMP threads.." &>> results.${CC}.${FC}
export OMP_NUM_THREADS=$max_performing_threads
./stream_f.${FC}.exe  &>> results.${CC}.${FC}
echo "Fortran executable test with 60% memory, $num_physical_cores threads complete.." &>> results.${CC}.${FC}

echo "STREAM test complete!" &>> results.${CC}.${FC}
