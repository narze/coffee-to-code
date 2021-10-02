using System;
//When Someone told you your code lack Passion =>
namespace F3nn1t0
{
    public class Program
    {
        //I Receive the Coffee
        //You Receive the Code
        public static void Main(string[] args)
        {
            var ElementArray = new string[] { "c", "o", "f", "e" }; //Element of words that construct in "Coffee"
            var Coffee = ""; //Coffee Holder
            var Code = ""; //Code Holder

            for (int i = 0; i < ElementArray.Length; i++)
            {
                var Word = ElementArray[i];

                //Switcherooooo
                switch (Word)
                {
                    case "c":
                        Coffee = Coffee.Insert(0, Word.ToUpper());
                        continue;
                    case "o":
                        Coffee = Coffee.Insert(1, Word);
                        continue;
                    case "f":
                        Coffee = Coffee.Insert(2, Word);
                        Coffee = Coffee.Insert(3, Word);
                        continue;
                    case "e":
                        Coffee = Coffee.Insert(4, Word);
                        Coffee = Coffee.Insert(5, Word);
                        continue;
                    default:
                        break;
                }
            }

            //Switcherooooo Season 2
            switch (Coffee)
            {
                case "Coffee":
                    for (int i = 0; i < ElementArray.Length; i++)
                    {
                        var Word = ElementArray[i];

                        switch (Word)
                        {
                            case "c":
                                Code = Code.Insert(0, Word.ToUpper());
                                continue;
                            case "o":
                                Code = Code.Insert(1, Word);
                                continue;
                            case "f":
                                Code = Code.Insert(2, "d");
                                continue;
                            case "e":
                                Code = Code.Insert(3, Word);
                                continue;
                            default:
                                break;
                        }
                    }
                    break;
                default:
                    break;
            }

            // Output Result
            Console.WriteLine(Code);
        }
    }
    //Time Well Spent!
}
