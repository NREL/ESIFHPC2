ESIF-HPC-2 HiBench Benchmark
=========================

Licensing
---------
HiBench is licensed under the Apache License 2.0, see LICENSE.txt in the supplied HiBench distribution.<br />
Apache Maven is licensed under the Apache License 2.0, see LICENSE in the supplied Maven distribution.<br />
Scala is licensed under the 3-clause BSD license, as stated in the LICENSE.md file of the supplied distribution.

Description
-----------
This tar file contains Big Data (Hadoop/Spark) benchmarks for nodes with large memory.

The instructions below cover pre-requisites, configuration and deliverables.

These instructions and workload are applicable for a Hadoop cluster of **10 or fewer** nodes and have been tested on a canonical 5 node cluster.

How to Build
------------

### Pre-requisites
We have tested HiBench using the following prerequisites.

  * [Scala 2.11.8](https://scala-lang.org/download/all.html)
  * [Maven 3.3.9](https://archive.apache.org/dist/maven/maven-3/3.3.9/)
  * Python 2.7.5
  * [HDP](https://hortonworks.com/downloads/#data-platform) 2.5.3.0-37
  * [Spark 1.6](https://archive.apache.org/dist/spark/spark-1.6.3/)
  
For Scala and Maven, e.g.,

```
tar xvzf scala-2.11.8.tgz
tar xvzf apache-maven-3.3.9-bin.tar.gz
source rc
```

Note that you may need to customize the rc script with paths for your system.

### HiBench

More information is available at https://github.com/intel-hadoop/HiBench.

The distribution provided here must be used for testing (version 6.1, commit 70a4616).

```
unzip HiBench-master-70a4616.zip
```

### HTTPS woes

If you cannot get to HTTPS sites (e.g., are behind a proxy):

Put this text in ~/.m2/settings.xml to force maven to use the UK HTTP mirror:

```
<settings>
 <mirrors>
  <mirror>
    <id>UK</id>
    <name>UK Mirror</name>
    <url>http://uk.maven.org/maven2</url>
    <mirrorOf>*</mirrorOf>
  </mirror>
 </mirrors>
</settings>
```

Replace pom.xml with the version given here (with HTTP repos).

### Build HiBench

Finally, build:

```
mvn -Dspark=1.6 -Dscala=2.11.8 clean package
```

How to Run
----------
Note: bigdata profile includes these input data sizes:

  * Sort: 300GB
  * Wordcount: 1.6T
  * Bayes: ~60GB (20M pages)
  * K-Means: ~5GB (1.2B samples)
  * DFSIOE: 2.04T

### Configuration

The following files will need to be configured as appropriate for the system under test. Examples for our baseline system are given.

**conf/hadoop.conf**

```
# Hadoop home
hibench.hadoop.home     /usr/hdp/2.5.3.0-37/hadoop

# The path of hadoop executable
hibench.hadoop.executable     ${hibench.hadoop.home}/bin/hadoop

# Hadoop configraution directory
hibench.hadoop.configure.dir  ${hibench.hadoop.home}/etc/hadoop

# The root HDFS path to store HiBench data
# Note: this must match the setting used in HDFS core-site.xml fs.defaultFS or dfsioe will give errors
hibench.hdfs.master       hdfs://nrelhdfs

# Hadoop release provider. Supported value: apache, cdh5, hdp
hibench.hadoop.release    hdp
```
**conf/hibench.conf**

```
# Data scale profile. Available value is tiny, small, large, huge, gigantic and bigdata.
# The definition of these profiles can be found in the workload's conf file i.e. conf/workloads/micro/wordcount.conf
hibench.scale.profile                  gigantic

# Mapper number in hadoop, partition number in Spark
hibench.default.map.parallelism         32

# Reducer nubmer in hadoop, shuffle partition number in Spark
hibench.default.shuffle.parallelism     32
```

**conf/spark.conf**

```
# Spark home
hibench.spark.home      /usr/hdp/2.5.3.0-37/spark

# Spark master
#   standalone mode: spark://xxx:7077
#   YARN mode: yarn-client
hibench.spark.master    yarn-client

# executor number and cores when running on Yarn
hibench.yarn.executor.num     20
hibench.yarn.executor.cores   5

# executor and driver memory in standalone & YARN mode
spark.executor.memory  23g
spark.driver.memory    23g
```

### Run Benchmarks

#### Wordcount

```
bin/workloads/micro/wordcount/prepare/prepare.sh
bin/workloads/micro/wordcount/hadoop/run.sh
bin/workloads/micro/wordcount/spark/run.sh
```

#### Sort

```
bin/workloads/micro/sort/prepare/prepare.sh
bin/workloads/micro/sort/hadoop/run.sh
bin/workloads/micro/sort/spark/run.sh
```

#### Bayes

```
bin/workloads/ml/bayes/prepare/prepare.sh
bin/workloads/ml/bayes/hadoop/run.sh
bin/workloads/ml/bayes/spark/run.sh
```

#### K-Means

```
bin/workloads/ml/kmeans/prepare/prepare.sh
bin/workloads/ml/kmeans/hadoop/run.sh
bin/workloads/ml/kmeans/spark/run.sh
```

#### DFS I/O Enhanced

```
bin/workloads/micro/dfsioe/prepare/prepare.sh
bin/workloads/micro/dfsioe/hadoop/run.sh
```

