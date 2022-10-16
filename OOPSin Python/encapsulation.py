# Creating a Base class
class Base:
    def __init__(self):
        self.a = "dog"
        self.__c = "cat"  # private attribute


# derived class
class Derived(Base):
    def __init__(self):

        super().__init__()
        print("Calling private member of base class: ")
        print(self.__c)


if __name__ == '__main__':
    # creating object of base cls to access the private variable
    obj1 = Base()
    print(obj1.a)
    # this will give the attribute error
    # obj2 = Derived()
    # print(obj2.a)
