# Simple Data Retrieval API 

This API provides endpoints to retrieve information from a data source (currently an Excel file). It's designed to be easily configurable and demonstrates a basic API using Python and Flask.

## Overview

The API exposes two primary endpoints:

* `/get_id`: Retrieves the ID associated with a product name.
* `/get_info`: Retrieves specific information about a record based on its ID and column name.
* `/get_pregnancy_data`: Retrieves pregnancy risk data for a drug.

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
curl "http://{ENDPOINT}/get_id?name=Reactonz Women's Daily Vitality"
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
curl "http://{ENDPOINT}/get_info?id=483073&column=Sponsor Name"
```

### 3. **GET /get_pregnancy_data**

Retrieve pregnancy risk data for a drug based on its name.
#### Query Parameters:
- `name` (required): The name or partial name of the drug to search for.

#### Response:
Returns the pregnancy risk data for the first matching drug.
  ```json
  {
    "Category": "A",
    "Classification Level 1": "X",
    "Classification Level 2": "Y",
    "Classification Level 3": "Z"
  }
  ```

#### Example Usage:
```bash
curl "http://{ENDPOINT}/get_pregnancy_data?name=abacavir"
```

## Environment Variables

- `DATA_FILE`: Path to the Excel file. Defaults to `data.xlsx`.

## Deployment

The API was deployed on AWS using Elastic Beanstalk and S3. 