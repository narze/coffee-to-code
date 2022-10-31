package coffeetocode_test

import (
	coffeetocode "coffee-to-code/vavar"
	"testing"
)

func TestCofeeToCode(t *testing.T) {
	output := coffeetocode.Coffee2code("coffee")
	if output != "code" {
		t.Logf("coffee is not convert to code : %s", output)
		t.Fail()
	}
}
