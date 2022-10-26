class Program
{
    static void Main()
    {
        bool drickAble = true;
        while (drickAble)
        {
            try
            {
                Console.WriteLine("What do you want?");
                string coffeeFillter = Console.ReadLine();
                string[] textSplit = coffeeFillter.Split(' ');
                string coffeeDrink = "";
                if (coffeeFillter != null || coffeeFillter != "")
                {
                    for (int i = 1; i < textSplit.Length; i++)
                    {
                        if (textSplit[i].ToLower() == "coffee")
                        {
                            textSplit[i] = "Code";
                        }
                        coffeeDrink += textSplit[i] + " ";
                    }
                    Console.WriteLine("no i think you need :" + coffeeDrink);
                    Console.WriteLine("you want to drink again ? 1:yes 2:no");
                    string choice = Console.ReadLine();
                    if (Convert.ToInt32(choice) == 2)
                    {
                        Console.WriteLine("ok good bye ");
                        drickAble = false;
                    }
                }
                else
                {
                    Console.WriteLine("try again");
                }
            }
            catch
            {
                Console.WriteLine("Error !!!! try again");
            }
            Console.ReadLine();
        }
    }
}
    
