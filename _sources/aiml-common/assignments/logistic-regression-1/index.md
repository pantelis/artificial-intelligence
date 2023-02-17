# Logistic Regression 

You are interviewing with Google's data science team having the responsibility of predicting the Click Through Rate (CTR) of ads they place on multiple web properties. Your hiring manager keen on testing you out, suggests to download [this dataset](https://www.kaggle.com/competitions/avazu-ctr-prediction/data) and asks you to code up a model that predicts the CTR based on Logistic Regression. 

## Environment Setup (10 points)

You will deliver this assignment in the form of a Colab notebook (or a Github repo if you like). Both must be configured to allow anyone to run the code (in Colab this is `Run All`) and get the results. Setup your environment that can automatically download the data from Kaggle and store them in a location. You may [want to read for this task](https://www.kaggle.com/docs/api#interacting-with-datasets) and ensure that this task is implemented with Python. 

## Data Preprocessing (30 points)

Preprocess the data you are given to your liking. This may include dropping some columns you wont use, addressing noisy or missing data etc. 

Use Pandas as a  dataframe abstraction for this task. You can learn about Pandas here:

```{eval-rst}
.. youtube:: PcvsOaixUh8
```

Ultimately this task has to result to a dataframe that you will use for the training and testing the classifier. 

## Logistic Regression (40 points)

Implement the logistic regression solution to the prediction problem that can work with Stochastic Gradient Descent (SGD). 

Show clearly all equations of the gradient and include comments in either markdown or Python (inline to code) explaining every stage of processing. Also, highlight any enhancements you may have done to improve performance. 

## Performance Results (20 points)

Plot the precision vs recall curve of your classifier. Clearly explain the tradeoff between the two quantities and the shape of the curve. 












