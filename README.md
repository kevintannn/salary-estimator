# Data Science Salary Estimator
A data science project to estimate salary of Data Science jobs.

## Code and Resources Used
**Python Version**: 3.7  
**Packages**: pandas, numpy, matplotlib, sklearn, seaborn, flask, json, pickle  
**Python Requirements**: pip install -r requirements.txt  
**Flask Productionize Article**: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2  

## Dataset
Dataset is collected from glassdoor.com and for each job, we have information on:
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
Perform data cleaning on collected dataset.
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
* Created a column for company competitors count

## Exploratory Data Analysis
Observed some data properties, distributions, and value counts for various categorical data.  
Few highlights from pivot tables:  
![image](https://user-images.githubusercontent.com/48116781/174987450-5ff35cac-f7e5-4f05-bae7-083dc471d0ff.png)
![image](https://user-images.githubusercontent.com/48116781/174987630-2a244070-65db-4186-bb6d-b92357ed67dd.png)
![image](https://user-images.githubusercontent.com/48116781/174987767-c3cd1e48-f861-470e-a53c-37bc9d92deb5.png)
