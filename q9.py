s = input("Enter string : ")
c = input("Enter character : ")[0]

count = 0
for i in s:
	if i == c:
		count = count+1

print(count)

newc = input("Enter new character : ")[0]

replacedS = s.replace(c,newc)

print("String after replacing : " + replacedS)

firstremoved = s.replace(c,'',1)

print("String after removing first occurence : " + firstremoved)

allremoved = s.replace(c,"")

print("String after removing all occurence : " + allremoved)
