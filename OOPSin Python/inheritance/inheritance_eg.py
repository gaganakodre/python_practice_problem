class A:
    def __init__(self):
        pass

    def method1(self):
        print("method 1")

    def method2(self):
        print("method 3")

class B(A):

    def method3(self):
        print("method3")

    def method4(self):
        print("method4")

obj1=A()
obj= B()
#here by using child class we can access all the methods in both the class
obj.method1()