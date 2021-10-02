package safesuk

import (
	"strings"
)

func CoffeeToCode(s string) string {
	o := strings.ReplaceAll(s, "Coffee", "Code")
	o = strings.ReplaceAll(o, "coffee", "code")
	return o
}
