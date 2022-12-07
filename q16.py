t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

tp1=t1[:5]
tp2=t1[5:]

print(tp1)

print(tp2)

eventp = tuple()
for i in t1:
    if(i%2 == 0) : 
        eventp = eventp + (i,)

print("Even tuple : ")
print(eventp)

t2 = (11,13,15)
t1 = t1 + t2 

print(t1)

print("Max : {}".format(max(t1)))
print("Min : {}".format(min(t1)))