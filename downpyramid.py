n= int(input("enter a number :"))

# 1 -> 2*n - 1
# 2 -> 2*n - 3
# 3 -> 2*n - 5

# ith -> 2*n - (2*i-1) = 2*n-2*i+1

i = 1 # line number
while i <= n:

     for j in range(1,2*i):
        print('*',end='')

     print('')

     i = i+1