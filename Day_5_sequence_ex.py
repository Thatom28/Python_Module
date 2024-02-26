movies = [
    {
        "title": "Inception",
        "ratings": [5, 4, 5, 4, 5]
    },
    {
        "title": "Interstellar",
        "ratings": [5, 5, 4, 5, 4]
    },
    {
        "title": "Dunkirk",
        "ratings": [4, 4, 4, 3, 4]
    },
    {
        "title": "The Dark Knight",
        "ratings": [5, 5, 5, 5, 5]
    },
    {
        "title": "Memento",
        "ratings": [4, 5, 4, 5, 4]
    },
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
movies_average_ratings = list(
    map(lambda movie: {
        **movie, "average": find_avg(movie)
    }, movies))  # the list it uses
#-----Or write the calculation indide the map
# movies_average_ratings = list(map(lambda movie: {**movie, "average":  sum(movie['ratings']) / len(movie['ratings'])}, movies)
print(movies_average_ratings)

#task 2, to rated movie

top_rated_movie = max(movies_average_ratings,
                      key=lambda x: x["average"])  #used the existing function
print(top_rated_movie["title"])  #output = Dark knght

#----Task 3: movie with rating above 4.6
list_top_rated = list(
    filter(lambda x: x["average"] >= 4.6, movies_average_ratings))
title = list(map(lambda x: x["title"], list_top_rated))
print(title)

#-----------Adding language key to movies
# movie_lang = map(lambda x : {**x, "Language": "English"}, movies)
# print(list(movie_lang))
# #-------------------Task 4: order the rating(Home work)
movie_sort = sorted(movies_average_ratings,
                    key=lambda x: x["average"],
                    reverse=True)
sorted_movie_title = list(map(lambda x: x['title'], movie_sort))
print(sorted_movie_title)
