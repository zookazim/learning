[My Microsoft Azure Home](microsoft_learn_home.md) > [Batch Processing Home](azure_batch_processing.md) > [Azure Databricks](azure_databricks.md)

# Apache Spark

Spark is an open source unified analytics engine for large-scale data processing.

## 1. RDDs : Basic Building Blocks of Spark

All operations in Spark are performed on in-memory objects

Two types of in-memory objects;
* Action - Return value
* Apply Transformation

Characteristics of RDDs
* Partitioned - split across nodes in cluster
* Immutable - cannot be changed
* Resilient - Can be reconstructed even if a node crashes

### 1.1 Partitioned

RDDs are split across nodes in clusters so that parallel processing can occur


### 1.2 Immutable


### 1.3 Resilient

RDD can be created in two ways
* Reading a file
* Transforming another RDD

Every RDD keeps track of where it came from. 
It tracks it's own lineage this means that 
* the RDD can be reconstructed 
* allows RDD to be Lazily instantiated


## 2. Dataframes & Datasets

Laid out very similarly to a relational database table, data is stored in rows and columns


DataFrames are available in Python, R, Scala, Java but datasets are only avaialble in Scala and Java






## Links

[Microsoft Doco : Azure Data Factory](https://learn.microsoft.com/en-us/azure/databricks/)
