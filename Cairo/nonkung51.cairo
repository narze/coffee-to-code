%builtins output

from starkware.cairo.common.serialize import serialize_word

func main{output_ptr: felt*}() {
    tempvar coffee = 'coffee';
    tempvar code = 'code';
    tempvar diff = coffee - code;

    tempvar coffeeToCode = coffee - diff;

    serialize_word(coffeeToCode);
    return ();
}
