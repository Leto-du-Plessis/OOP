# To be formatted later *** 

class User:

    def __init__(self, username: str, password: str, favourite_movie: str):
        self.username = username
        self.password = password
        self.favourite_movie = favourite_movie

    def compare_movie(self, other) -> bool:
        return self.favourite_movie == other.favourite_movie
    
    def compare_movie_from_string(self, movie: str) -> bool:
        return self.favourite_movie == movie
    
    def compare_movie_from_strings(self, movie: str, other_movie: str) -> bool:
        return movie == other_movie
    
    def compare_movie_from_user(self, other_user):
        return self.compare_movie_from_string(other_user.favourite_movie)
    
    def compare_username(self, other) -> bool:
        return self.username == other.username
    
    def __eq__(self, other) -> bool:
        return self.username == other.username and self.favourite_movie == other.favourite_movie

user = User("Leto", "ThisPasswordIsTotallySecure", "Across the Spiderverse")
# print(f"{user.username} likes {user.favourite_movie}.")

users = [user, User("Joe", "ThisPasswordIsNotSecure", "Saving Private Ryan"), User("Maria", "ThisPasswordIsExtremelySecure", "The Incredibles")]
users.append(User("Leto", "ThisPasswordIsTotallySecure", "Across the Spiderverse"))

# print(" and ".join(f"{user.username} likes {user.favourite_movie}" for user in users) + ".")
# print(users[0].compare_movie(users[1]))
# print(users[0].compare_movie_from_string(users[2].favourite_movie)) #???
# print(users[0].compare_movie_from_user(users[1]))
# print(users[0].compare_username(users[0]))
# print(users[0] == users[1])
# print(users[0] == users[0])
# print(users[0] == users[3])

class Dog:

    num_legs = 4
    num_eyes = 2

    def __init__(self, name: str, age: int):

        self.name = name
        self.age = age

    def bark(self):
        print("woof")

class Border_Collie(Dog):

    energy_level = "high"

    def __init__(self, name: str, age: int, colour: str):
        super().__init__(name, age)
        self.colour = colour

class German_Shepard(Dog):
    
    def __init__(self, name: str, age: int, training: int):
        
        super().__init__(name, age)
        if isinstance(training, int):
            if training >= 0 and training <= 10:
                self.training = training
            else:
                raise Exception("training out of bounds [0,10]")
        else:
            raise Exception("training is not an integer")
        


Danny = Border_Collie("Danny", 4, "brown")
Danny.bark()
Mauler = German_Shepard("Mauler", 7, 5)

print(isinstance(Danny, German_Shepard))

