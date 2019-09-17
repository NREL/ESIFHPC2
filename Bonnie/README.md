Licensing
---------
Bonnie++ is licensed under the GPLv2, as stated in copyright.txt.

Description
-----------
Bonnie++ is a file system performance benchmarking tool for Unix and Unix-like local and network file systems.
Further information on Bonnie++ can be found at http://www.coker.com.au/bonnie++/, or on the online manual page
https://linux.die.net/man/8/bonnie++.

How to Build
------------
Bonnie++ is written in C++ and building requires the GCC C++ compiler. Benchmark results must be generated with binaries built from the source code provided in this repo.

The build should require nothing more than a simple

`./configure CC=gcc CXX=g++; make; make install`

How to Run
----------
Bonnie++ should be run for each network-connected file system on each node type as indicated in the benchmark reporting spreadsheet. In addition, it should be run on the local file system for the Standard, Big Memory, and DAV nodes. 

Iterations for each node type should be run on 1 core, half the available cores on the node, and all the available cores on the node. 

Example of a four-process run targeting the filesystem holding `./bonnie-local`:
```
# Create semaphore array for process synchronization over 4 processes
./sbin/bonnie++ -p4
# Start Bonnie++ processes, each writing to its own target directory and files
for i in 0 1 2 3
do
   mkdir -p bonnie-local/$i
   ./sbin/bonnie++ -m dale-4 -y -f -d ./bonnie-local/$i >& out4.$i &
done
# Delete semaphore array
./sbin/bonnie++ -p -1
```
In case of local filesystems with multiple groupings of disks, run for each grouping. For example, if there is a RAID 1 OS grouping, and a RAID 6 Data grouping, run against each.

Reporting Results
-----------------
Parsing output may be easiest using the HTML convertor as pre-processor, _e.g._,

`tail -1 out4.0 | ../bin/bon_csv2html > out4.0.html`

Outside of the materials enumerated in the General Benchmark instructions,  
* Report sequential write(create), sequential rewrite, and sequential read performance. When running more than one process, please report the sum over all processes.
* _Explain_ the reasons behind any differences in submission flags used from the example. For example, RAM size shouldn't need to be specified, but can be with -r if it is not discovered by Bonnie++. In addition to the system-level specifications enumerated in the General Benchmark Instructions, please provide any user-level configuration options used to run Bonnie++ (_e.g._, striping).
