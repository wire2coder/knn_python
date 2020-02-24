## Important Requirement
## Python 2.7
## Pyspark
## Java 8


import timeit # for timing the program execution time
from pyspark import SparkContext


logFile = "43.txt" # 160KB
# logFile = "warPeaceBig.txt" # 1GB


# sc = SparkContext("local", "first app") << this line DOES NOT WORK
# sc = SparkContext.getOrCreate() # application_1568753002261_0322, this PARALELL
sc = SparkContext('local[*]') # local-1581541952245, this SERIAL
logData = sc.textFile(logFile).cache()

# starting timer
start = timeit.default_timer()


numAs = logData.filter(lambda s: 'a' in s).count() 
print "Lines with a: %i" % (numAs)


# stop timer
stop = timeit.default_timer()

# print out, execution time for the program
print "program run time: %f second(s)" % (stop - start) 