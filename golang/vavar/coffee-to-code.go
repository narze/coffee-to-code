package coffeetocode

import "strings"

func coffee2code(input string) string {
	if strings.ToLower(input) != "coffee" {
		panic("invalid")
	}
	return strings.Join([]string{input[:2], "de"}, "")
}
