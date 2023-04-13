class Car:
    no_of_wheel = 4  # this is static or class variable

    def __init__(self, model, color):
        self.model = model
        self.color = color


    @classmethod
    def printNoOfWheel(cls):
        print(cls.no_of_wheel)

    @staticmethod
    def areCarsGood():
        return "Yes"



bmw = Car("BMW", "Red")
print(bmw.color)

Car.printNoOfWheel()

print(Car.areCarsGood())