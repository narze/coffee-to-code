k = 0x436f25090100 # This must be something that important !
coffee = "Coffee"
coffee_h3x = ""

for c in coffee:
	coffee_h3x += '{:x}'.format(ord(c))
coffee_h3x = int(hex(int(coffee_h3x, 16)), 16)

dah3ll = '{:x}'.format(coffee_h3x ^ k) # XOR Decryption
dah3ll_object = bytes.fromhex(dah3ll)
dah3ll_string = dah3ll_object.decode("ASCII")

print(dah3ll_string)  # print 'Code'
