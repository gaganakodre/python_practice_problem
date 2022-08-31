# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name)
        print(self.id)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.id))


# child class
class Employee(Person):
    def __init__(self, name, id, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self, name, id)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.i))
        print("Post: {}".format(self.post))


#  object variable
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function
# its instance
a.display()
a.details()
