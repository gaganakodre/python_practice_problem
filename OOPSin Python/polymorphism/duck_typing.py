class Pycharm:
    def execute(self):
        print("running")
        print("compiling")

class Editor:
    def execute(self):
        print("spell check")
        print("indentation check")

        print("running")
        print("compiling")


class Laptop:
    def code(self, ide):
        ide.execute()


# ide = Pycharm()

lap1 = Laptop()
# lap1.code(ide)

ide=Editor()
lap1.code(ide)
