text = input("Enter first string : ")
pattern = input("Enter second string : ")

lt = len(text)
lp = len(pattern)

ans = []

for i in range(0,lt-lp+1):
    if pattern == text[i:i+lp]:
        ans.append(i)

print("Indices of occurences : ",end='')
print(ans)