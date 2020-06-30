# Hypothesis-Testing
## Hypothesis Testing
Hypothesis: University towns have their mean housing prices less effected by recession.

Null hypotheses: The housing prices of the university towns and non-university towns have similar tendency affected by 2008 – 2009 recession

How to test: Run a t-test to compare the ratio of mean prices of houses in university towns the quarter before the recession starts compared to the recession bottom. 


## Overview:
This project is to test a Hypothesis whether University towns have their mean housing prices less effected by recession. The algorism used in this hypothesis is t-test. It is required to run a t-test to compare the ratio of mean prices of houses in university towns the quarter before the recession starts compared to the recession bottom. There are three datasets needed for this analysis. Python, Jupyter Notebook provide the support for the explorations.  Libraries needed are pandas, Numpy and scipy.stats. 

## Note:
This is project is based on assignments from the introduction to Data Science in Python by University of Michigan on Coursera. All the data have been downloaded from the Coursera website.

## Data description:

Datasets:

•	Housing data for United States, which has median home sale prices at a fine grained level from the  Zillow research data site 

•	University towns in the United States from Wikipedia page

•	From Bureau of Economic Analysis, US Department of Commerce, the GDP over time of the United States in current dollars (use the chained value in 2009 dollars), in quarterly intervals. For this project, only look at GDP data from the first quarter of 2000 onward.

## Results
The resulting tuple is (True, 0.0043252148535112009, 'university town') with p-value of 0.0043252148535112009, which is smaller than 0.01 (threshold). It means the null hypotheses (the two groups have similar tendency affected by 2008 – 2009 recession) is rejected. The result implies that university towns’ mean house prices have less affected by 2008-2009 recession.


