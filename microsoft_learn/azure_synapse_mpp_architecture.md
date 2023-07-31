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

## Round Robin

* Simplest 




## Links

[DP-203: Azure Synapse Architecture](https://www.udemy.com/course/dp200exam/learn/lecture/21655648#overview)



