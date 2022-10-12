using System;

namespace coffee_to_code
{
    class Program
    {
        static void Main(string[] args)
        {
            string inputString;
            string correctString;
            
            if(args.Length > 0)
                inputString = String.Join(" ", args);
            else
                inputString = "Coffee";

            Console.WriteLine($" Input : {inputString}");
            correctString = inputString.Replace("Coffee", "Code");
            Console.WriteLine($"Output : {correctString}");
        }
    }
}
