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

# turn csv into variable then create "X" and "Y" matrix/vectors 
csvFileInput = read_csv("kidney_disease.csv")
labelVectorY = csvFileInput["classification"]
featureMatrixX = csvFileInput.drop(columns=["classification"])  # turn csv data into feature matrix
                                                                # But get rid of "classification" column
                                                                # using panda's drop function
# otherWayFeatureMatrixX= csvFileInput.loc[:,["id", "age", "bp", 
#                                             "sg", "al","su", 
#                                             "rbc", "pc", "pcc"
#                                             , "ba", "bgr", "bu"
#                                             , "sc", "sod", "pot"
#                                             , "hemo", "pcv", "wc"
#                                             , "rc", "htn", "dm"
#                                             , "cad", "appet", "pe"
#                                             , "ane"]]     # way shown in lecture

# create training and testing data for "X" and "Y"
featuresTrain, featuresTest, classificationTrain, classificationTest = train_test_split(featureMatrixX,labelVectorY, test_size=0.3, train_size=0.7, random_state=50)


# check if test data size is 30% and train data size is 70%
# print(len(featuresTrain))
# print(len(featuresTest))


# we shouldnt use the train and test data on the same model since 
# the train data is used to be the main initial way to develop the model
# to better predict later wanted data
# and the test data is used to calculate the precision of this model
# by using the dependent variable from the test data then getting the output of from the model
# we could compare the model's predicted values and the actual values
# by using the train and test data it causes the model to "overfit"
# where trying to predict "newer" data is not possible since it sticks to the original too much



# the purpose of the testing set is to get the precision of the model
# allows us to check if the model is accurate or not giving us a "grading"
# of the model much like how teaching a concept in class with an example
# and using a "different" example in an exam to test a student's understanding of the concepts