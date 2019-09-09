VASP
====

Licensing
----------------
Must be arranged through developers or a commercial reseller per

https://www.vasp.at/index.php/faqs/71-how-can-i-purchase-a-vasp-license.

Benchmarks must be run with version 5.4.1.

General comments
----------------

1. Supplied content

    a. VASP input files: `INCAR*, POTCAR, POSCAR,` and `KPOINTS`   
    b. PBS job script templates   
    c. Validation scripts and reference data

2. Process to generate vendor results. Benchmarks should be run on the Standard node offering.

   For Standard nodes, runs will use the number of MPI ranks as given in the
reporting spreadsheet. Rank placement should be consecutive for consistency with
VASP NCORE option. However, the Offeror is permitted to map ranks within a NUMA
domain as desired, subject to limitations given in the general instructions.
   
3. Validation

    a. Validation is achieved via a script written in Python, version 3.5. This
lends the validation process a certain degree of platform independence, and
validation should be able to pass on any platform with a Python3 implementation,
assuming this implementation is done to standard. Aside from the standard
libraries alone, the validation process will require the `numpy` module.  
    b. Reference data is supplied, and should be in the same directory as the
`validate.py3` script at the time of validation.   
    c. Neither the `validate.py3` scripts nor the test or reference data may be
modified in any way by the Offeror, without prior written permission.   
    d. The directory containing reference and test data (*i.e.*, the OUTCAR*
files) may be transferred to another machine if needed. For example, if the
machine used for job execution did not have Python3 installed, the respondent
may find it convenient to perform the validation elsewhere.

VASP bench1
-----------

*Benchmark 1* represents a typical high-accuracy band structure calculation,
involving bootstrapping from an initial approximate GGA wavefunction, through a
hybrid HSE function, to a final band structure from a GW calculation. The runs
as configured test scaling with respect to node count, at constant number of
ranks per node. Each run should have access to at least 64 GB of available
memory.  As a multi-stage job, there are three distinct INCAR files supplied.
The "std" VASP build (as opposed to Gamma-point-only or non-collinear builds)
should be used for this benchmark.

The key output files for validation are of the form `OUTCAR-{type}-{rankcount}`,
where `{type}` is one of `gga`, `hse`, or `gw`. We have supplied the relevant
reference data, with which test data will be compared.

Validation may be done either for individual files, or all at once after all the
requested runs are completed.  To validate individual files, run the
`validate.py3` script directly, providing the test file name (which must have
the format given above) as the sole argument. To run all validations at once,
you may run the `validate.bash` convenience script.

*GW calculations*: It should be noted that the GW method as implemented in VASP
currently does not take advantage of parallelism in the same manner that the GGA
and HSE methods do.  Thus, the rank counts used to demonstrate scaling for GGA
and HSE are excessive and beyond useful scaling for GW on the test calculation.
However, the supplied example PBS scripts are named by the GGA/HSE rank counts.
For the three example rank counts in {128, 256, 320} used for GGA and HSE, the
corresponding GW rank counts are {16, 32, 64}.

Three separate VASP GW validation references are supplied, as we have observed
slight differences in calculated band structure versus rank count. While these
differences would be unlikely to affect scientific conclusions, they do result
in validation failures in our hands at a reasonable level of numerical precision.
The supplied validation scripts take this into account automatically.

VASP bench2
-----------

*Benchmark 2* represents a typical surface catalysis study calculation, with
large unit cell and k-point sampling limited to the Gamma point. A single model
chemistry (DFT functional and plane-wave basis) is employed, and strong scaling
with respect to MPI rank count is of interest. The "gam" VASP build should
be used (as opposed to the general k-point std or non-collinear builds).

Validation is done per-run, and assumes the presence of a file or symlink `OUTCAR`
representing the test data. File `OUTCAR.ref` supplied by us carries the reference
data. Validation is achieved by running the `validate.py3` script with no
arguments in the presence of these two files.

For overall system throughput testing, this benchmark includes a configuration
requiring the Offeror to use a single node. For this configuration, the intent
is to minimize time-to-solution. To that end, the Offeror may subscribe the node
with MPI ranks, and configure VASP paralellism (_e.g._, by changing the NPAR
parameter in the INCAR file), as needed to achieve this goal.

What to Consider
----------------
The output times from the "time" Linux command as illustrated in the provided
example run scripts, converted to seconds. The "# cores" reported should reflect
the number of _physical_ cores hosting independent threads of execution,
and the "# workers" reported should be equal to that number of threads.

Files OUTCAR and vasprun.xml are useful records for each run done, as well as all
validation output.
