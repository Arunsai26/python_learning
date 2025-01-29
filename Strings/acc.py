class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print("Your are insider a constructor class")
        
    def confif(self):
        print("hello world")
        print("Your confif is :",self.cpu,self.ram)

A=Computer("i5",4)
B=Computer("ryzen",6)
A.confif()
B.confif()
print(id(A))


