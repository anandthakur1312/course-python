
a = 10

def something():
    a = 9
    # global a
    # a = 15
    print("id of global a before change: " + str(id(globals()['a'])))
    globals()['a'] = 15
    print("id of global a after change: " + str(id(globals()['a'])))
    x = globals()['a']
    print("id of x: " + str(id(x)))
    print("2. local : " + str(a))
    print("3. global after change : " + str(x))

print("1. global : " + str(a))
print("id of a: " + str(id(a)))

something()