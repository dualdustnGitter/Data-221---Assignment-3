### Question 3
# load kidney_disease.csv as pandas DataFrame
# create feature matrix X containg all columns except CKD
# create label vector y using CKD col
# 
# split dataset into 
#   70% training data
#   30% testing data 330%
#       use train_test_split with fixed random_state
# 
# then explain
#   Why we should not train and test a model on same data
#   purpose of testing set
### 

from pandas import read_csv
from sklearn.model_selection import train_test_split


csvFileInput = read_csv("kidney_disease.csv")
featureMatrixX = csvFileInput.drop(columns=["classification"])  # turn csv data into feature matrix
                                                                # But get rid of "classification" column
                                                                # using panda's drop function

# print(featureMatrixX)