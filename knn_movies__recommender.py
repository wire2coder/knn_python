""" 
    Importatnt Requirement
    Pythong 2.7, Pythong 3
    PySpark 2
    Java 8

    'k-nearest neigbors' 
    https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761
 """

from knn_from_scratch import knn, euclidean_distance

def recommend_movies(movie_query, k_recommendations):
    raw_movies_data = []

    # open file, read only
    with open('movies_recommendation_data.csv', 'r') as md:

        next(md) # skip the 'first line'

        # read data into memory
        for line in md:
            data_row = line.strip().split(',')

            # debug
            print("\n")
            print("data_row", data_row)

            raw_movies_data.append(data_row)

        # debug
        print("\n\n")
        print("raw_movies_data", raw_movies_data)    

    # prepare the data, so it can be use by the 'KNN'
    # need to convert data in 'each column' into numbers
    # because it was 'read in' as a string
    movies_recommendation_data = []

    for row in raw_movies_data:
        # row[2:], get data 'starting' from 'row 2'
        # probably don't need ' list() '
        data_row = list(map(float, row[2:])) 

        movies_recommendation_data.append(data_row)

    # debug
    print("\n\n")
    print("movies_recommendation_data", movies_recommendation_data)    
    print("\n")
    print("type movies_recommendation_data", type(movies_recommendation_data) )    

    # use KNN algorithm to get '5 similar movies' to 'query_movie'
    recommendation_indices, jim = knn(
        movies_recommendation_data, movie_query, k=k_recommendations,
        distance_fn=euclidean_distance, choice_fn=lambda x: None
    )
    
    # debug
    print("\n\n")
    print("recommendation_indices", recommendation_indices)

    movie_recommendations = []
    for _, index in recommendation_indices:

        # debug
        print("\n\n")
        print("_", _)
        print("index", index)
        
        movie_recommendations.append(raw_movies_data[index])
    
    
    # debug
    print("\n\n")
    print("movie_recommendations", movie_recommendations)

    return movie_recommendations


# program STARTs HERE
def main():
    
    # movie name is 'the_post'
    the_post = [7.2, 1, 1, 0, 0, 0, 0, 1, 0] # 'feature vector' for 'The Post'

    # use KNN to 'predicts' the 5 similar movies
    recommended_movies = recommend_movies(the_post, 5)

    # print the 5 'movie titles'
    for recommendation in recommended_movies:
        print("\n")
        print("recommendation", recommendation)
        # print("recommendation (2nd column)", recommendation[1])

# run the 'main' function
if __name__ == '__main__':
    main()