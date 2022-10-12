package safesuk

import (
	"testing"
)

func TestCoffeeToCode(t *testing.T) {
	o := CoffeeToCode("Coffee")
	if "Code" != o {
		t.Error("It should be 'Code' but output is", o)
	}

	o = CoffeeToCode("I love Coffee")
	if "I love Code" != o {
		t.Error("It should be 'I love Code' but output is", o)
	}

	o = CoffeeToCode("I love Coffee and Coffee")
	if "I love Code and Code" != o {
		t.Error("It should be 'I love Code and Code' but output is", o)
	}

	o = CoffeeToCode("I love coffee and coffee")
	if "I love code and code" != o {
		t.Error("It should be 'I love code and code' but output is", o)
	}
}
