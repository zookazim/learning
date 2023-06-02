[My Microsoft Azure Home](microsoft_learn_home.md)

[Azure Storage](azure_storage.md)


# Azure Disk Storage

* VM uses disks to store OS files, applications and data
* A VM can have one OS disk and mulitple data disks
* The OS disk and data disk are virtual hard disks (VHDs) stored in an Azure storage account
* VHDs in Azure are .vhd files stored as page blobs in a storage account

## Unmanaged disks (not recommended)
* we create the storage account and specifiy it when creating the disk

## Managed disks
* Azure create and manages storage accounts in the background
* Scalability issues are taken cares of
* disks are managed based on the size and performance tier

## Managed disk types

* Standard HDD : Backup, non-critical, infrequent access
* Standard SSD : lightly used production applications. Dev/Test environments
* Premium SSD : Super fast and high performance, low latency. Use for production
* Ultra disks (SSD) : most demanding and IO intensive loads, top tier database use

## Links




