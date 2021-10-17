import imdb
a=imdb.IMDb()
movie_name=input("Enter the movie name : ")
movies=a.search_movie(movie_name)
index=movies[0].getID()
movie=a.get_movie(index)
movie_title=movie['title']
movie_year=movie['year']
movie_cast=movie['cast']
b=len(movie_cast)

print(" The title of the movie is : ",movie_title)
print(" The release year of the movie is : ",movie_year)
print(" The cast of the movie is : ")
for i in range(0,b):
    movie_cast_name=movie_cast[i]['name']
    print(" "+movie_cast_name)

