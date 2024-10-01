import pandas as pd
import json
import logging
from sqlalchemy import create_engine
from school_scores_etl_pipeline import extract, transform, load

raw_schools_scores = {
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


logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

try:
    # extract the scores data
    raw_schools_scores = extract(raw_schools_scores)
    
    # Clean the scores data
    cleaned_schools_scores = transform(normalized_data)
    
    # Define your PostgreSQL connection URL
    db_url = 'postgresql://username:password@localhost:5432/your_database'
        
    # Create a database connection
    db_engine = create_engine(db_url)
    
    # Load the cleaned data into PostgreSQL
    load(cleaned_schools_scores, db_engine)

	logging.info("Successfully extracted, transformed and loaded data.")  # Log a success message.
    
except Exception as e:
		logging.error(f"Pipeline failed with error: {e}")  # Log failure message


# Query the data from the schools_scores table and validate
to_validate = pd.read_sql("SELECT * FROM schools_scores", con=db_engine)
print(to_validate.head())

#checkpoint
# Check that the DataFrames are equal
print(to_validate.equals(cleaned_schools_scores))
