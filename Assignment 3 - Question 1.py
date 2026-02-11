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
import matplotlib.pyplot

# get the file and column
csvFileinput = pandas.read_csv("crime1.csv")
columnOfViolentCrimesInPop = csvFileinput["ViolentCrimesPerPop"]


# calculate the values needed
meanOfViolentCrimesPerPop = numpy.mean(columnOfViolentCrimesInPop)
medianOfViolentCrimesPerPop = numpy.median(columnOfViolentCrimesInPop)
stdvOfViolentCrimesPerPop = numpy.std(columnOfViolentCrimesInPop)
minOfViolentCrimesPerPop = numpy.min(columnOfViolentCrimesInPop)
maxOfViolentCrimesPerPop = numpy.max(columnOfViolentCrimesInPop)


# show output
print("Mean: " + str(meanOfViolentCrimesPerPop))
print("Median: " + str(medianOfViolentCrimesPerPop))
print("Standard deviation : " + str(stdvOfViolentCrimesPerPop))
print("Minimum Value: " + str(minOfViolentCrimesPerPop))
print("Maximum Value: " + str(maxOfViolentCrimesPerPop))





# comparing the mean and median, it can be observed that the mean is larger then the median
matplotlib.pyplot.hist(columnOfViolentCrimesInPop, bins = 25)
matplotlib.pyplot.show()
# along side with the histogram showing the distribution shows a slightly apparent right skew shape,
# this is concluded by the "tail" shape thats going right and a "hill" found on the left



# with outliers found at the value of 1.0, this causes the mean to deviate quite a bit
# as seen from comparing it with the median, the mean is larger
# this is explained by the way they are calculated, 
# average/mean is calculated by the sum of all values and dividing it by the number of elements
# while the median is the middle value of all the values