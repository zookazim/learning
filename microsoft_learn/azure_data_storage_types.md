[My Microsoft Azure Home](microsoft_learn_home.md) > [Azure Data Solution Design](azure_data_solution_design.md)

# Data Storage Types

## Relational Database Management Systems (RDBMS)

### Data Structure
* Schema-on-write
* Normalised
* Relationships enforced using database constraints

### Operation

* Structured Query Language (SQL)
* ACID (Atomic, Consistent, Isolated, Durable) for read write consistency


## Key Value Stores

### Data Structure

* Each data value associated with a unique key
* scalable
* no relationship between entities

### Operation

* Simple insert/delete operation
* highly optimised for performing simple lookups

### Examples

* data caching
* session management
* environment variables


### Azure Services

* Azure Cosmos DB
* Azure Cache for Redis

## Links

