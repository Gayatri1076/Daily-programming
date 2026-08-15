using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Gayatri
{
    class Input_Output
    {
        static void Main(string[] args)
        {
            Console.WriteLine("___Basic Input/Output Program___");

            Console.WriteLine("Enter Your Name:");
            string name = Console.ReadLine();

            Console.WriteLine("Enter Your Age:");
            int Age = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Hello {0}, you are {1} years old.", name, Age);

            Console.ReadLine();
        }
    }
}




