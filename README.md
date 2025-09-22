# Translation API Test Automation

This project automates testing for a simple translation API. The main objective is to verify that translations returned from the API match expected results. The tests are fully automated using pytest with mocked API responses.Logging
The test suite uses logging.info() to log which translation is being tested.

## Project Structure
### app/main.py	
Contains the get_translation() function and sample translation data
### app/config.py	
Configuration for BASE_URL
### tests/test_main.py	
Pytest test suite for get_translation()
### pytest.ini	
Pytest configuration (verbosity, reports)
### requirements.txt	
Python dependencies
### README.md	
Project documentation

## Setup Instructions

How to install requirements:
### pip install -r requirements.txt

Running the Tests (run from the project root directory):
### pytest
