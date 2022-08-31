class Student:
    school='AVS'

    def __init__(self, m1, m2, m3):#instance method
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):# Accessor instance method
        return self.m1

    def set_m1(self,value):
         self.m1=value

    @classmethod
    def get_clsmethod(cls):#class method
        return cls.school

    def info():
        print("this is stdt cls and we are trying to get static method")




s1 = Student(1, 2, 3)
s2 = Student(4, 5, 6)


print(s1.average())


#to call the class methods
print(Student.get_clsmethod())


#to call the static method
Student.info()