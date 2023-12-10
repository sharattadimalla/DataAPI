# DataAPI

## Goals

> Create a data API to share data in Databricks

## Demo

```
# Running the API
docker-compose up

# Submitting a data request

curl -X 'POST' \
  'http://127.0.0.1:18000/data' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "entity_name": "Individual",
  "key": "TIN",
  "value": "123-45-6789",
  "start_date": "string",
  "end_data": "string"
}'

# Get data request

curl -X 'GET' \
'http://127.0.0.1:18000/data/4f09eaf3-c98a-414e-b90c-9d2a9dfa6a83' \
  -H 'accept: application/json'

## Output
{
  "request_id": "4f09eaf3-c98a-414e-b90c-9d2a9dfa6a83",
  "status": "processing",
  "data": []
}
```

## High Level Functionality

- Authenticate & Authorize users
- Generate tokens to allow access to data with TTL
- Ability to request data
- Ability to download data
- Store data requests for audit

## API Design

### Pre-requisites

1. [Databricks SQL Warehouse](https://docs.databricks.com/en/compute/sql-warehouse/create-sql-warehouse.html#warehouse-sizing-and-autoscaling-behavior) is running

### Detailed Design

1. User submits data request to a public API and return a request_id
   - `client_id, requested_ts, request_info` log for `auditing`
   - Store request
2. User use `request_id` to verify status of request
3. Private api `polls` requests
4. Construct `SQLQuery`
5. `Private api` has permissions to execute query Databricks SQL Warehouse
6. `read` permission to allow running queries on `Databricks SQLWarehouse`
7. Private api queries `SQLWarehouse` and returns the data

## References

1. [databricks-sdk-py/examples](https://github.com/databricks/databricks-sdk-py/tree/main/examples)
