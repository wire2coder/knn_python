""" 
    Importatnt Requirement
    Pythong 2.7
    PySpark 2
    Java 8
 """

from pyspark import SparkContext
from math import sqrt
import timeit # for timing the program execution time


""" step 1, calculate the Euclidean distance between '2 vectors' """
def euclidean_distance(row1, row2):
    distance = 0.0
    
    for i in range( len(row1)-1 ): # >> 3-1 = 2
        distance = distance + ( row1[i] - row2[i] )**2
    return sqrt(distance)


# Test distance function
dataset = [
    [2.7810836,2.550537003,0],          # row 0           
	[1.465489372,2.362125076,0],        # row 1
	[3.396561688,4.400293529,0],        # row 2
	[1.38807019,1.850220317,0],         # row 3
	[3.06407232,3.005305973,0],         # row 4
	[7.627531214,2.759262235,1],        # row 5
	[5.332441248,2.088626775,1],        # row 6
	[6.922596716,1.77106367,1],         # row 7
	[8.675418651,-0.242068655,1],       # row 8
	[7.673756466,3.508563011,1]         # row 9
    ]

row0 = dataset[0] # row 0
# print(row0)

for row_asdf in dataset: # for each 'ROW --'
    distance = euclidean_distance(row0, row_asdf)   # calculating the "straight line distance"
    print(distance) # printing the "stright line distance" of row0 to ALL other rows, including row0 to row0
