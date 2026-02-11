### Question 2
# use same dataset and col, create 2 plots
# 
#   histogram
#   boxplot
#   
# both plots must include
#   title
#   X axis label
#   Y axis label
# 
# Answer questions:
#   what the hist shows about data values are spread
#   box plot on the median
#   does box plot present presence of outliers?
#   
### 


import pandas
import numpy
import matplotlib.pyplot

# make plot labels
titleOfPlotLabel = "Histogram of Violent Crimes per Population"
xAxisLabelName = "Violent Crimes per Population"
yAxisLabelName = "Occurences of violent crimes"

matplotlib.pyplot.title(titleOfPlotLabel)
matplotlib.pyplot.xlabel(xAxisLabelName)
matplotlib.pyplot.ylabel(yAxisLabelName)






# get the file and column
csvFileinput = pandas.read_csv("crime1.csv")
columnOfViolentCrimesInPop = csvFileinput["ViolentCrimesPerPop"]




# displaying plot
displayHistogram = True # switching boolea value to see histogram/boxplot -> True/False respectively

# choosing between histogram or boxplot
if displayHistogram:
    matplotlib.pyplot.hist(columnOfViolentCrimesInPop,bins=25)
else:
    matplotlib.pyplot.boxplot(columnOfViolentCrimesInPop)


matplotlib.pyplot.show()



# The histogram shows a distribution of the number of values that were found
# for example of 2 values of 0.4 were found 
# then the y axis would be the frequency(amount) and x axis would be the value
# most of the values are found at the lower end (left) and lesser on the higher values (right)
# thus with this it can be said that it is right skewed



# the box plot shows the median as the the orange line in the actual box
# the median again, represents the middle value according to all the values given
# and it shows how the median is "found" in the data, to make it easier flip the boxplot by rotating it 90 degrees
# now you'd see that the median line is found more on the left side of the box 
# showing that the median is the lower end of values and showing that its a right skew



# the box plot usually does show outliers but here since theyre are in the range of values
# in a normal box plot if outliers were detected then that'd be presented as hollow circles
# and found above or udner the "handles" the furthiest horizontal lines which represent the min/max
# in this case no outleirs were found so they werent added here