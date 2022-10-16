class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()  # we have to create the object of inner cls inside outer cls

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        """
        Inner class to access the info
        """

        def __init__(self):
            self.brand = "Hp"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('narayan', 1)
s2 = Student('nayana', 2)

# print(s1.name, s2.name, s1.rollno, s2.rollno)
s1.show()

# to access the inner cls
print(s1.lap.brand)  # 1 way to access the inner cls

# another way
lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))

# to get the class we can get
lap1 = Student.Laptop()
