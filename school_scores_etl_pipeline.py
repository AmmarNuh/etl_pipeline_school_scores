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

# Print normalized testing scores
print(normalized_testing_scores)

# Create a DataFrame from the normalized_testing_scores list
normalized_data = pd.DataFrame(normalized_testing_scores)

# Set the column names
normalized_data.columns = ["school_id", "street_address", "city", "avg_score_math", "avg_score_reading", "avg_score_writing"]

# Set school_id as the index
normalized_data = normalized_data.set_index("school_id")

# Print the first few rows of the normalized DataFrame
print(normalized_data.head())
