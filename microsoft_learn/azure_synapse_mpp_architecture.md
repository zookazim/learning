[My Microsoft Azure Home](microsoft_learn_home.md)

[Azure Synapse Analytics](azure_synapse_analytics.md)


# Azure Synapse MPP Architecture

## Overview

![Azure Synapse MPP](images/azure_synapse_mpp_architecture.png)


## Storage

Data is sharded
Distribution - basic unit of storage
Rows stored across 60 distributions

## Sharding Patterns

* Hash
* Round Robin
* Replicated

### Replicated Tables

* Full copy of table is stored on each node
* Used for small tables
* 

### Round Robin

* Simplest 
* quick to load
* data is destributed evenly without additional optimisation
* joins are slow and query performance better with hash

### Hash 
* hash has best performance for large tables
* each row belongs to one particular distribution
* used mostly for larger tables


### Distribution Key

* Good key
    * distribute evenly
    * used for grouping
    * used as join
    * hash column is not updatable
    * has more than 60 distinct values (number of nodes)

### What distribution should I use

|Type|Good for|Watch out for|
|----|--------|-------------|
|Replicated|Small dimension tables|Many write transactions which are not good|
|||Changing DWU provisioning frequently|
|||Use only 2-3 columns but your table has many cols|
|Round Robin|Temp/Staging table|Performance is slow|
||No obvious join column||
|Hash|Fact tables|Distribution key can't be updated|
||Large Dimension Tables||


## Links

[DP-203: Azure Synapse Architecture](https://www.udemy.com/course/dp200exam/learn/lecture/21655648#overview)



