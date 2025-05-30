
public class Test {
    
    // Note making use of the overloaded methods below.
    static User user1 = new User("Leto", "ThisPasswordIsTotallySecure", "Across the Spiderverse");
    static User user2 = new User("Alice", "Saving Private Ryan");
    static User user3 = new User("Mario", "The Grand Budapest Hotel");
    static User user4 = new User("Jason", "The Grand Budapest Hotel");

    static Border_Collie dog1 = new Border_Collie("Danny", "male");
    static German_Shepard dog2 = new German_Shepard("Bennet", "male");
    static German_Shepard dog3 = new German_Shepard("Sally", "female", 10);

    // Note that the main method is the method that is run when a compiled Java file (a .class file) is executed.
    public static void main() {

        // User output
        System.out.println("Output from the User class");
        System.out.printf("%s likes %s. \n", user1.username, user1.favourite_movie);
        System.out.printf(user1.compare_movie_output(user2));
        System.out.printf(user3.compare_movie_output(user4));

        // Dog output
        System.out.println("\nOutput from the Dog class and subclasses");
        System.out.println(dog1.description());
        System.out.println(dog2.description());
        dog1.bark();
        dog2.bark();
        dog3.bark_four_times();
        // Note as per last time, dog1 is both an instance of the Dog class and the Border_Collie class.
        System.out.println(dog1 instanceof Dog);
        System.out.println(dog1 instanceof Border_Collie);
        // But even though dog1 and dog2 are both dogs, if we compare their classes directly they are not equivalent since they are primarily a border_collie and a german_shepard respectively.
        System.out.println(dog1.getClass().equals(dog2.getClass()));
        // On the other hand of course.
        System.out.println(dog2.getClass().equals(dog3.getClass()));
    }

}
