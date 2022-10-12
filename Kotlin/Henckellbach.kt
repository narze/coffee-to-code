fun coffeeToCode(): String {
    val text = "Coffee"

    return text
        .toCharArray()
        .distinct()
        .map { it.code }
        .map { Char(if (it == 102) it - 2 else it) }
        .joinToString("")
}

fun main() {
    println(coffeeToCode())
}
