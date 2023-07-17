[My Microsoft Azure Home](microsoft_learn_home.md) > [Azure Relational Data Stores](azure_relational_data_stores.md) > [Azure SQL Database](azure_sql_database.md)


# Azure SQL Database Backup and Restore


## Types

### Full Backup

* whole database
* taken once a week

### Differential Backup

* captures data changed since last full backup
* taken every 12 hours

### Transaction log Backup

* records committed and uncomitted transactions
* taken every 5-10 mins


## Storage Costs

Backup files copied to RA-GRS standard blob storage by default to paired region

## Backup Retention

### Backup storage redundancy

* point in time restore (PITR) - 7-35 days
* Long-term retention - up to 10 years

### Long term retention

* full backups can be taken for up to 10 years
* stored in RA-GRS blob storage


### LTR and Managed Instance

* LTR not yet available


## Backup Restore

Use cases

* pointin time restore of existing database
* point in timte restore of deleted database
* geo-restore (copy)


Restore time is impacted by;

* size of database and compute
* no of transaction logs and amount of activity
* network bandwidth
* concurrent restore requests being run




## Links

[Udemy dp203 - Azure SQL DB Backup and Restore](https://www.udemy.com/course/dp200exam/learn/lecture/27768976#overview)



