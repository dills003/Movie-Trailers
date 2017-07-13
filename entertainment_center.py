import fresh_tomatoes
import media #contains my movie class

#Three movies using the 'Movie' class to feed fresh tomatoes
#Needs a name, poster link, and trailer link
GoneInSixty = media.Movie("Gone In 60 Seconds",
                  "https://upload.wikimedia.org/wikipedia/en/2/2a/Gone_in_sixty_seconds.jpg",
                 "https://www.youtube.com/watch?v=o6AyAM1buQ8")

Go = media.Movie("Go",
                  "https://upload.wikimedia.org/wikipedia/en/a/a8/Go_1999_film.jpg",
                 "https://www.youtube.com/watch?v=0KTWEFpDOis")

DaysOfThunder = media.Movie("Days of Thunder",
              "https://upload.wikimedia.org/wikipedia/en/d/d8/Days_of_thunder.jpg",
              "https://www.youtube.com/watch?v=AhUhuDW_jOw")

movies = [GoneInSixty, Go, DaysOfThunder] #list to give to fresh_tomatoes

fresh_tomatoes.open_movies_page(movies) #takes our list/info and converts it into a nice html that we can view in a web browser
