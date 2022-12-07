l = [1,2,4,3,5,4,"whkbf","wkhf","kwhdbf",3.44]

ans1 = []
for item in l : 
    if(isinstance(item,int) and item%2 == 0) :
        ans1.append(item**3)

print("Using for loop : ",end='')
print(ans1)


ans2 = [item**3 for item in l if (isinstance(item,int) and item%2 == 0)]
print("Using list compression : ",end='')
print(ans2)