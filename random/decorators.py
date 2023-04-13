def div(c, d):
    return c / d


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a,b)
    return inner


div1 = smart_div(div)
result = div1(2, 4)

print(result)

print("Inside: " + __name__)
