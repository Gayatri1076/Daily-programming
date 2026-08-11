using System;

class StudentDetails
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter your name:");
        string name = Console.ReadLine();

        Console.WriteLine("Enter your age:");
        int age = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine("\n--- Student Details ---");
        Console.WriteLine("Name: " + name);
        Console.WriteLine("Age: " + age);

        Console.ReadLine();
    }
}