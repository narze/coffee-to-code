package coffeetocode

import "strings"

func Coffee2code(input string) string {
	if strings.ToLower(input) != "coffee" {
		panic("invalid")
	}
	return strings.Join([]string{input[:2], "de"}, "")
}
