x = int(input("Enter a number : "))

if x < 2:
	print("Invalid input")
	exit()

flag = 0
for elem in range(2,x):
	if x%elem == 0:
		flag = 1


if flag == 1:
	print("{} is not prime".format(x))
else:
	print("{} is prime".format(x))