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

from pandas import read_csv
from numpy import mean, median, std, min, max
import matplotlib.pyplot

# get the file and column
csvFileinput = read_csv("crime1.csv")
columnOfViolentCrimesInPop = csvFileinput["ViolentCrimesPerPop"]


# calculate the values needed
meanOfViolentCrimesPerPop = mean(columnOfViolentCrimesInPop)
medianOfViolentCrimesPerPop = median(columnOfViolentCrimesInPop)
stdvOfViolentCrimesPerPop = std(columnOfViolentCrimesInPop)
minOfViolentCrimesPerPop = min(columnOfViolentCrimesInPop)
maxOfViolentCrimesPerPop = max(columnOfViolentCrimesInPop)


# show output
print("Mean: " + str(meanOfViolentCrimesPerPop))
print("Median: " + str(medianOfViolentCrimesPerPop))
print("Standard deviation : " + str(stdvOfViolentCrimesPerPop))
print("Minimum Value: " + str(minOfViolentCrimesPerPop))
print("Maximum Value: " + str(maxOfViolentCrimesPerPop))






# comparing the mean and median, it can be observed that the mean is larger then the median
# along side with the histogram showing the distribution shows a slightly apparent right skew shape,
# this is concluded by the "tail" shape thats going right and a "hill" found on the left

showPlot = False # show/hide plot
if showPlot:
    matplotlib.pyplot.hist(columnOfViolentCrimesInPop, bins = 25) # to see plot
    matplotlib.pyplot.show()



# an unusually large portion of the values of 1 were found although not exactly an outlier it is still unusual
# this causes the mean to deviate quite a bit
# as seen from comparing it with the median, the mean is larger
# this is explained by the way they are calculated, 
# average/mean is calculated by the sum of all values and dividing it by the number of elements
# while the median is the middle value of all the values