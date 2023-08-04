[My Microsoft Azure Home](microsoft_learn_home.md)

[Azure Synapse Analytics](azure_synapse_analytics.md)


# Azure Synapse Data Types

## Overview

* Use the smallest type to support your data
* Avoid definining large sizes in character data sets
* Use varchar instead of nvarchar if this is sufficient - nvarchar uses twice the space
*

## Table Types

### Clustered Columnstore
* Updateable primary storage method
* Great for read only


* This is the default table type
* High compression ratio
* Ideally segments of 1M rows - load large amount of rows at a single time
* No secondary indexes


### Heap
* Data is not in any particular order
* use when data has no natural order

* No indexes possible
* Fast load
* No compression
* Allows secondary indexes


### Clustered Index
* An index that is physically stored in the same order as the data begin indexed

* Sorted index on the data
* Fast lookup of single row 
* No compression
* Allows secondary indexes


## Table Partitioning

### Features

* Enables division of data into smaller groups
* Improves efficiency of loading by use of partidion deletion, switching and merging
* Usually data is partitioned on a date column
* Can be used to improve query performance

### Why paritioning?

* Easy load or unload of data
* Easy maintenance
* Some query performance 

### Best Practice

* use relatively small number (max hundreds)
* remember table is split into 60 partitions even before custom partitions is created




