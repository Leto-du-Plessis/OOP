// Finally, let's reexamine our Dog example so that we can get a feel for class inheritance in Java

// I'm going to use the opportunity to introduce another concept, which did not appear in Python.
// Namely: abstraction.
// Abstract classes provide a template for child classes to follow through inheritance. 
// You cannot instantiate an object from an abstract class.

abstract class Dog {
    
    // Note here the use of class versus instance fields. 
    String name;                  // Instance field
    String gender;
    static int num_of_legs = 4;   // Class field 
    static int num_of_eyes = 2;

    public void bark() {
        System.out.printf("%s: Woof!\n", name);
    };

    // Note how the below abstract method does not have a body. This must be specified by any child classes, as will be demonstrated.
    public abstract String description();

}

// Inheritance is specified in Java using the keyword "extends".
// Note that the IDE will throw a fit if we do not implement the abstract description method. 
class Border_Collie extends Dog {

    // Our constructor instantiates the instance fields we didn't touch in the abstract class. 
    Border_Collie(String name, String gender) {
        this.name = name;
        this.gender = gender;
    }

    // Of course, we inhereit the bark() method from the parent class Dog. 

    // Now we implement the abstract method description().
    public String description() {
        return String.format("%s is a %s border collie!", name, gender);
    }
}

class German_Shepard extends Dog {

    // As a demonstration that we can add additional instance fields as we could in Python.
    int training;

    German_Shepard(String name, String gender, int training) {
        this.name = name;
        this.gender = gender;
        this.training = training;
    }

    // Overloading the constructor.
    German_Shepard(String name, String gender) {
        this.name = name;
        this.gender = gender;
        this.training = 0;
    }

    // Of course, we can also overwrite methods.
    public void bark() {
        System.out.printf("%s: Grrr!\n", name);
    }

    // And we can add new methods.
    public void bark_four_times() {
        for (int i = 0; i < 4; i++) {
            if (i%2 == 0) {
                System.out.printf("%s: Grrr!\n", name);
            } else {
                System.out.printf("%s: Woof!\n", name);
            }
        }
    }

    // And we also need to implement the abstract method again.
    public String description() {
        return String.format("%s is a %s german shepard!", name, gender);
    }

}
