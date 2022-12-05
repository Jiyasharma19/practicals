from math import sqrt

print("Eqaution : ax^2 + bx + c = 0")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

det = b**2 - 4*a*c
# det should be positive

if det < 0:
	print("Root does not exist")
	exit()

det = sqrt(det)

r1 = (-b + det)/(2*a)
r2 = (-b - det)/(2*a)

print("Root 1: {}".format(r1))
print("Root 2: {}".format(r2))