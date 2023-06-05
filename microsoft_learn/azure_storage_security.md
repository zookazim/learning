[My Microsoft Azure Home](microsoft_learn_home.md)

[Azure Storage Home](azure_storage.md)


# Authentication

## Storage Account Keys

* Also called shared keys

* This authentication option is one of the easiest to use, and it supports blobs, files, queues, and tables. The client embeds the shared key in the HTTP Authorization header of every request, and the Storage account validates the key.

* Use only in house - not suitable for third parties

* Shared keys can be regenerated

* the keys do not expire automatically

## Shared Access Signature (SAS)

* You'd typically use a SAS for a service where users read and write their data to your storage account

* SAS delegates access to blob containers in a storage account with granular control over how the client accesses your data.

* You can define a SAS token to allow access only to a specific blob container with a defined expiration


## Azure Active Directory (Azure AD)



# Access Control

## Role Based Access Control (RBAC)

## Access Control List (ACL)


 
# Network Access

## Firewall and Virtual Networks




## Links


[MS Learn - Azure Storage Security](https://learn.microsoft.com/en-us/training/modules/secure-azure-storage-account/)


[Grant limited access to blob storage through Shared Access Signature](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)

[Authorise with a Shared Key](https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-with-shared-key)