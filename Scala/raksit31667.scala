object raksit31667 {
    def main(args: Array[String]): Unit = {
        val coffee: String = "Coffee"
        val coffeeList: List[String] = coffee.split("").map(_.trim).toList
        val coffeeSet: Set[String] = coffeeList.toSet
        val codeSet: Set[String] = coffeeSet.map { case "f" => "d"; case x => x }
        println(codeSet.mkString(""))
    }
}