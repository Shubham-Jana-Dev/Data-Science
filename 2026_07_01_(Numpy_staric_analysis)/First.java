import java.util.Scanner;
public class First{
    public static int add(){
        return 23+45;
    }
    public static void main(String[] args){
        int result = add();
        System.out.println(result);
        UserInputDemo.main(args);
    }
}
class UserInputDemo{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        System.out.print("Enter your GPA: ");
        double gpa = scanner.nextDouble();

        System.out.println("\n --- User Frofile ---");
        System.out.println("Name: " + name);
        System.out.println("Age: "+age);
        System.out.println("GPA: " + gpa);

        scanner.close();
       
    }
}
