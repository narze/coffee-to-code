package nontw

import "testing"

func TestCoffeeToCode(t *testing.T) {

	tests := []struct {
		in, want string
	}{
		{"Coffee", "Code"},
		{"COffEe", "Code"},
		{"Cofee", "Cofee"},
		{"I love Coffee", "I love Code"},
		{"I love Coffee and Coffee", "I love Code and Code"},
		{"I love coffee and coffee", "I love code and code"},
	}

	for _, test := range tests {
		result := CoffeeToCode(test.in)
		if result != test.want {
			t.Errorf("Expect %s, but got %s", test.want, result)
		}
	}
}
