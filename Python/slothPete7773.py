coffee = 'coffee'
word = [char for char in coffee]
word = list(filter(lambda char: char in ['c', 'o'], word))
word.append('de')
print("".join(word))
