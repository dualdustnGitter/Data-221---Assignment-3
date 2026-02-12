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