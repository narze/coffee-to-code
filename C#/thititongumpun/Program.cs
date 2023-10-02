using System.Globalization;

class Program
{
    private static void Main(string[] args)
    {
        {
            string input = "";

            while (input.ToLower() != "coffee")
            {
                Console.WriteLine("Please input Coffee or COFFEE: ");
                input = Console.ReadLine()!;
                if (input.ToLower() == "coffee")
                {
                    Console.WriteLine(ToTitleCase("code"));
                }
            }
            Environment.Exit(0);
        }
    }

    private static string ToTitleCase(string str)
    {
        var textInfo = new CultureInfo("en-US", false).TextInfo;
        return textInfo.ToTitleCase(str);
    }
}