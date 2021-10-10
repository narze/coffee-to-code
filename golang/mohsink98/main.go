package main

import "fmt"

func convertToCode(chars []rune) []rune {
	code_word := "de"
	code_chars := []rune(code_word)
	for _, char := range code_chars {
		chars = append(chars, char)
	}
	return chars
}

func main() {
	coffee_word := "Coffee"
	chars := []rune(coffee_word)
	code_chars := convertToCode(chars[:len(chars)-4])
	fmt.Printf("%s -> %s", coffee_word, string(code_chars))
}
