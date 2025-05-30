// Let's create a similar User class to what we had before in Python, and then we'll create a Test class in another file to actually test it.

public class User {

    // In Java, we need to declare the variables that will belong to an object (fields), even if we don't immediately assign them.
    String username;
    String password;
    String favourite_movie; 
    // We can also assign variables at declaration. For instance:
    static String type = "User";
    // Note that we cannot use "static" for the other three fields since their values are not available at compile time.
    // In this case, we can think of the static field as belonging to the class instead of an instance of the class since all User objects will have the same type field.
    
    // We now need to create a constructor method (analogous to our __init__() method in Python)
    // Note below, what were "type hints" in Python are now required type declarations. 
    // Java is fussy and we need to tell it exactly what type of variable to expect. 
    // Finally, note the use of this. instead of self. to reference internal fields. This is only necessary if the method variables and internal fields have the same name. 
    public User(String username, String password, String favourite_movie) {
        this.username = username;
        this.password = password; 
        this.favourite_movie = favourite_movie; 
    }

    // Just to quickly demonstrate method overloading. I can define two different constructors with different expected arguments.
    // When creating a User object, the correct constructor will be chosen depending on what arguments we pass.
    // Note that I could also leave the password field unassigned, with the intention of having it potentially set later. But that is bad practice unless necessary.
    public User(String username, String favourite_movie) {
        this.username = username;
        this.password = "password";
        this.favourite_movie = favourite_movie;
    }

    // Now let's define the comparison methods we had before. 
    // In this case we must use public NOT static since the comparison requires the specific object fields.
    // Later I will define a static method which we can use to the same effect. 
    // Note that we cannot use the == operator to compare Strings, because a String object is not a primitive like an int, bool or float.
    // For non primitive objects, the == operator compares memory addresses, not values. 
    // The .equals() method provides the functionality we seek. 
    // Note that it's generally good practice to define this explicitely (overwrite the default) for custom classes.
    public boolean compare_movie(User other_user) {
        if (this.favourite_movie.equals(other_user.favourite_movie)) {
            return true; 
        } else {
            return false;
        }
    }

    // Now, note that instead of defining a method with a new name or using type comparisons, we can simply overload the method to introduce the extra functionality.
    public boolean compare_movie(String favourite_movie) {
        if (this.favourite_movie.equals(favourite_movie)) {
            return true;
        } else {
            return false;
        }
    }

    // Let's now define the static class method I spoke about earlier
    // Note that in a static method, we cannot access this. Hence, we need two arguments
    static boolean compare_movie(User user1, User user2) {
        if (user1.favourite_movie.equals(user2.favourite_movie)) {
            return true;
        } else {
            return false;
        }
    }

    // Can you write a further overload method to extend the class method to work for String arguments? 

    public String compare_movie_output(User other_user) { 
        if (this.compare_movie(other_user)) {
            return String.format("%s and %s like the same movie! \n", this.username, other_user.username);
        } else {
            return String.format("%s and %s do not like the same movie! \n", this.username, other_user.username);
        }
    }
}
