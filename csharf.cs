using System;

namespace HelloWorldApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // Prompt the user for input
            Console.Write("Enter your name: ");
            
            // Read the input from the console
            string userName = Console.ReadLine();
            
            // Display a personalized greeting
            Console.WriteLine($"Hello, {userName}! Welcome to C# programming.");
            
            // Keep the console window open
            Console.WriteLine("\nPress any key to exit...");
            Console.ReadKey();
        }
    }
}