class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature 2")


# class B(A):
#     def __init__(self):
#         # if we want to access the init of both the class we have to use the super method init
#         super().__init__()
#         print("in B init")
#
#     def feature3(self):
#         print("feature 3")
#
#     def feature4(self):
#         print("feature 4")

class B:
    def __init__(self):
        # if we want to access the init of both the class we have to use the super method init
        super().__init__()
        print("in B init")

    def feature1(self):
        print("feature 3")

    def feature4(self):
        print("feature 4")


# here it follows MRO(Method resolution order)it will follow from left to right concpet
# 1st it will fine the init of itself and left so it will print A class init
class C(A, B):
    def __init__(self):
        super().__init__()
        print("c init")


# a1=B()
b1 = C()
b1.feature1()
