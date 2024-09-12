[My Microsoft Azure Home](microsoft_learn_home.md) > [Batch Processing Home](azure_batch_processing.md)

# Azure Databricks

An instance of Databricks offered by Microsoft that has been optimised for the Azure Cloud and offers native Microsoft connectors etc as a result of this integration.

## 1. Clusters

Cluster Types
* Interactive
* Automatic

### 1.1 Interactive

* interactively analyse the data
* created by users
* manually terminate
* option to auto terminate if inactive
* low execution time
* auto scale on demand
* comparitively costly

### 1.2 Job Clusters

* run automated jobs
* auto created when job starts
* terminates when job ends
* cannot be created or terminated
* high throughput
* auto scale on demand
* comparitively cheaper

### 1.3 Cluster Modes

#### 1.3.1 Standard Mode

* Single user
* No fault isolation
* no task preemption
* each user requires separate cluster
* support Scala, Python, SQL, R, Java

#### 1.3.2 High Concurrency Mode

* Multiple users
* Fault isolation
* Task preemption - fair resource sharing
* Maximum cluster utilisation
* Only support Python, SQL, R


## 2. Workspaces



## 3. Notebooks


## 4. Jobs


## 5. Libraries

* install third party libraries on cluster


## 6. Database and Tables

* create databases and tables

Tables
* collection of structure data
* equivalent to dataframe
* created using file on storage
* directly query or write to tables




## Links

[Microsoft Doco : Azure Data Factory](https://learn.microsoft.com/en-us/azure/databricks/)
