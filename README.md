# Data Science Salary Estimator
A data science project to estimate salary of Data Science jobs.

## Code and Resources Used
**Python Version**: 3.7  
**Packages**: pandas, numpy, matplotlib, sklearn, seaborn, flask, json, pickle  
**Python Requirements**: pip install -r requirements.txt  
**Flask Productionize Article**: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2  

## Dataset
Dataset are taken from glassdoor.com and for each job, we have information on:
* Job Title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Headquarters
* Company Size
* Company Founded Date
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors

## Data Cleaning
* Parsed salary data into integer
* Created columns for employer provided salary and hourly wages
* Removed rows with no salary
* Removed rating from out of Company Name
* Created a column for company state
* Created a column to describe if the company location is the same as its headquarter
* Converted founded date into company age
* Get job keyword from job description:
..* Python
..* R
..* AWS
..* Spark
..* Excel
* Created a column for simplified job title:
..* Data Scientist
..* Data Engineer
..* MLE
..* Analyst
..* Manager
* Created a column for job seniority:
..* Senior
..* Junior
* Created a column for job description length
