using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Gayatri
{
    class Arithmetic_Operations
    {
       static void Main(string[] Args) 
        { 
            double num1, num2; 
 
            Console.Write("Enter first number: "); 
            num1 = Convert.ToDouble(Console.ReadLine()); 
 
            Console.Write("Enter second number: "); 
            num2 = Convert.ToDouble(Console.ReadLine()); 
 
            Console.WriteLine("\nArithmetic Operations:"); 
            Console.WriteLine("Addition: " + (num1 + num2)); 
            Console.WriteLine("Subtraction: " + (num1 - num2)); 
            Console.WriteLine("Multiplication: " + (num1 * num2)); 
            Console.WriteLine("Division: " + (num1 / num2)); 
            Console.WriteLine("Modulus: " + (num1 % num2)); 
            Console.ReadLine(); 
        } 
    } 
} 

