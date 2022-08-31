class A:
    def __init__(self):
        self.__tech = None
        self.course="python program"
        self.__tech="python"

    def courseName(self):
        return self.__tech+self.course

ob=A()
print(ob.course)
print(ob._A__tech)
print(ob.courseName())