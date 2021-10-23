package suradidchao

import (
	"fmt"
	"testing"
)


func TestCoffeeToCode(t *testing.T) {
	tcs := []struct{
		in string
		want string
	}{
		{
			in: "coffee",
			want: "code",
		},
		{
			in: "CoFFee",
			want: "code",
		},
		{
			in: "coffEe",
			want: "code",
		},
		{
			in: "CoFFee",
			want: "code",
		},
	}
	for pos, tc := range tcs {
		t.Run(fmt.Sprintf("test case no. %d", pos), func (t *testing.T){
			got, err := CoffeeToCode(tc.in)
			if err != nil {
				t.Error(err)
			}
			if got != tc.want {
				t.Error(fmt.Sprintf("want %s, but got %s", tc.want, got))
			}
		})
	}
}