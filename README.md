# ETL Pipeline for School Scores

This repository contains an ETL (Extract, Transform, Load) pipeline that processes nested JSON data representing school scores. The pipeline normalizes the data and prepares it for analysis using Pandas.

## Project Overview

The JSON file `nested_school_scores.json` is read into a dictionary, and the following steps are performed:

1. **Extract**: Read the JSON data into a Python dictionary.
2. **Transform**: Normalize the data by extracting relevant fields and converting them into a structured format. This step includes cleaning the data to fill in missing values.
3. **Loading Data to PostgreSQL**:

   After data has been extracted and transformed, it can be loaded into a PostgreSQL database for easy access and querying. This                repository provides functionality to load cleaned data into a PostgreSQL database.
4. **Unit Tests**: adding end-to-end tests and checkpoints to ensure pipeline quality.
### Requirements

Make sure you have the following installed:

- PostgreSQL server running
- SQLAlchemy (`pip install sqlalchemy psycopg2`)
## Data Structure:

The input data is structured as follows:

```json
{
    "school_id": ["02M260", "06M211", "01M539", "02M294", "02M308"],
    "street_address": [
        "425 West 33rd Street",
        "650 Academy Street",
        "111 Columbia Street",
        "350 Grand Street",
        "350 Grand Street"
    ],
    "city": ["Manhattan", "Manhattan", "Manhattan", "Manhattan", "Manhattan"],
    "math_score": [None, None, 657.0, 395.0, 418.0],
    "reading_score": [None, None, 601.0, 411.0, 428.0],
    "writing_score": [None, None, 601.0, 387.0, 415.0]
}
```

## Output Structure:

The output data is structured as follows:

```SQL
 school_id        street_address       city  math_score  reading_score  writing_score       street_name

02M260      425 West 33rd Street  Manhattan     432.944        424.504        418.459  West 33rd Street
06M211        650 Academy Street  Manhattan     432.944        424.504        418.459    Academy Street
01M539       111 Columbia Street  Manhattan     657.000        601.000        601.000   Columbia Street
02M294          350 Grand Street  Manhattan     395.000        411.000        387.000      Grand Street
02M308          350 Grand Street  Manhattan     418.000        428.000        415.000      Grand Street
```

The final output data in PostgreSQL:

```SQL
      school_id       street_address       city  math_score  reading_score  writing_score  city_rank
    0    01M539  111 Columbia Street  Manhattan       657.0          601.0          601.0        4.0
    1    02M294     350 Grand Street  Manhattan       395.0          411.0          387.0       54.0
    2    02M308     350 Grand Street  Manhattan       418.0          428.0          415.0       41.0
    3    02M545     350 Grand Street  Manhattan       613.0          453.0          463.0       18.0
    4    01M292     220 Henry Street  Manhattan       410.0          406.0          381.0       52.0
```

## Dependencies
  1. Python 3.x
  2. Pandas


## Usage
  1. Clone the repository.
  2. Install the required dependencies (if any).
  3. Place the nested_school_scores.json file in the same directory as the script.
  4. Set your PostgreSQL connection URL in the script.
  5. Run the script to load the cleaned data into the specified table.
  6. The script will print the first few rows of the loaded data for validation.
