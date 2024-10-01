# ETL Pipeline for School Scores

This repository contains an ETL (Extract, Transform, Load) pipeline that processes nested JSON data representing school scores. The pipeline normalizes the data and prepares it for analysis using Pandas.

## Project Overview

The JSON file `nested_school_scores.json` is read into a dictionary, and the following steps are performed:

1. **Extract**: Read the JSON data into a Python dictionary.
2. **Transform**: Normalize the data by extracting relevant fields and converting them into a structured format.
3. **Load**: Create a Pandas DataFrame for further analysis.

## Data Structure:

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

## Output Structure:

The output data is structured as follows:

```SQL
                 street_address       city  avg_score_math  avg_score_reading  avg_score_writing
school_id                                                                                       
02M260     425 West 33rd Street  Manhattan             NaN                NaN                NaN
06M211       650 Academy Street  Manhattan             NaN                NaN                NaN
01M539      111 Columbia Street  Manhattan           657.0              601.0              601.0
02M294         350 Grand Street  Manhattan           395.0              411.0              387.0
02M308         350 Grand Street  Manhattan           418.0              428.0              415.0
```

## Dependencies
  1. Python 3.x
  2. Pandas


## Usage
  1. Clone the repository.
  2. Install the required dependencies (if any).
  3. Place the nested_school_scores.json file in the same directory as the script.
  4. Run the script to see the normalized data output.
