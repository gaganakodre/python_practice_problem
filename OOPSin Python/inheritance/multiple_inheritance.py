class A:
    def __init__(self):
        print("A init")

    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature 2")


class B:


    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("feature 4")


class C(A,B):#multiple inheritance
    def feature5(self):
        print("feature 5")

    def feature6(self):
        print("feature 6")


c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature6()
c1.feature5()
