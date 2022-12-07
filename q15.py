cubes = {}

for i in range(1,6):
    cubes[i] = i**3

for k in cubes.keys():
    print("{} : {}".format(k,cubes[k]))