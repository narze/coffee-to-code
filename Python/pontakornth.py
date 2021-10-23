# Very Evil version
coffee = "coffee"
ascii_coffee = list(map(ord, coffee))
f_position = ord("f")
d_position = ord("d")
e_position = ord("e")

def f_to_d(char_ord: int):
    """
    Convert f to d. Return the same character otherwise.

    Args:
        char_ord: Character in Unicode order

    Returns:
        str: If the character is f, convert to d
    """
    return d_position if char_ord == f_position else char_ord

ascii_coffee = list(map(f_to_d, ascii_coffee))
ascii_coffee.pop()
ascii_coffee.pop()
ascii_coffee[-1] = e_position
print("".join(map(chr, ascii_coffee)))

