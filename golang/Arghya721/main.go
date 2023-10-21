package main

import (
	"fmt"
)

// remove duplicate characters from rune
func removeDuplicate(runes []rune) []rune {
	var result []rune
	for _, r := range runes {
		if !contains(result, r) {
			result = append(result, r)
		}
	}
	return result
}

// check if rune is present in slice
func contains(runes []rune, r rune) bool {
	for _, v := range runes {
		if v == r {
			return true
		}
	}
	return false
}

// convert coffee to code
func CoffeeToCode(coffee string) string {

	// convert coffee to rune to iterate over each character
	coffeeRune := []rune(coffee)

	// iterate over each character and replace 'f' with 'd' and 'F' with 'D'
	for i, char := range coffeeRune {
		if char == 'f' || char == 'F' {
			coffeeRune[i] -= 2
		}
	}

	// remove all duplicate characters
	coffeeRune = removeDuplicate(coffeeRune)

	// convert rune to string
	code := string(coffeeRune)

	return code

}

func main() {
	fmt.Println(CoffeeToCode("Coffee"))
}
