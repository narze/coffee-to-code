#Coffee to Code

def coffee_to_code() -> str:

    coffee = "coffee"
    replace_dict = {"ff": "d", "ee": "e"}

    coffee = list(coffee.lower())

    def replace(coffee: list) -> str:
        """
        Replaces the indexes at which "ff" and "ee" are found.
        """
        for pattern in replace_dict:
            indexes = search(pattern, coffee)
            for index in indexes:
                del coffee[index : index + len(pattern)]
                coffee.insert(index, replace_dict.get(pattern))
        coffee = "".join(coffee)
        return coffee

    return replace(coffee)


def search(pat: str, txt: str) -> list:
    """
    :param pat: the substring to be found
    :type pat: str
    :param txt: the string in which pat needs to be found in
    :type txt: str
    :return: list with the indexes of the substring
    """

    pat_len = len(pat)
    txt_len = len(txt)
    indexes = []
    # Loop to iterate through the index of each element
    for x in range(txt_len - pat_len + 1):
        increment = 0
        while increment < pat_len:
            if txt[x + increment] != pat[increment]:
                # The elements of txt and pat are not equal.
                break
            # 1 is added to the increment to check against the next element in the next iteration.
            increment += 1

        # If the loop broke when the length of the pattern is equal to the
        # length of the substring sound in the text.
        # This implies, it is part of the text until pat is over.
        # This means that the pattern is in the text at that position.
        
        if increment == pat_len:
            indexes.append(x)

    return indexes


print(coffee_to_code())
