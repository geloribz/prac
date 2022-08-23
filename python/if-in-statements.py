movies_watched = {"The Kingsmen", "The Ring", "Jurassic Park"}
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print(f"Nope, I have not watched {user_movie}")
    