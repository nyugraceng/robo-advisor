# robo-advisor

Overview 
This is the Robo Advisor project for our Python class: https://github.com/prof-rossetti/intro-to-python/blob/main/projects/robo-advisor/README.md 
In essence, the output allows the user to pull stock data from an API at a certain point in time to be able to see the latest close, recent high, recent low, recommendation and why of a stock. 

Instructions
You can clone my Repo from: https://github.com/nyugraceng/robo-advisor 

You will need to choose a stock ticker API: https://www.alphavantage.co/documentation/. We will be using the Time Series Daily API. 

Packages
You will need to install certain packages in order to proceed:
1. CSV 
2. JSON
3. OS 
4. pandas
5. pip install requirements 

Files and functions 
You will need an environment file (.env) to store your secret API key, obtainable for free from alphavantage website. Copy and paste the key, defined "ALPHAVANTAGE_API_KEY="inputyourAPIkey". By defining it, you can then use the os package to get the script to obtain this key from your environment. 

Please ensure you create a gitignore file and a read me file when you create your own repository. This ensures that your personal API key will not be uploaded onto GitHub.

You will need to use the to_usd function to format prices. 

Data CSV file 
You will need to create a data folder and a csv file to store the data. 
