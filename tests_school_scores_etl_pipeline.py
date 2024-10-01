from school_scores_etl_pipeline import extract, transform, load
import pytest


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

# Create a pytest fixture
@pytest.fixture()
def raw_school_data():
	raw_data = extract(raw_schools_scores)
    
    # Return the raw DataFrame
	return raw_data
    
def test_transformed_data(raw_school_data):
    clean_school_data = transform(raw_school_data)
    
    # Assert that the transform function returns a pd.DataFrame
    assert isinstance(clean_school_data, pd.DataFrame)
    
    # Assert that the clean_tax_data DataFrame has more columns than the raw_tax_data DataFrame
    assert len(clean_school_data.columns) > len(raw_school_data.columns)


# run the test: python -m pytest 
