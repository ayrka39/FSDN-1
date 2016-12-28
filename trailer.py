import fresh_tomatoes
import movie

# detailed information about favorite moves
fiddler = movie.Movie("Fiddler on the roof",
    "the father of five daughters, and his attempts to maintain his Jewish religious and cultural traditions as outside influences encroach upon the family's lives.",
    "https://upload.wikimedia.org/wikipedia/en/5/5e/Fiddler_on_the_roof.jpg",
    "https://youtu.be/t32ttyvWToQ")

singing = movie.Movie("Singing in the rain",
    "It offers a lighthearted depiction of Hollywood in the late 1920s, with the three stars portraying performers caught up in the transition from silent films to 'talkies'",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/Singing_in_the_rain_poster.jpg",
    "https://youtu.be/B0asbGJbLKc")

fair = movie.Movie("My fair lady",
    "it  depicts a poor Cockney flower seller named Eliza Doolittle who overhears an arrogant phonetics professor, Henry Higgins, as he casually wagers that he could teach her to speak 'proper' English, thereby making her presentable in the high society of Edwardian London.",
    "https://upload.wikimedia.org/wikipedia/en/d/d5/My_fair_lady_poster.jpg",
    "https://youtu.be/C0xhzA78u4Q")

# set movies to open in a browser
movies = [fiddler, singing, fair]
fresh_tomatoes.open_movies_page(movies)
