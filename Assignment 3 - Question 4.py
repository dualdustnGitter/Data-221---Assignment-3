### Question 4
# using train/test data from Q3
# 
#   train KNN classifier, using training data
#       set k = 5
#   use train data to predict labels of test data
# 
#   compute and print:
#       confusion matrix
#       accuracy
#       precision
#       recall
#       f1-score
# 
# Answer:
#   what TP, TN, FP, FNB mean in context of kidney disease prediction
#   why accuracy alone isnt enough to evaluyate classfication model
#   which metric is most important if missing kidney disease is serious and why
# 
###
from pandas import read_csv, get_dummies
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# from question 3
# turn csv into variable then create "X" and "Y" matrix/vectors 
csvFileInput = read_csv("kidney_disease.csv")
labelVectorY = csvFileInput["classification"]
featureMatrixX = csvFileInput.drop(columns=["classification"])  # turn csv data into feature matrix
                                                                # But get rid of "classification" column
                                                                # using panda's drop function

# cleaning up the feature Matrix so its usable

featureMatrixX = get_dummies(featureMatrixX,drop_first=True)    # changes the categorical variables into binary so the sklearn.metric methods can actually work with the function
featureMatrixX = SimpleImputer(strategy="mean").fit_transform(featureMatrixX)  # to replace missing values with mean (of full column)

# create training and testing data for "X" and "Y"
featuresTrain, featuresTest, classificationTrain, classificationTest = train_test_split(featureMatrixX,labelVectorY, test_size=0.3, train_size=0.7, random_state=50)


# getting the trained model
numberOfNeighbors = 5
knnModelForKidneyDiseaseCSV = KNeighborsClassifier(n_neighbors=numberOfNeighbors)
knnModelForKidneyDiseaseCSV.fit(featuresTrain,classificationTrain)

# use the model to predict the test  features
predictedClassification = knnModelForKidneyDiseaseCSV.predict(featuresTest)
# calculate the, accuracy, precision, recall score, and f1 score
accuracy = accuracy_score(classificationTest,predictedClassification)
precision = precision_score(classificationTest,predictedClassification, average= "macro", zero_division=1.0)
recallScore = recall_score(classificationTest,predictedClassification, average = "macro")
f1Score = f1_score(classificationTest,predictedClassification, average = "macro")

# display the calculated values
print("Accuracy of model:\t\t" + str(accuracy))
print("Precision of model:\t\t" + str(precision))
print("Recall score of model:\t" + str(recallScore))
print("F1 score of model:\t\t" + str(f1Score))



# In the context of Kidney Disease..
# True positive means to have a test to output positive/present on a person that does have the disease
# True negative means to have a test to output negative/not present on a person that does not have the disease
# False positive means to have a test output positive/present on a person when they do not have the disease
# False negative means to have a test output negative/not present on a person when they do have the disease


# as stated in the lectures, accuracy alone is enough to represent a model's effectness (bad models can have high accuracy)
# this is due to the fact on how its calculated
# its numerator is the sum of true positive and negative
# and denominator being all 4 True P/N and False P/N
# which it turn treats all errors equally even though they should be weighted depending on the number of them
# espiecially if the data is heavily sided (imbalanced in data)


# the most important metric here would be the "classification" metric  
# what this entire model is predicting the classification depending on other variables such as age, blood pressure etc
# by just having these independent and no classification there isnt really a point to train the data off of
# just giving it "gibberish" values to conclude nothing
# so the most important metric here would be the "classification" metric