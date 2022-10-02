using System.Text.RegularExpressions;

class Program
{
    public static void Main()
    {
        string? input = Console.ReadLine();
        if(input == null)
        {
            Console.WriteLine("Something Went Wrong");
        }
        else
        {
            input = Regex.Replace(input,"coffee","code", RegexOptions.IgnoreCase);
            Console.WriteLine(input);
        }
    }
}