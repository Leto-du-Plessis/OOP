public class Test {
    
    // Note making use of the overloaded methods below.
    static User user1 = new User("Leto", "ThisPasswordIsTotallySecure", "Across the Spiderverse");
    static User user2 = new User("Alice", "Saving Private Ryan");
    static User user3 = new User("Mario", "The Grand Budapest Hotel");
    static User user4 = new User("Jason", "The Grand Budapest Hotel");

    // Note that the main method is the method that is run when a compiled Java file (a .class file) is executed.
    public static void main() {

        System.out.printf("%s likes %s. \n", user1.username, user1.favourite_movie);
        System.out.printf(user1.compare_movie_output(user2));
        System.out.printf(user3.compare_movie_output(user4));

    }

}
