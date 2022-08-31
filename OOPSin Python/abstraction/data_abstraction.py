from abc import ABC, abstractmethod


class Computer(ABC):  # this is of type abstract class

    @abstractmethod  # this is of type abstract method
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("its running")

class Programmer:
    def work(self,com):
        print("solving Bugs")
        com.process()

class Destktop(Computer):
    def process(self):
        print("hii")
com = Laptop()
# com.process()


pos=Programmer()
pos.work(com)

com1=Destktop()
com1.process()