""" 
    Importatnt Requirement
    Pythong 2.7, Pythong 3
    PySpark 2
    Java 8

    'k-nearest neigbors' 
    https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761
 """

from collections import Counter
import math


def knn(data, query, k, distancce_fn, choice_fn):
    # making a new 'list'
    neighbor_distance_and_indices = []

    # 3. for each 'example' in the data
    for index, example in enumerate(data):
        # 3.1 calculate the distance between the '' and ''
        distance = distance_fn(example[:-1], query)

        # 3.2 and the distance to the 'list'
        neighbor_distance_and_indices.append( (distance, index) )

        # 4 /sort/ the 'list' from smallest to largest
        sorted_neighbor_distances_and_indices = sorted(neighbor_distance_and_indices)

        # 5 pick the first 'K'
        k_nearest_distances_and_indices = sorted_neighbor_distances_and_indices[:k]

        # 6 get the 'lable' of the 'K' << here, what is this line doing????
        k_nearest_lables = [ data[i][1] for distance, i in k_nearest_distances_and_indices ]

        # 7. If regression (choice_fn = mean), return the average of the K labels
        # 8. If classification (choice_fn = mode), return the mode of the K labels
        return k_nearest_distances_and_indices, choice_fn(k_nearest_lables)


def main():

    '''
    # Regression Data
    # 
    # Column 0: height (inches)
    # Column 1: weight (pounds)
    '''

    reg_data = [
       [65.75, 112.99],
       [71.52, 136.49],
       [69.40, 153.03],
       [68.22, 142.34],
       [67.79, 144.30],
       [68.70, 123.30],
       [69.80, 141.49],
       [70.01, 136.46],
       [67.90, 112.37],
       [66.49, 127.45],
    ]

    # Question:
    # Given the data we have, what's the best-guess at someone's weight if they are 60 inches tall?
    reg_query = [60]
    reg_k_neareset_neighbors, reg_prediction = knn( reg_data, reg_query, k=3, distancce_fn=euclidean_distance, choice_fn=mean )

    here


if __name__ == '__main__':
    main()