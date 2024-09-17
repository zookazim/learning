[My Microsoft Azure Home](microsoft_learn_home.md)


# Azure Stream Analytics

Azure Stream Analytics is a fully managed stream processing engine that is designed to analyze and process large volumes of streaming data with sub-millisecond latencies. You can build a streaming data pipeline using Stream Analytics to identity patterns and relationships in data that originates from various input sources including applications, devices, sensors, clickstreams, and social media feeds. Then, you can use these patterns to trigger actions and initiate workflows such as raising alerts, feeding information to a reporting tool, or storing transformed data for later use. Stream Analytics is also available on the Azure IoT Edge runtime, which enables you to process data directly from IoT devices.


![Stream Analytics](images/stream-analytics-e2e-pipeline.png)




## 1. Stream Analytics

Stream Analytics is a big data analytics solution that allows you to analyze real-time events.

The input data source can be an event hub, an IoT hub, blob storage or SQL Server.

The reference input is data that never or rarely changes. Reference data can be saved in Azure SQL Database or Blob storage

[Microsoft Docs : What is Azure Stream Analytics](https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-introduction)



## 2. Event Hubs

Event Hub is an Azure resource that allows you to stream big data to the cloud.

Event Hub accepts streaming telemetry data from other sources. It is basically a big data pipeline. It allows you to capture, retain, and replay telemetry data

It accepts streaming data over HTTPS and AMQP (Advanced Message Queuing Protocol).

A Stream Analytics job can read data from Event Hubs and store the transformed data in a variety of output data sources, including Power BI.


## 3. IOT Hub

IoT Hub is an Azure resource that allows you to stream big data to the cloud.

It supports per-device provisioning.

It accepts streaming data over HTTPS, AMQP, and Message Queue Telemetry Transport (MQTT).

A Stream Analytics job can read data from IOT Hubs and store the transformed data in a variety of output data sources, including Power BI.


## 4. Windowing Functions

[Windowing Functions](azure_data_factory.md)


## Links


[Microsoft Docs : What is Azure Stream Analytics](https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-introduction)

