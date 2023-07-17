[My Microsoft Azure Home](microsoft_learn_home.md) > [Azure Relational Data Stores](azure_relational_data_stores.md) > [Azure SQL Database](azure_sql_database.md)


# Azure SQL Database HA and DR Options



## Geo Replication

### Use Cases

* can failover to secondary databse in case of outage
* migrate a database from one server to another in the same or cross region with minimal downtime

### Data Loss

* Uses the Always-on feature to replicate committed transactions to the secondary databse asynchronously
* may lag the primary database at any point in time

### Manual - Forced Failover

* This will make your secondary database immediately online and start accepting connections.
* Forced failover my result in data loss

### Issues

* only supports manual failover
* end-point connection must be changed in the application after the failover (problem for user applications)
* must have same firewall rules and logins to run apps successfully

* NB: Failover groups can get over the above issues because an endpoint is given to the failover group not the specific instance


## Failover Groups

Auto-failover groups is a declarative abstraction on top of the existing active geo-replication feature, designed to simplify deployment and management of geo-replicated databases at scale.

The auto-failover group adds convenience but also imposes limitations;

1. A listener concept enables your apps to take advantage of the same endpoint to your SQL, while with geo-replication your app is responsible for connection strings manipulation to target required SQL instance

2. On another hand, geo-replication supports multiple RO targets including in the same region, while failover group supports only two SQL instances in different regions, in which one is RW and another is RO

3. As validly pointed in another answer, SQL managed instances only support failover groups via vNet peering



## Links

[Udemy dp203 - Azure SQL DB Scaling](https://www.udemy.com/course/dp200exam/learn/lecture/23952350#overview)

[Azure Docs - Active geo-replication](https://learn.microsoft.com/en-us/azure/azure-sql/database/active-geo-replication-overview?view=azuresql)

[Azure Docs - Auto-failover groups](https://learn.microsoft.com/en-us/azure/azure-sql/database/auto-failover-group-sql-db?view=azuresql&tabs=azure-powershell)


