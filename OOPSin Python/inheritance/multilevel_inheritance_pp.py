class A:
    def __init__(self):
        pass

    def method1(self):
        print("1")


class B:
    def method2(self):
        print("2")


class C(A,B):
    def __init__(self):
        super().__init__()

    def method3(self):
        print("3")

obj1=A()
obj2=B()
obj3=C()

print(obj3.method2())
print(obj3.method3())
print(obj3.method1())
