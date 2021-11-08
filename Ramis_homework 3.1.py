import datetime
current_year = int(datetime.datetime.now().strftime("%Y"))


class Cinema:
    def __init__(self, film_id, title, ticket_price, date_of_release, list_of_actors):
            self.film_id = film_id
            self.title = title
            self.ticket_price = ticket_price
            self.date_of_release = date_of_release
            self.list_of_actors = list_of_actors

    def __str__(self):
        return f"Film id: {self.film_id}\n" \
               f"Film: {self.title}\n" \
               f"Date of release: {self.date_of_release}\n" \
               f"Actors: {self.list_of_actors}"

    def __sub__(self, other):
        age = other - self.date_of_release
        return f"The movie already {age} years"

    def __len__(self):
        return f"Participates in the film {len(self.list_of_actors)} actors"


film_1 = Cinema(film_id=1, title="1 + 1",  ticket_price=220,  date_of_release=2021, list_of_actors=["Esen", "Nurgazy", "Ramis", "Aidana", "Mirhad"]
                )

film_2 = Cinema(film_id=2, title="Eternal", ticket_price=370, date_of_release=2001, list_of_actors=["Gemma Chan, Richard Madden, Angelina Jolie, Salma Hayek, Kit Harington"]
                )

print("**" * 20)
print(film_1)
print(film_1.__sub__(current_year))
print(film_1.__len__())
print("**" * 20)
print(film_2)
print(film_2.__sub__(current_year))
print(film_2.__len__())
print("**" * 20)


def choice_film():
    choice = input("Select a movie by title or id: ").lower()
    if choice in film_1.title.lower() or choice == str(film_1.film_id):
        print(f"The ticket for this movie is worth - {film_1.ticket_price} som")
    if choice in film_2.title.lower() or choice == str(film_2.film_id):
        print(f"The ticket for this movie is worth - {film_2.ticket_price} som")




class Starbucks:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        if len(self.name) > 5:
            return self.name[:5]
        return self.name


customer1 = Starbucks("Ramis")
customer2 = Starbucks("Aza")

print(customer1.__len__())
print(customer2.__len__())