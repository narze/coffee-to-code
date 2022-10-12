initial_words = "Coffee"
removed_duplicate = ''.join(sorted(set(initial_words), key=initial_words.index))
result = removed_duplicate.replace("f", "d")
print(result)