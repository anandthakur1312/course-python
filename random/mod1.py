from mod2 import func2

# Notes when we import any module then it will run any function if there is a function execution without __name__ == __main__ check
def fun1():
    print("func one")

fun1()