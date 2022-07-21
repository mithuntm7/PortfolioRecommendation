# Portfolio Recommendation

## IISc Data Engineering at Scale Project

## Problem Motivation

It’s the prime time for investments in stocks and cryptocurrencies in India:
Cryptocurrency investments in India increased from $923 million in April 2020 to almost $6.6 billion by May 2021, a 7X growth one year News Article
The holding of retail investors touched an all-time high of 7.18% in the June quarter
This motivates us to analyse the data available from these domains and build a simple application which helps users new to this world make investment decisions.

## Resources
1. Notebook for recommending portfolio.
2. Streamlit App Code for UI

## Instructions for Running Python Notebook
1. Unzip the Datasets Folder, the notebook has dependencies on datasets
2. Instructions for code under each headings (including sub-headings under each heading)
- **0. Setup - Pyspark, Google Drive, Yahoo Finance** : run as it is 
- **1. Default Imports and Path Definition** : change the _**path**_ variable to point to the Datasets Folder
- **2. Sample data download using yahoo finance and trading data plot** : run as it is 
- **3. Trading Data Fetcher** : ignore running this module as it fetches trading data for each asset (this would take 5+ minutes even for a single day's data fetch)
- **4. Function Definitions** : run as it is 
- **5. End to end functions in action** : run as it is 
- **6. Evaluation of sclaing** : google colab crahses/ doens't complete due to memory issues, please don't run this section


## Running instructions for the Streamlit Demo

Step 1 :Running ENTER_THE_NAME_OF THE_FILE.ipynb will output two csv files portfolio_recommendations.csv and coins_portfolio_recommendations.csv which has portfolio recommendations.

Step 2: This needs following packages to be installed for running the front-end using streamlit.

• pip install pandas

• pip install streamlit

Dashboard.py reads the questions to be asked to the user from risk_profile_quiz.txt and uses portfolio_recommendations.csv and coins_portfolio_recommendations.csv files generated in Step1 to display portfolio recommendations to the end user in a webpage hosted in localhost.

Run Dashboard.py using

• streamlit run Dashboard.py

This would automatically launch the webpage in the browser, in which end user answers questions and inputs investment amount to get portfolio recommendations.
