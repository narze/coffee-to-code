package xyz.vallat.louis;

public class LouisVallat {

    private final static String aLotOfCoffee = "[cC][oO][fF][fF][eE][eE]";

    public static void main(String[] args) {
        String beverages[] = { "Coffee", "Code", "Tea", "Tux", "coffee",
            "Programmers love to ? coffee!", "Doom", "Coffee",
            "Programmers are at it again! They stole all the coffee!",
            "Coffee may have been turned into some beautiful coffeE",
            "This coffee is awful.", "Looks like I self-roasted myself by using my own coffee!"
        };
        for (String beverage : beverages) System.out.println(coffeeConvertor(beverage));
    }

    /**
     * The allmighty beverage detector allied with a coffee converter.
     *
     * @param potentialBeverage A potential beverage to... study.
     * @return the beverage of the gods may have been consumed, who knows?
     */
    private static String coffeeConvertor(String potentialBeverage) {
        if (potentialBeverage.matches(".*" + aLotOfCoffee + ".*"))                              // Have we found the secret coffee?
            return coffeeConvertor(potentialBeverage.replaceFirst(aLotOfCoffee, "code"));       // It's coffee! replace it with *code* and re-do again just in case there's another one
        else return potentialBeverage;                                                          // It doesn't contain coffee, nothing of interest here I believe.
    }
}

