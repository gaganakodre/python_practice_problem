class Employee:
    """a sample example to practice the logging"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        print('created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.formate(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('honey', 'johnny')
emp_2 = Employee('justice', 'bieber')
