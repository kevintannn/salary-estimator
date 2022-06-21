from nltk.tokenize import word_tokenize

sentence = "Data Analyst\n\nDo you love data? Do you thrive on digging for info to answer complex questions and solve head-scratching problems? If you say yes, you might be part of the next generation of data scientists we’re looking for! This entry-level position will assist in prepping raw data for analysis, running and monitoring statistical models, and preparing findings for internal and external use.\n\nThe role\nNo two days at Suds Creative are the same, but in general you can expect to:\n•Use statistical methods to analyze data and generate useful business reports\n•Work with our management team to create a prioritized list of needs for each business segment\n•Identify and recommend new ways to gain revenue by streamlining analytic processes\n•Use data to create models that depict trends in the customer base and the consumer population as a whole\n•Work with departmental managers to outline the specific data needs for each business method analysis project\nYou’re most likely to succeed in this role if you:\n•Have 1-3 year of experience in data management\n•Are a self-motivated, autonomous problem solver\n•Understand data work is 80% prep–the successful candidate must know that when developing new tools, brute force may be required to shape the data\n•Have a high degree of comfortability in Excel\n•Have functional knowledge of various statistical tools (Regression, ANOVA, ARIMA, Clustering, and PCA)\n•Bring to the table natural curiosity and the ability to adapt models to the available data\n\nNice to haves:\n• Background in mathematics, finance, statistics or business\n• Proven track record of communicating complex findings in a digestible format\n• SQL database management expertise\n• Experience with R-Studio, Rattle, Alteryx, Tableau, SPSS, or Python\n• ODBC and API management experience\n\nBenefits& pay\n\nWe will invest in your professional development and create an environment where you will be given an opportunity to grow and develop your career. We offer a competitive compensation and a wide range of benefits, including paid time off, health insurance with company HSA contribution, dental, vision, 401(k) with company match, life insurance, and disability insurance. Plus, your favorite beverage will be stocked in our refrigerator!\n\nWork environment\nAt Suds Creative, we strive to foster a relaxed, friendly work environment that encourages creativity and collaboration. We are a quickly expanding company seeking someone who wants to grow alongside us as we take on new and exciting projects."

words = word_tokenize(sentence)
index = 0
for word in words:
    # print(word)
    if "r-studio" in word.lower() or "r studio" in word.lower():
        print(word)
        print(index)
    index += 1

for i in range(290, 300):
    print(words[i], end=" ")
print()

title = "Jr.Programmer"
print(title if "jr" in title.lower() else "na")