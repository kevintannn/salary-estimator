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
![image](https://user-images.githubusercontent.com/48116781/174987997-e1d77ee7-13d8-4ab7-bd9b-5dc48644dcac.png)
![image](https://user-images.githubusercontent.com/48116781/174987630-2a244070-65db-4186-bb6d-b92357ed67dd.png)
![image](https://user-images.githubusercontent.com/48116781/174987767-c3cd1e48-f861-470e-a53c-37bc9d92deb5.png)

## Model Building
Before building the model, I first transformed categorical datas into dummy variables.  
After that, I split the data into train set and test set, with a test size of 20%.

I decided to try three different regression model and evaluated them using Mean Absolute Error.  
Using Mean Absolute Error is relatively easy to interpret and pressing down the influence of outliers.

The three different models:
* **Linear Regression** - Baseline for the model
* **Lasso Regression** - Due to the dataset has a large amount of categorical variable, I think it will be good to use a normalized regression
* **Random Forest** - With the same reason as Lasso, I think it will be a good fit.

## Model Performance
Random Forest model performs way better than the other two models.
* **Random Forest**: MAE = 11.65
* **Linear Regression**: MAE = 20.02
* **Lasso**: MAE = 21.29

## Productionize Model
