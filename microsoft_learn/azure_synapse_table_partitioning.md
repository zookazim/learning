[My Microsoft Azure Home](microsoft_learn_home.md)

[Azure Synapse Analytics](azure_synapse_analytics.md)


# Azure Synapse Table Partitioning


## Benefits of Partitioning

### Loading Data

* Primary benefit is to performance of loading data using partition deletion, switching and merging
* quickly remove or replace a section of a table eg. deleting old data can be very expensive because of transaction logs, removing an old partition is quick

### Queries

* Query performance can be improved by limiting the query to only a few partitions and excluding irrelevant data



## References

[Microsoft Docs - Synapse Table Partitioning](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/sql-data-warehouse-tables-partition)