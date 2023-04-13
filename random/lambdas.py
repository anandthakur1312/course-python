from functools import reduce
f = lambda a : a % 2 == 0

m = lambda a: a*a

print(f(2))


l1 = [2,3,4,5,6]

evenList = list(filter(f, l1))

print(list(map(lambda a: a*a, filter(f, l1))))

sum = reduce(lambda a, b: a+b, evenList)

print(sum)





######SWAP############

a = 2
b = 3

print(a)
print(b)

a,b = b,a

print(a)
print(b)
