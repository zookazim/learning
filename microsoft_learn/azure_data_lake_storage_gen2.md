# Azure Data Lake Storage Gen2



![Data Lake Storage](images/azure_data_lake_storage.PNG)


## General Setup

Azure Data Lake Storage Gen2 is just standard blob storage with configuration changes. Click "Enable Hierarchical Namespace" when creating a storage account to turn it into Data Lake Gen2 storage.

Or you can use the Data lake Gen2 upgrade wizard if you want to convert an existing storage account.


## Comparing Data Lake Store to Azure Blob storage

### Blob storage
- stores large amounts of unstructured data 
- flat or single level hierarchy (ie no directories) 
- you can name the blobs with '/' for virtual folders but still single directory


### Data Lake Storage
- builds on blob storage
- optimises I/O of high volume data
- Hierarchical namespace (stores files in directories)
- stores metadata about each directories and the files contained within


### Stages for Processing Big Data

- **Ingest** -  identify processes and technology 
- **Store** - identify where the data will go
- **Prep and train** - Azure Synapse Analytics, Azure Databricks, HDInsight, Azure Machine Learning
- **Model and serve** - present data to users. PowerBI etc





## References

| Ref | Description | Link |
| --- | ------------------- | --------------- |
| 1 | Microsoft Learn Training | https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-data-lake-storage/1-introduction |
| 2 | Upload data exercise | https://learn.microsoft.com/en-us/training/modules/upload-data-to-azure-data-lake-storage/|

