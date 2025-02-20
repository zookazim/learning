[Azure Synapse Home](azure_synapse_analytics.md)

# Azure Synapse : Serverless SQL Pools



## Overview

Every Azure Synapse Analytics workspace comes with serverless SQL pool endpoints that you can use to query your data.

Serverless SQL pool is a query service over the data in your data lake.


## Serverless SQL Pool Benefits

Suitable for the following;

* Basic discovery and exploration
* Logical data warehouse
* Data transformation - simple, scalable and performant way to transform data in the data lake using T-SQL and fed to BI tools

Team roles can benefit;
* Data Engineers - explore data in the lake, tansofmr and prepare data
* Data Scientists - quickly see the content and structure of files
* Data Analysts - explore data using T-SQL and spark using their favourite tools


## T-SQL support

### Supported

* any tool that connects to SQL database can connect to the SQL endpoint
* Databases - multiple databases
* Views, stored procs, file formats and tables

### Security

* Logins and users
* Credentials to control access to storage accounts
* Grant, deny and revoke permissions per object level
* Microsoft Entra integration

### Supported T-SQL

* Full SELECT surface area in including most sql functions
* CETAS
* DDL statements related to views and security only

### Not supported

Serverless SQL pool has no local storage, data cannot be stored eg. in tables or materialised views.

* DML :-(
* Tables
* Triggers
* Materialised views


## Links

* [Microsoft Learn : Serverless SQL](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql/on-demand-workspace-overview)



* [Microsoft Learn : Use Azure Synapse SQL Pool to query files in a data lake](https://learn.microsoft.com/en-us/training/modules/query-data-lake-using-azure-synapse-serverless-sql-pools/)