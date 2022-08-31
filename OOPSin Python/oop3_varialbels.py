class Car:
    wheels = 4

    def __init__(self):
        """
        Function to initialize the variables

        variables:creating the instance variables
        """
        self.mil = 10
        self.com = "benz"


c1 = Car()
c2 = Car()

# to change the instance variables
c1.mil = 8
c1.com = "bmw"

# to change the static or class variable
Car.wheels = 8
print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
