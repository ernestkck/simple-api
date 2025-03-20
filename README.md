# Simple Data Retrieval API 

This API provides endpoints to retrieve information from a data source (currently an Excel file). It's designed to be easily configurable and demonstrates a basic API using Python and Flask.

## Overview

The API exposes two primary endpoints:

* `/get_id`: Retrieves the ID associated with a product name.
* `/get_info`: Retrieves specific information about a record based on its ID and column name.

The path to the data file is configurable through an environment variable.

## Technologies Used

* Python
* Flask
* Pandas
* AWS Elastic Beanstalk


## Endpoints

### 1. **GET /get_id**

Retrieve the ID of the first row where the `Product Name` column contains a given name (case-insensitive, partial match).

#### Query Parameters:
- `name` (required): The name or partial name to search for in the `Product Name` column.

#### Response:
Returns the ID of the first matching row.
  ```json
  {
    "id": "123"
  }
  ```

#### Example Usage

```bash
curl "http://simple-api-env.eba-p2wxw3ar.ap-southeast-2.elasticbeanstalk.com/get_id?name=Example"
```

### 2. **GET /get_info**

Retrieve a specific value from the Excel file based on an `id` and a column name.

#### Query Parameters:
- `id` (required): The ID of the row to retrieve.
- `column` (required): The name of the column to retrieve the value from.

#### Response:
Returns the value from the specified column for the given ID.
  ```json
  {
    "value": "value_from_column"
  }
  ```
#### Example Usage:
```bash
curl "http://simple-api-env.eba-p2wxw3ar.ap-southeast-2.elasticbeanstalk.com/get_info?id=123&column=Product Name"
```

## Environment Variables

- `DATA_FILE`: Path to the Excel file. Defaults to `data.xlsx`.

## Deployment

The API was deployed on AWS Elastic Beanstalk. The current base URL is:

http://simple-api-env.eba-p2wxw3ar.ap-southeast-2.elasticbeanstalk.com