class A:
    def __init__(self):
        pass

    def method1(self):
        print("method1")

    def method2(self):
        print("method2")


class B(A):

    def method3(self):
        print("method3")

    def method4(self):
        print("method4")


class C(B):

    def method5(self):
        print("method5")

    def method6(self):
        print("method6")


obj1 = A()  # we can acess only 1 and 2
obj2 = B()  # we can acess only 1,2,3 and 4
obj3 = C()  # we can acess only 1,2,3,4,5 and 6
print(obj3.method2())
print(obj3.method3())
print(obj3.method1(), obj3.method2(), obj3.method3(), obj3.method4(), obj3.method5(), obj3.method6())
print(obj2.method1(), obj2.method2(), obj2.method3(), obj2.method4())
print(obj1.method1(), obj1.method2())

