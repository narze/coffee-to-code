package main

import (
	"fmt"
	"strings"
)

func removeDuplicateChr(strSlice []rune) string {
	allKeys := make(map[rune]bool)
	list := []rune{}
	for _, item := range strSlice {
		if _, value := allKeys[item]; !value {
			allKeys[item] = true
			list = append(list, item)
		}
	}
	return string(list)
}

func convertToCode(text string) string {
	newStr := removeDuplicateChr([]rune(text))
	return strings.ReplaceAll(newStr, "f", "d")
}

func main() {
	coffee := "coffee"
	fmt.Printf("coffee ===> %s", convertToCode(coffee))
}
