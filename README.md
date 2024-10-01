# ETL Pipeline for School Scores

This repository contains an ETL (Extract, Transform, Load) pipeline that processes nested JSON data representing school scores. The pipeline normalizes the data and prepares it for analysis using Pandas.

## Project Overview

The JSON file `nested_school_scores.json` is read into a dictionary, and the following steps are performed:

1. **Extract**: Read the JSON data into a Python dictionary.
2. **Transform**: Normalize the data by extracting relevant fields and converting them into a structured format.
3. **Load**: Create a Pandas DataFrame for further analysis.

## Data Structure

The input data is structured as follows:

```json
{
    "01M539": {
        "street_address": "111 Columbia Street",
        "city": "Manhattan",
        "scores": {
              "math": 657,
              "reading": 601,
              "writing": 601
        }
    },
    ......
}
```



## Dependencies
  Python 3.x
  Pandas


## Usage
  Clone the repository.
  Install the required dependencies (if any).
  Place the nested_school_scores.json file in the same directory as the script.
  Run the script to see the normalized data output.
