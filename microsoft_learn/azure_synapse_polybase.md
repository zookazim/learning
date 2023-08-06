[My Microsoft Azure Home](microsoft_learn_home.md)

[Azure Synapse Analytics](azure_synapse_analytics.md)


# Azure Synapse Polybase

## Overview

PolyBase allows for parallel read and processing of data into the data warehouse. It is different from BCP, SSIS, Microsoft Data Factory in that it bypasses the Control Node (see [MPP Architecture](azure_synapse_mpp_architecture.md) )


## Polybase Setup

1. Create a Master Key
2. Create a database scoped credential with the storage key
3. Create an external data source
4. Create external file format
5. Create External Table
6. Load from External Table
