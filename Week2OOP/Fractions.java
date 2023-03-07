import java.util.Scanner;

public class Fractions
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the fraction (in the format x/y): ");
        String fractionStr = input.nextLine(); // reads input and stores as string
        String[] parts = fractionStr.split("/"); // creates string array called parts and splits it at '/'
        int numerator = Integer.parseInt(parts[0]); // parseint converts indexed 'parts' value into an int
        int denominator = Integer.parseInt(parts[1]);
        float result = (float) numerator / denominator;
        System.out.println(fractionStr + " = " + result);
    }
}
