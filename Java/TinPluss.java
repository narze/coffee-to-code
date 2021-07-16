// Usage java Java/Tinpluss.java

import java.util.*;

public class TinPluss
{
public static void main(String args[]) 
  {
  String[] Coffee = "Coffee".split("");
  List<String> CoffeeList = Arrays.asList(Coffee);
  Set<String> set = new LinkedHashSet<>(CoffeeList);
  String CoffeeString = String.join("", set);
  String Code = CoffeeString.replace("f","d");
  System.out.println(Code);
  }
}
