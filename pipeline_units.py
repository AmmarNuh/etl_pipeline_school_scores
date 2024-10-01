import pandas as pd
import json
import logging


def extract(raw_data):

	normalized_schools_scores = []
	
	# Loop through each of the dictionary key-value pairs
	for school_id, school_info in raw_data.items():
		normalized_schools_scores.append([
	    	school_id,
	    	school_info.get("street_address"),  # Pull the "street_address"
	    	school_info.get("city"),
	    	school_info.get("scores").get("math", 0),
	    	school_info.get("scores").get("reading", 0),
	    	school_info.get("scores").get("writing", 0),
	    ])
	
		print(normalized_schools_scores)
		
		# Create a DataFrame from the normalized_schools_scores list
		normalized_data = pd.DataFrame(normalized_schools_scores)
		
		# Set the column names
		normalized_data.columns = ["school_id", "street_address", "city", "avg_score_math", "avg_score_reading", "avg_score_writing"]
		
		normalized_data = normalized_data.set_index("school_id")
		print(normalized_data.head())
		
		logging.info('Data extracted succssfuly')

#----------------------
  # Define a function to find the street name
def find_street_name(row):
    return ' '.join(row['street_address'].split()[1:])

#----------------------

# Define a function to transform and clean the data
def transform(raw_data):
    # Use .loc[] to only return the needed columns
    raw_data = raw_data.loc[:, ["city", "math_score", "reading_score", "writing_score"]]
        
    # Add street name extraction
   # raw_data["street_name"] = raw_data.apply(find_street_name, axis=1)
    
    # Fill NaN values with column mean for scores
    raw_data.fillna(
        value={
            "math_score": raw_data["math_score"].mean(),
            "reading_score": raw_data["reading_score"].mean(),
            "writing_score": raw_data["writing_score"].mean()
        },
        inplace=True
    )
	
    logging.info('Data transformed succssfuly')
	
    return raw_data

#----------------------

# Function to load cleaned data into PostgreSQL
def load(clean_data, con_engine):
    # Store the data in the school's database
    clean_data.to_sql(
        name="schools_scores",
        con=con_engine,
        if_exists="replace",  # Make sure to replace existing data
        index=True,
        index_label="school_id"
    )
