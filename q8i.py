c = input('Enter a character : ')[0]

if (c >= '0' and c <= '9'):
	print("number")
elif (c >= 'a' and c <='z'):
	print("alphabet")
elif (c >= 'A' and c <='Z'):
	print("alphabet")
else:
	print("Special character")