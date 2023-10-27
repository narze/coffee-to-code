package main

import (
	"fmt"
	"strings"
)

func main() {
	var word string

	fmt.Println("What is the secret word?")
	fmt.Scanf("%s", &word)

	if (word != "Coffee") && (word != "coffee") {
		fmt.Println("Secret word invalid! Try again.")
	} else {
		fmt.Println(strings.Split(word, "")[0] + "ode")
	}
}
