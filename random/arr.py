import array

intArray = array.array('i', [2, 3, 4, 5, 6])

(addr, size) = intArray.buffer_info()
print('Size is : {} and Address is : {}'.format(size, addr))

for i in range(len(intArray)):
    print(i)

for e in intArray:
    print(e)


intArrayCopy = array.array(intArray.typecode, (a*a for a in intArray))

for e in intArrayCopy:
    print(e)