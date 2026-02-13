### Question 5
# use trained model from last question
#   train using k = [1,3,5,7,9]
#       for each k calc
#           test accuracy
#           make smal table showing k val and and corr accuracy
#           id which k has highest accuracy
#           
#           
# Answer:
#   how changing k changes accuracy
#   why small k cause overfitting
#   why large k cause underfitting
#   
###

# Question 4 stuff
from pandas import read_csv, get_dummies, DataFrame
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
# sources:
#   get_dummies - https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html
#   SimpleImputer - https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html 
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




# Actual question 5 stuff

# initialize lists
listOfNumberOfNeighbors = [1,3,5,7,9]
listOfAccuracyValuesOfKNNModel      = []
listOfPrecisionValuesOfKNNModel     = []
listOfRecallScoreValuesOfKNNModel   = []
listOfF1ScoreValuesOfKNNModel       = []

greatestTestAccuracyValueIndex = 0

# go through values of k value list to create their corr Accuracy, Precision, Recall Score, and F1 Score values
for numberOfNeighbors in listOfNumberOfNeighbors:
    knnModelForKidneyDiseaseCSV = KNeighborsClassifier(n_neighbors=numberOfNeighbors)
    knnModelForKidneyDiseaseCSV.fit(featuresTrain,classificationTrain)

    # use the model to predict the test  features
    predictedClassification = knnModelForKidneyDiseaseCSV.predict(featuresTest)
    # calculate the, accuracy, precision, recall score, and f1 score
    accuracyOfKNNModel = accuracy_score(classificationTest,predictedClassification)
    precisionOfKNNModel = precision_score(classificationTest,predictedClassification, average= "macro", zero_division=1.0)
    recallScoreOfKNNModel = recall_score(classificationTest,predictedClassification, average = "macro")
    f1ScoreOfKNNModel = f1_score(classificationTest,predictedClassification, average = "macro")

    # add values to respective list
    listOfAccuracyValuesOfKNNModel.append(accuracyOfKNNModel)
    listOfPrecisionValuesOfKNNModel.append(precisionOfKNNModel)
    listOfRecallScoreValuesOfKNNModel.append(recallScoreOfKNNModel)
    listOfF1ScoreValuesOfKNNModel.append(f1ScoreOfKNNModel)

    if listOfAccuracyValuesOfKNNModel[greatestTestAccuracyValueIndex] < accuracyOfKNNModel:
        greatestTestAccuracyValueIndex = len(listOfAccuracyValuesOfKNNModel) - 1


# print to check if it works
# for indexOfCurrentListElement in range(len(listOfNumberOfNeighbors)):
#     print("[K value: " + str(listOfNumberOfNeighbors[indexOfCurrentListElement]) +"]\n"
#     "\t\t\tAccuracy: " + str(listOfAccuracyValuesOfKNNModel[indexOfCurrentListElement]) + "\n"
#     "\t\t\tPrecision: " + str(listOfPrecisionValuesOfKNNModel[indexOfCurrentListElement]) + "\n"
#     "\t\t\tRecall Score: " + str(listOfRecallScoreValuesOfKNNModel[indexOfCurrentListElement]) + "\n"
#     "\t\t\tF1 Score: " + str(listOfF1ScoreValuesOfKNNModel[indexOfCurrentListElement]))


# make it into a dataframe/table
coolNewDataFrame = DataFrame()
for indexOfCurrentListElement in range(len(listOfNumberOfNeighbors)):
    coolNewDataFrame["K value " + str(listOfNumberOfNeighbors[indexOfCurrentListElement])] = [listOfAccuracyValuesOfKNNModel[indexOfCurrentListElement], 
                                                                                 listOfPrecisionValuesOfKNNModel[indexOfCurrentListElement], 
                                                                                    listOfRecallScoreValuesOfKNNModel[indexOfCurrentListElement], 
                                                                                    listOfF1ScoreValuesOfKNNModel[indexOfCurrentListElement]]
    coolNewDataFrame.index=["Accuracy", "Precision", "Recall Score", "F1 Score"]
    
print(coolNewDataFrame)


# show k value with highest test accuracy
print("\nK value: [" + str(listOfNumberOfNeighbors[greatestTestAccuracyValueIndex]) + "] with highest accuracy: " + str(listOfAccuracyValuesOfKNNModel[greatestTestAccuracyValueIndex]))


