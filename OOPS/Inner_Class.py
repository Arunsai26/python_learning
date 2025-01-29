class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    # class of classes
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class Laptop:
        def __init__(self):
            self.brand="dell"
            self.cpu='15'
            self.ram=5
        def show(self):
            print(self.brand,self.cpu,self.ram)
          
    
A=Student('arunsai',2)          
A.show()
# access class of classes
lap1=A.lap

lap1=Student.Laptop()


        

        