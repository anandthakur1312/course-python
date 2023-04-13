def func2():
    print("func two")

if __name__ == "__main__": # If we remove this if condition then func2() will be run by every import of this module
    func2()