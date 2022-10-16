# a=5
# b=9
# print(a+b)
#
# print(int.__add__(a,b))
# if we want to perform any operation on the objects we have to define methods
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3
    def __gt__(self, other):
        r1=self.m1+other.m1
        r2=self.m2+other.m2
        if r1>r2:
            return  True
        else:
            return  False

    def __str__(self):
        return "{},{}". format(self.m1,self.m2)
        # return self.m1,self.m2




s1 = Student(33, 44)
s2 = Student(33, 44)

s3 = s1 + s2

print(s3.m1)

if s1 > s2:#>not supported between instances
    print("s1 win")
else:
    print("s2")


print(s1.__str__()) # if we want to print this we have to call this method called __str__