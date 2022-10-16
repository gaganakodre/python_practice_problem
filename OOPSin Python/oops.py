class Computers:

    def __init__(self, cpu, ram):
        """
        Function used to initialize the variables we use this method, and it will be called automatically
        """
        self.cpu = cpu
        self.ram = ram

    def config(self):  # object to pass

        print("config: ",self.ram,self.cpu)


com1 = Computers('i5', 16)  # object
comp = Computers('ryzen', 8)

# access the class
Computers.config(com1)
Computers.config(comp)

# most used syntax
com1.config()
comp.config()

a = 5
a.bit_length()  # Number of bits necessary to represent self in binary.
