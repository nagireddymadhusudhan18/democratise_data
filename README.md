# Youtube Engagement Score

## Description of Problem statement

Given set of of keywords , get the engagement score for any of 100 keywords on youtube.com  

Split this data based on country
 (get this data for usa and india only (but have the code flexible to add more )) 
Split this data based on category
 ( Ready to Eat, Snacks, Beverages, Alocholic Beverages (but have the code flexible to add more ) 
Required Componenets to run the Application

## Installation or required Components

1. Python 3.X. [ import modules (googleapiclient, numpy, pandas) if not available ] 
2. Google Youtube API access Key.

## File Structure:

1. configuration.py - Contains the configuration details like the API key to connect to Youtube V3 API and the required country's input list
2. keywords.xlsx - Contains the list of input keywords for calculating the engagement score
3. youtube_eng_score.py - Python program application file for calculating the engagement score
4. country-codes_csv.csv - Contains the country code mapping as input to youtube.search().list() API
5. YT_engagement_score.ipynb - Jupyter file for ease of code expansion
6. Youtube Eng score.drawio.pdf - Contains the flow daigram of the application program
   
## Input required for the application program

1. Edit the list of Keywords in a keywords.xlsx file.
2. List of country's for slicing the engagement score for given set of keywords.

## Usage
1. Download/Clone the git repository to your local.
2. Edit the input .xls(keywords.xlsx) file to modify the required keywords to get the engagement score.
3. Edit configuration.py to update the Google Youtube API key and list of country's for the input.
4. Required country list code has to be fetched from the country-codes_csv.csv file for country mapping codes
5. Run the python file using the command

   _pyhton3 youtube_eng_score.py_

## Roadmap

version 2

Furthur the program will accept video category's as the input to slice the engagement score for given set of keywords into grain of each country and video category.

## 





