import fresh_tomatoes
import media

# entertainment_center.py is a simple Python script used to help me understand
# the basics of the Python language via the building of a simple web page that
# serves up information about several of my favorite movies.

# Toy Story
toy_story = media.Movie(
    "Toy Story",
    "A Story of a boy and his toys that come to life.",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4"
)

# Avatar
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8"
)

# School Of Rock
school_of_rock = media.Movie(
    "School of Rock",
    "Storyline",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74"
)

# Ratatouille
ratatouille = media.Movie(
    "Ratatouille",
    "Storyline",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk"
)

# Midnight In Paris
midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Storyline",
    "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
    "https://www.youtube.com/watch?v=U_3gIxrcWK8"
)

# Hunger Games
hunger_games = media.Movie(
    "Hunger Games",
    "Storyline",
    "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
    "https://www.youtube.com/watch?v=PbA63a7H0bo"
)

# Blade
blade = media.Movie(
    "Blade",
    "A badass with an attitude...",
    "http://upload.wikimedia.org/wikipedia/en/1/19/Blade_movie.jpg",
    "https://www.youtube.com/watch?v=kaU2A7KyOu4"
)

# Scary Movie 4
scarymovie4 = media.Movie(
    "Scary Movie 4",
    "A pretty funny movie...",
    "http://upload.wikimedia.org/wikipedia/commons/e/e4/Scary_Movie_4_logo.jpg",
    "https://www.youtube.com/watch?v=9PuhVxfxj8w"
)

# Sling Blade
slingblade = media.Movie(
    "Sling Blade",
    "A good movie...",
    "http://upload.wikimedia.org/wikipedia/en/4/44/Slingbladeposter.jpg",
    "https://www.youtube.com/watch?v=DfnPrMypS8U"
)

#print(media.Movie.VALID_RATINGS)
#print("Documentation is referenced via the __doc__ annotation")
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)


# Listing of my favorite movies...
movies = [
    toy_story, avatar, school_of_rock, ratatouille,
    midnight_in_paris, hunger_games,
    blade, scarymovie4, slingblade
]

# 
fresh_tomatoes.open_movies_page(movies)
