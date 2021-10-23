package suradidchao

import (
	"errors"
	"strings"
)



func CoffeeToCode(input string) (string, error) {
	var result string
	lowercaseInput := strings.ToLower(input)
	if lowercaseInput != "coffee" {
		return result, errors.New("input string is not coffee, unacceptable")
	}
	result = strings.Replace(lowercaseInput, "coffee", "code", 1)
	return result, nil
}


