import pandas as pd
import json

# Load the JSON data
with open("nested_school_scores.json", "r") as file:
    raw_testing_scores = json.load(file)

normalized_testing_scores = []

# Loop through each of the dictionary key-value pairs
for school_id, school_info in raw_testing_scores.items():
    normalized_testing_scores.append([
        school_id,
        school_info.get("street_address"),
        school_info.get("city"),
        school_info.get("scores").get("math", 0),
        school_info.get("scores").get("reading", 0),
        school_info.get("scores").get("writing", 0),
    ])

# Create a DataFrame from the normalized_testing_scores list
normalized_data = pd.DataFrame(normalized_testing_scores)

# Set the column names
normalized_data.columns = ["school_id", "street_address", "city", "math_score", "reading_score", "writing_score"]

# Set school_id as the index
normalized_data = normalized_data.set_index("school_id")

# Define a function to find the street name
def find_street_name(row):
    return ' '.join(row['street_address'].split()[1:])


# Define a function to transform and clean the data
def transform(raw_data):
    # Use .loc[] to only return the needed columns
    raw_data = raw_data.loc[:, ["city", "math_score", "reading_score", "writing_score"]]
    
    # Group the data by city, return the grouped DataFrame
    grouped_data = raw_data.groupby(by=["city"], axis=0).mean()
    
    # Add street name extraction
    raw_data["street_name"] = raw_data.apply(find_street_name, axis=1)
    
    # Fill NaN values with column mean for scores
    raw_data.fillna(
        value={
            "math_score": raw_data["math_score"].mean(),
            "reading_score": raw_data["reading_score"].mean(),
            "writing_score": raw_data["writing_score"].mean()
        },
        inplace=True
    )
    
    return grouped_data

# Clean the testing scores
grouped_testing_scores = transform(normalized_data)

# Print the first few rows of the grouped DataFrame
print(grouped_testing_scores.head())
