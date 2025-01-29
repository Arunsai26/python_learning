class Student:
    school="arunsai"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        print("working in instance zone")
        return (self.m1+self.m2+self.m3)//3
    @classmethod
    def getschoolname(cls):
        print("your are in class zone")
        cls.school="koya Aruunsai"
    @staticmethod
    def info():
        print("your are in static zone")

A=Student(10,20,30)
A.avg()
A.getschoolname()
A.info()

    


        