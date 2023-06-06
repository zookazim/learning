[My Microsoft Azure Home](microsoft_learn_home.md)

[Azure Relational Data Stores](azure_relational_data_stores.md)


# Azure SQL

## Features

* Fully Managed
* Predictable performance and pricing
* Elastic pool for unpredictable workloads
* 99.99% availability built-in
* Geo-replication and restore services
* Supports existing SQL Server tools, libraries and APIs
* Scalablility with no downtime
* Security : Secure and compliant for sensitive data


## Azure SQL Services

### IaaS - Infrastucture as a Service

* SQL server inside a fully-managed VM
* Maintenance on the 
    ** VM maintenance and patches required
    ** db maintenance is still required by users eg. no patching, scaling
    ** backups must be setup
    ** security is user responsiblity VM connection, database etc.
* good for lift and shift from on-prem
* full control of database engine
    * can control when patching happens
    * start stop VM to save costs
    * use pay-as-you-go
* can bring your own license
* Limitiations
    * generally more expensive as you are paying for underlying infrastructure
    * Availability : can be affected by underlying infrastructure and your network setup for example


### PaaS - Platform as a Service

* AKA Database as a Service
* simply create Azure SQL resource
* only create database and tables
* no patching, backups etc.
* can benefit from only PaaS additional features
    ** high availability
* pay-as-you-go service
    ** easy scale up or scale out without interuption
* responsibility for user
    ** choosing right service tier
    ** high availability and disaster recovery is setup but must be tested
    ** change control in database
    ** security - eg. logins, roles, users
* Limitation
    * Vendor lock in - harder to migrate away
    * Customisation - less flexible
    * Limited control - have less ability to configure the database for your needs
    * Compatibility - less compatible with third part applications or tools





## Links

[Install Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash#install-the-azure-functions-core-tools)



