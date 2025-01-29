class PyCharmm:
    def execute(self):
        print("compiling")
        print("running")
    
class Laptop:
    def code(self,ide):
        ide.execute()

# mention ide
ide=PyCharmm()
lap1=Laptop()
lap1.code(ide)