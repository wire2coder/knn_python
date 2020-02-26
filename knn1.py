""" 
    Importatnt Requirement
    Pythong 2.7, Pythong 3
    PySpark 2
    Java 8

    'k-nearest neigbors' on the Iris Flowers Dataset
 """

import matplotlib
import matplotlib.pyplot as plt
import numpy as np  # 'library' for dealing with BIG 'data set'

from sklearn.ensemble import RandomForestClassifier

import timeit               
from pyspark import SparkContext
from math import sqrt
from random import seed
from random import randrange
from csv import reader

### Section, extra code
def simpleGraph():
    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)


    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
        title='About as simple as it gets, folks')
    ax.grid()

    fig.savefig("test.png")
    plt.show()


### Section, main program

# Load a  CSV file
def load_csv(filename):

    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)   # >> 'file reader' object
        
        for row in csv_reader:
            if not row:
                continue    # >> exit the 'for loop'

            dataset.append(row)
        
    return dataset    
    

# Convert 'string colum' to float numbers
def str_column_to_float(dataset, column):

    for row in dataset:
        # print(row[column])                  # print the value of colum 1, colum 2 of each row
        row[column] = float( row[column] )  # strip() take out all empty spaces
        # print( "after", type(row[column]))


# Convert 'string colum' to integer numbers        
def str_column_to_int(dataset, column):    
    class_values = [ row[column] for row in dataset ]
    unique = set(class_values) # converting values to 'SET'

    # print("class_values", class_values)
    # print("unique", unique)

    lookup = dict() # make a new 'dictionary'
    # print( list(enumerate(  unique)) )  # >> [(0,0)(1,1)] >> (counter, data)

    for i, value in enumerate(unique):   
        lookup[value] = i
    
    for row in dataset:        
        row[column] = lookup[ row[column] ]  # adding values to 'dictionary'
        
    # print("lookup", lookup)
    return lookup
    
# Convert string column to integer
def dataset_minmax(dataset):
    minmax = list() # make a new 'list'
    for i in range( len(dataset[0]) ):  # the length of the first row of dataset is 3, from 0 - 2
        col_values = [ row[i] for row in dataset ]
        value_min = min(col_values)
        value_max = max(col_values)

        minmax.append( [value_min, value_max] ) # adding data to the 'list'
    
    return minmax


# Rescale dataset column to the range 0-1
def normalize_dataset(dataset, minmax):
    for row in dataset:
        for i in range( len(row) ):
            row[i] = ( row[i] - minmax[i][0] / minmax[i][1] - minmax[i][0] )


# Split a dataset into k folds
# here


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
    

    neighbors = list()
    for i in range( num_neighbors ):
        neighbors.append( distances[i][0] )
    
    return neighbors


""" 
    Step 3: Make Predictions
        'Prediction' refers to the output of an algorithm 
"""
def predict_classification(train, test_row, num_neighbors):

    neighbors = get_neighbors(train, test_row, num_neighbors)

    # using "zip" to print 3 'nearest neighbor'
    print("____'nearest neighbor'_____")
    for asdf in zip(neighbors):
        print(asdf)
    print("_____________________")


    output_values = [row[-1] for row in neighbors]
    # print(output_values) # >> [0,0,0] print the last COLUM in each ROW

    # max() find the largest value in 'iterable'
    ## key=output_values.count
    ## COUNT the number is data that OCCUR the most

    # set() convert 'iterable' to SET theory
    ## The list before conversion is : [3, 4, 1, 4, 5]
    ## The list after conversion is : {1, 3, 4, 5}

    prediction = max( set(output_values), key=output_values.count )
    here, try to understand the 'max( set(output_values), key=output_values.count )'
    print("___'prediction'_____")
    print(prediction)
    print("_____________________")


    return prediction



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


## Section, stuff to show Dr.Shi
def showDrshi():
    prediction = predict_classification(dataset, dataset[0], 3)
    print('Expected %d, Got (prediction) %d.' % (dataset[0][-1], prediction) )
    
showDrshi()


# Make a 'prediction' with KNN on Iris Dataset    
filename = 'iris.csv'    
load_csv(filename)

for i in range( len(dataset[0])-1 ):    # >> length of dataset[0] - 1 is 2 | range(2) >> value 0,1
    # print(i)
    # convert class colum to floats
    str_column_to_float(dataset, i)


# convert class colum to integers
str_column_to_int(dataset, len(dataset[0])-1 )

# define model parameter

# define a new record

# predict the label


