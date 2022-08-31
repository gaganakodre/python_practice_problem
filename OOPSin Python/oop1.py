class Computer:
    def __init__(self):
        self.name = "navin"
        self.age = 45

    def update(self):
        self.age = 90


com = Computer()  # object of the cls
com.age = 45
com.name = "gagana"

com.update()

print(id(com))  # id method used to print the address of the memory

print(com.age)
print(com.name)
