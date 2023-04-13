class Car:
    no_of_wheel = 4  # this is static or class variable

    def __init__(self, model, color):
        self.model = model
        self.color = color


    def printCarModel(self):
        print(f"Car Model is {self.model}")

    @classmethod
    def printNoOfWheel(cls):
        print(cls.no_of_wheel)

    @staticmethod
    def areCarsGood():
        return "Yes"



bmw = Car("BMW", "Red")
print(bmw.color)

bmw.printCarModel()
# Car.printCarModel(bmw) # This is same as above

Car.printNoOfWheel()

print(Car.areCarsGood())