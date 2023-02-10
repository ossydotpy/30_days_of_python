#TUPLES
    #QUESTION

# Create a movies list containing a single tuple.
# The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.
# Use the input function to gather information about another movie.
# You need a title, director’s name, release year, and budget.
# Create a new tuple from the values you gathered using input.
# Make sure they’re in the same order as the tuple you wrote in the movies list.
# Use an f-string to print the movie name and release year by accessing your new movie tuple.
# Add the new movie tuple to the movies collection using append.
# Print both movies in the movies collection.
# Remove the first movie from movies. Use any method you like.

#SOLUTION
#declaring the movies list
movies =  [("Suicide Squad","James Gunn", 2022, "$20M")]

#accepting user input
movie_name = input("Please Enter a movie name:\n")
movie_director = input("Whoo directed this movie?:\n")
movie_release_date = input("When was this movie released?:\n")
movie_budget = input("What was the budget of this movie?:\n")

movie_info = (movie_name,movie_director,movie_release_date,movie_budget)

#adding the user input into the movies list
movies.append(movie_info)

#printing the content of the movie list
for i in movies:
    print(i)


# removing the first entry
del movies[0]

print(f"\nmovies:\n{movies}")