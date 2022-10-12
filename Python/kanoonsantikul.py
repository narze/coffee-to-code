coffee_with_special_ingredient = "C 	    o		f 		 				f 		 e 	   		  	 	e"
print("eating coffee_with_special_ingredient: ", coffee_with_special_ingredient)

brain_out = ''
for c in coffee_with_special_ingredient:
	if c == ' ':
		brain_out += "0"
	if c == '	':
		brain_out += "1"

out = int(brain_out, 2)
print(out.to_bytes((out.bit_length() + 7) // 8, 'big').decode())