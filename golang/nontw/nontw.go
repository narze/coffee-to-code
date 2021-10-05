package nontw

import (
	"regexp"
)

func CoffeeToCode(s string) string {
	r := regexp.MustCompile(`([Cc])[Oo][Ff][Ff][Ee][Ee]`)
	return r.ReplaceAllString(s, "${1}ode")
}
