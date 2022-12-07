n = int(input("Enter number of lines : "))

i = 1 # number of stars in line
while i <= 2*n-1:
    for j in range(1,i+1):
        print('*',end='')
    print('')
    i = i+2