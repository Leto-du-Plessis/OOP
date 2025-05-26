

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