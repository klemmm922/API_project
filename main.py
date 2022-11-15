from package import boxOffAllTime
from package import movie

# we want the rating of the boxOffice of all time movies

boxOffAllTime_list = boxOffAllTime.boxOfficeAllTimeRequest.get_box_office()

rating_list = []

for i in boxOffAllTime_list:
    rating_list.append((movie.movie(i).rating,i))

# sort the  list by rating

rating_list.sort(reverse=True)

print ("The top 10 movies of box office of all time based on rating are:")
for i in range(10):
    print (rating_list[i][1]+" with a rating of "+str(rating_list[i][0]))


