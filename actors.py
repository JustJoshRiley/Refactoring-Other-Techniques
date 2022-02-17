# by Kami Bigdely
# Extract class


class Actor:
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email

    def print_rap_sheet(self):
        print(self.first_name, self.last_name)
        print('Movies Played In: ', self.print_movies())
        print

    def print_movies(self):
        for movie in self.movies:
            print(movie, end=" ")

    def send_hiring_email(self):
        print("email sent to: ", self.email)
    


first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
        ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']


actors = []

for index in range(len(first_names)):
    actors = Actor(first_names[index], last_names[index], birth_year[index], movies[index], emails[index])
    actors.append(actors)

for actor in actors:
    if actor.birth_year > 1985:
        actor.print_rap_sheet()
        actor.send_hiring_email()

# for i, value in enumerate(emails):
#     if birth_year[i] > 1985:
#         print(first_names[i], last_names[i])
#         print('Movies Played: ', end='')
#         for m in movies[i]:
#             print(m, end=', ')
#         print()
#         send_hiring_email(value)