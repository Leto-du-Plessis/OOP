// A very basic Java program.

public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello!");
    }
}

// A small handful of comments about this example in the context of talking about OOP in Python. 
// Note how even this simple example is a defined class. All Java code is written within a class, unlike in Python where this is optional.
// This is due to the deployable design philosophy of Java.

// Note that the keyword "public" controls the access scope of the class. In this case, it is accessible by any other class.
// The keyword "private" would restrict access to a method, field to within the class itself. Leaving no keyword (implicitely the "default" keyword) means that the method, field or class is only accessible within the package. 
// The "static" keyword on the other hand tells us that the method is, well, static, and hence memory allocation can be made at compile time.
// The "void" keyword tells us that the method does not return any values. If the method did return a variable, we would need to replace "void" with the return variable type, for instance, "String". 
// All of the above is an example of Java's static nature (as opposed to the dynamic nature of Python). 
// In other words, we need to tell our Java compiler what our variables/classes/methods are, and how they're going to be used.
// Python does this process automatically and dynamically. This makes Python slower, but more approachable. 

