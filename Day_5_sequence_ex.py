movies = [
  {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},
  {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},
  {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},
  {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},
  {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},
]
#Task 1 print the titles
# Title = map(lambda x: x["title"], movies)
# print(list(Title))
# #task 1,1 the average as average
# average = list(map(lambda rating: sum(rating["ratings"])/len(rating["ratings"]), movies))
# print(average)


# Task 1.2 - Find average for all - map, filter, all, ...


def find_avg(movie):
  return sum(movie['ratings']) / len(movie['ratings'])
# print(movies)

# for movie in movies:
#   for ave in average:
#     movie["average"] = ave
# print(movies)
 #map(func, list)
movies_average_ratings = list(map(
lambda movie: {
    **movie, "average_rating": find_avg(movie)
}, movies)) # the list it uses



#task 2, to rated movie
#max_score_name = max(scores, key=lambda x: x[1])
top_rated_movie = max(movies_average_ratings, key = lambda x: x["average_rating"])  #used the existing function
print(top_rated_movie["title"])


#----Task 3: movie with rating above 4.6
list_to_rated_movies = list(filter(lambda movie: movie["average_rating"] >= 4.6, movies_average_ratings))
maped_list = list(map(lambda x: x["title"], list_to_rated_movies))
print(maped_list)


#-------------------Task 4: order the rating(Home work)
