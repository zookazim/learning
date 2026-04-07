[My Azure Synapse Notes](my_synapse_notes.md) > [Synapse Queries](synapse_queries.md)



## 1. Simple Read a CSV

```
select top 10 *
from openrowset(
    bulk 'https://pandemicdatalake.blob.core.windows.net/public/curated/covid-19/ecdc_cases/latest/ecdc_cases.csv',
    format = 'csv',
    parser_version = '2.0',
    firstrow = 2 ) as rows
```

```
select * --count(*) rec_count
from openrowset(
    bulk 'https://wahmhcbdazestsilver.blob.core.windows.net/silver/transactional/c3_aodmds/*/dsp_validation_report.csv',
    format = 'csv',
    parser_version = '2.0',
    firstrow = 2 )
    WITH (
         app_id VARCHAR(1000)
        ,severity VARCHAR(1000)
        ,edit VARCHAR(1000)
        ,validation_check VARCHAR(1000)
        ,agency_id VARCHAR(1000)
        ,client_id VARCHAR(1000)
        ,episode_id VARCHAR(1000)
        ,start_date VARCHAR(1000)
        ,end_date VARCHAR(1000)
    ) 
    AS epi
WHERE validation_check = 'THASP longer than 180 days'
;
```

## 2. Querying Data in a Folder


```
SELECT  *, nyc.filepath(1) AS [year], nyc.filepath(2) AS [month]
FROM OPENROWSET(
        BULK 'csv/taxi/yellow_tripdata_*-*.csv',
        DATA_SOURCE = 'SqlOnDemandDemo',
        FORMAT = 'CSV', 
        FIRSTROW = 2
    )
    WITH (
          vendor_id VARCHAR(100) COLLATE Latin1_General_BIN2, 
          pickup_datetime DATETIME2, 
          dropoff_datetime DATETIME2,
          passenger_count INT,
          trip_distance FLOAT,
          rate_code INT,
          store_and_fwd_flag VARCHAR(100) COLLATE Latin1_General_BIN2,
          pickup_location_id INT,
          dropoff_location_id INT,
          payment_type INT,
          fare_amount FLOAT,
          extra FLOAT,
          mta_tax FLOAT,
          tip_amount FLOAT,
          tolls_amount FLOAT,
          improvement_surcharge FLOAT,
          total_amount FLOAT
    ) AS nyc
```

## 4. Joining data from file with data warehouse table

```
select ambu.region_id
      ,ambu.ambulatory_id
      ,ambu.ambulatory_name
      ,ambu.clients
      ,ambu.contacts
      ,ambu_cmhc.NPersons as cmhc_clients
      ,ambu_cmhc.Contacts as cmhc_contacts
  from a1_mhe.dbo.fact_ambulatory ambu
  join openrowset(
    bulk 'https://wahmhcbdazestraw.blob.core.windows.net/raw/transactional/a1_mhe/ambu_cmhc.csv',
    format = 'csv',
    parser_version = '2.0',
    firstrow = 2 )
    WITH (
         RegId VARCHAR(1000) COLLATE Latin1_General_100_BIN2_UTF8
        ,orgid VARCHAR(1000) COLLATE Latin1_General_100_BIN2_UTF8
        ,ClusId VARCHAR(1000) COLLATE Latin1_General_100_BIN2_UTF8
        ,AmbuId VARCHAR(1000) COLLATE Latin1_General_100_BIN2_UTF8
        ,AmbuName VARCHAR(1000) COLLATE Latin1_General_100_BIN2_UTF8
        ,NPersons VARCHAR(1000) COLLATE Latin1_General_100_BIN2_UTF8
        ,Contacts VARCHAR(1000) COLLATE Latin1_General_100_BIN2_UTF8
    ) AS ambu_cmhc ON ambu.ambulatory_id = ambu_cmhc.AmbuId

 where ambu.fin_year = '2024/25'
 order BY
       ambu.region_id
```


## 4. Delta File History

You can view history using a timestamp or a version number. Query the versions from DESCRIBE HISTORY sql command;

```
describe a1_mhe.fact_admitted

describe history a1_mhe.fact_admitted
```

Return data from a particular version;

```
SELECT count(*) FROM a1_mhe.fact_admitted VERSION AS OF 0;
```