""" 
    Importatnt Requirement
    Pythong 2.7
    PySpark 2
    Java 8
 """

from pyspark import SparkContext
from math import sqrt
import timeit # for timing the program execution time


""" Step 1, calculate the Euclidean distance between '2 vectors' """
def euclidean_distance(row1, row2):
    distance = 0.0
    
    for i in range( len(row1)-1 ): # >> 3-1 = 2
        distance = distance + ( row1[i] - row2[i] )**2
    return sqrt(distance)


""" Step 2: Get the Nearest Neighbor """

def get_neighbors(train, test_row, num_neighbors):
    distances = list()    

    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append( (train_row, dist) )
    
    # debugging
    print("_____________________")
    print("distances LIST")
    for asdf in distances:
        print(asdf)
    print("_____________________")

    ### check point
    distances.sort( key=lambda tup: tup[1])
    print("_____________________")
    print("distances LIST SORT by Euclidean_distance")
    for asdf in distances:
        print(asdf)
    print("_____________________")


    # here 2/24/2020
    neighbors = list()

    for i in range( num_neighbors ):
        neighbors.append( distances[i][0] )
    
    return neighbors


# Test distance function
dataset = [
    [2.7810836,2.550537003,0],          # row 0, with 3 colums           
	[1.465489372,2.362125076,0],        # row 1, with 3 colums
	[3.396561688,4.400293529,0],        # row 2, with 3 colums
	[1.38807019,1.850220317,0],         # row 3, with 3 colums
	[3.06407232,3.005305973,0],         # row 4, with 3 colums
	[7.627531214,2.759262235,1],        # row 5, with 3 colums
	[5.332441248,2.088626775,1],        # row 6, with 3 colums
	[6.922596716,1.77106367,1],         # row 7, with 3 colums
	[8.675418651,-0.242068655,1],       # row 8, with 3 colums
	[7.673756466,3.508563011,1]         # row 9, with 3 colums
    ]


print("_____________________")
print("Original Dataset")
for asdf in dataset:
    print(asdf)
print("_____________________")


row0 = dataset[0] # row 0
print("_____________________")
print("Row 0", row0)
print("_____________________")


# for row_asdf in dataset: # for each 'ROW --'
#     distance = euclidean_distance(row0, row_asdf)   # calculating the "straight line distance"
#     print(distance) # printing the "stright line distance" of row0 to ALL other rows, including row0 to row0

# for asdf in dataset:
#     print(asdf)


neighbors = get_neighbors(dataset, dataset[0], 3)
# print(neighbors)


# for asdf in neighbors:
#     print(asdf)

