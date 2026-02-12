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
featureMatrixX = get_dummies(featureMatrixX,drop_first=True)
featureMatrixX = SimpleImputer(strategy="most_frequent").fit_transform(featureMatrixX)

# create training and testing data for "X" and "Y"
featuresTrain, featuresTest, classificationTrain, classificationTest = train_test_split(featureMatrixX,labelVectorY, test_size=0.3, train_size=0.7, random_state=50)


# getting the trained model
numberOfNeighbors = 5
knnModelForKidneyDiseaseCSV = KNeighborsClassifier(n_neighbors=numberOfNeighbors)
knnModelForKidneyDiseaseCSV.fit(featuresTrain,classificationTrain)

predictedClassification = knnModelForKidneyDiseaseCSV.predict(featuresTest)
accuracy = accuracy_score(classificationTest,predictedClassification)
# precision = precision_score(classificationTest,predictedClassification)
# recallScore = recall_score(classificationTest,predictedClassification)
# f1Score = f1_score(classificationTest,predictedClassification)

print(accuracy)
# print(precision)
# print(recallScore)
# print(f1Score)