str1 = input("Enter string 1 : ")
str2 = input("Enter string 2 : ")
n = int(input("Enter number of char's to swap : "))

if n > min(len(str1),len(str2)):
    print("Invalid Input")
    exit()

temp = str1[:n]
str1 = str2[:n] + str1[n:]
str2 = temp + str2[n:]

print("String after swapping : ")
print("str1 : " + str1)
print("str2 : " + str2)