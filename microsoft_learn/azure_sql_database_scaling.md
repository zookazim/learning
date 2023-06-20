[My Microsoft Azure Home](microsoft_learn_home.md) > [Azure Relational Data Stores](azure_relational_data_stores.md) > [Azure SQL Database](azure_sql_database.md)


# Azure SQL Database Scaling

Two types of scaling

## Vertical Scaling

* Scale up or down by adding compute power
* CPU, Memory, IO throughput and storage can be added
* Use DTU and vCore models to scale
* Dynamic Scalibility (not auto-scale)
* Any change is applied instantly (almost)


## Horizontal Scaling

* Scale out 
    * add more databases
    * use sharding

## Scale-Out


### Read-Only Scale Out
* can use read-only replicas for read-only work loads like analytics saving the write node from undue loads
* Require Premium (DTU) or Business Critical/Hyperscale (vCore)


### Global Scale Out/Sharing
* Split data into multiple nodes
* database shards are independent databases
* can access database shards in a region and not affect other shards
* Use cases
    * Data exceeds capability of single database
    * Tenants require physical isolation
    * Parts of database are required in different geographical regions (eg. specific region content)

    


## Links

[Udemy dp203 - Azure SQL DB Scaling](https://www.udemy.com/course/dp200exam/learn/lecture/27768948#overview)



