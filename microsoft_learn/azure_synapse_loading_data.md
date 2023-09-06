[My Microsoft Azure Home](microsoft_learn_home.md)

[Azure Synapse Home](azure_synapse_home.md)


# Azure Synapse Loading Data

## Different Loading Methods

### Single Client
1. SSIS
2. Azure Data Factory
3. BCP
4. Can add some parallel capabilities but bottlenecked at control node

### Parallel loading methods
1. PolyBase
    * Reads from Azure blob storage and loads contents to Azure SQL DW
    * Bypasses the Control Node and loads directly into the Compute Node



## Loading with SSIS




## Links

[Install Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash#install-the-azure-functions-core-tools)



