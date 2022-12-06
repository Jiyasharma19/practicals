n = int(input("Enter a number : "))

if n <= 1 :
	print("Invalid Input")
	exit()

def checkPrime(x):
	flag = 0
	for i in range(2,x):
		if x%i == 0:
			flag = 1
	
	if flag == 0:
		return True
	else:
		return False
	

i = 2
while i <= n:
	if checkPrime(i) :
		print(i)

	i = i+1