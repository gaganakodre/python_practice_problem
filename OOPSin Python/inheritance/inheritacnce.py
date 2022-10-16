class A:
    def features1(self):
        print("features 1 working")

    def features2(self):
        print("feature 2 is working")


class B(A): # B is child class and A is the parent class
    def features3(self):
        print("features 3 is working")

    def features4(self):
        print("feturre 4 is working")


c1=A()

c1.features1()
c1.features2()

b1=B()
b1.features1()
b1.features2()
b1.features3()
b1.features4()
