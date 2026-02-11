### Question 1
# load crime.csv into pandas DataFrame, focus col of ViolentCrimesPerPop
# 
# Compute:
#   Mean
#   Median
#   Standard deviation
#   Minimum value
#   Maximum value
#   
# Answer using comments:
#   Compare mean and median, is dist symmetric or skewed, explain
# 
#   If there are outliers, which stat is affected mean or median
# 
### 

import pandas
import numpy


csvFileinput = pandas.read_csv("crime1.csv")
columnOfViolentCrimesInPop = csvFileinput["ViolentCrimesPerPop"]

meanOfViolentCrimesPerPop = numpy.mean(columnOfViolentCrimesInPop)
medianOfViolentCrimesPerPop = numpy.mean(columnOfViolentCrimesInPop)
stdvOfViolentCrimesPerPop = numpy.std(columnOfViolentCrimesInPop)
minOfViolentCrimesPerPop = numpy.min(columnOfViolentCrimesInPop)
maxOfViolentCrimesPerPop = numpy.max(columnOfViolentCrimesInPop)


print("Mean: " + str(meanOfViolentCrimesPerPop))
print("Median: " + str(medianOfViolentCrimesPerPop))
print("Standard deviation : " + str(stdvOfViolentCrimesPerPop))
print("Minimum Value: " + str(minOfViolentCrimesPerPop))
print("Maximum Value: " + str(maxOfViolentCrimesPerPop))


