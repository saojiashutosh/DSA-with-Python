class movies:
    def __init__(self, title, actor, actress):
        self.title = title
        self.actor = actor
        self.actress = actress

    def info(self):
        print("Movie title :", self.title)
        print("Actor name :", self.actor)
        print("Actress name :", self.actress)


list_of_movies = []
while True:
    title = input("Enter movie title:")
    actor = input("Enter actor name:")
    actress = input("Enter actress name:")
    m = movies(title, actor, actress)
    list_of_movies.append(m)
    print("Movies added successfully to the list")
    choice = input("Do you want to add other movie(y/n):")
    if choice.strip().lower() == "n":
        break

for movie in list_of_movies:
    movie.info()
    print()
