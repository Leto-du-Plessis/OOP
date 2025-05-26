# To appreciate what it is that object oriented programming can do for us, let's examine the alternative.
# Let's say that we'd like to represent a user profile that tracks a username, password and a favourite movie.
# The simplest approach would be to do the following:

username = "Leto"
password = "ThisPasswordIsTotallySecure"
favourite_movie = "Across the Spiderverse"

print(f"{username} likes {favourite_movie}.")

# job done.
# But now, what if we wanted to add another user?
# If we simply do:

username = "Joe"
password = "ThisPasswordIsNotSecure"
favourite_movie = "Saving Private Ryan"

print(f"{username} likes {favourite_movie}.")

# Cool, we've succesfully stored the new user in memory, but we've also overwritten the original user.
# We could use the following rather ugly solution: 

username2 = "Leto"
password2 = "ThisPasswordIsTotallySecure"
favourite_movie2 = "Across the Spiderverse"

print(f"{username} likes {favourite_movie} and {username2} likes {favourite_movie2}.")

# Great, now we have both users! But obviously this solution sucks. Not only is it ugly, but it's not easily scalable. We would have to manually write a new codeblock for each new user assignment.
# Let's look at a better solution.

def create_user (username: str, password: str, favourite_movie: str): 
    return {"username": username, "password": password, "favourite_movie": favourite_movie}

user1 = create_user("Leto", "ThisPasswordIsTotallySecure", "Across the Spiderverse")
user2 = create_user("Joe", "ThisPasswordIsNotSecure", "Saving Private Ryan")

print(f"{user1["username"]} likes {user1["favourite_movie"]} and {user2["username"]} likes {user2["favourite_movie"]}")

# We have made use of a python function and python dictionaries to generate and store our information more efficiently. 
# Incidently, python objects are fundamentally stored in a dictionary format so this example is quite relevant.
# Of course, we are still storing our users as individual variables. We can make a further improvement (in the sense of scalability)

users = [user1, user2]
users.append(create_user("Maria", "ThisPasswordIsExtremelySecure", "The Incredibles"))

print(" and ".join(f"{user["username"]} likes {user["favourite_movie"]}" for user in users) + ".")

# For the sake of pedagogy it's worth noting that it's generally going to be better to store users in a dictionary where the username is given as the key.
# This provides a significant lookup time speedup. O(N) -> O(1). But this is besides the point for now. 
# The structure we have now is actually quite a good way to store the information we want to store, as the information is now. 
# Let's say now that we want to check whether two users like the same movie. We could define a function to do this.

def compare_movie(movie1: str, movie2: str) -> bool:
    if movie1 == movie2:
        return True
    return False

print(compare_movie(users[0]["favourite_movie"], users[1]["favourite_movie"]))
print(compare_movie(users[0]["favourite_movie"], "Across the Spiderverse"))

# Now, we've introduced some level of nuisance into our workflow. Firstly, say we propagate our users list into a difference context. We need to explicitely
# bring our new function with us. Or else, we'd need to redefine compare_movie(). Now, in this case that's hardly a hardship, but consider how this might be 
# painful if the relevant function were more complex. 
# A second point is that, note we got a "True" boolean when we provided a string as an argument to compare against the first users favourite movie. This was the 
# intended behaviour in this case, but note that we may not want this behaviour since if we can provide an arbitrary string as an argument, that string could represent
# something other than a movie. 
# In other words, our function has no way to determine whether or not the provided strings are associated with the favourite_movie of a user. 
# We also have no real way to compare users. Say we add another user:

users.append(create_user("Leto", "ThisPasswordIsTotallySecure", "Across the Spiderverse"))

# Is this user the "same" as user 0? 

print(users[0] == users[3])

# This above comparison is making use of a dictionary equality method. Clearly, it says, yes, they are the same! 
# This might be what we wanted. But, what if this is a different user who just happens to have the same name, password and favourite movie? 
# The point is, we may want more control over this behaviour. 
# We could define a function which compares two users explicitely. However, we now have another function to carry around with us. 
# Furthermore, we would then lose the functionality of the == operator. There is a way to maintain this functionality ... 

