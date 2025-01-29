class A:
    def __init__(self):
        print("in a init")
    
    

    def f1(self):
        print("f1")
    def f2(self):
        print("f2")

class B(A):
    def  __init__(self):
        super().__init__()
        print("in b init")

        
    
        
    def f3(self):
        print("f3")
    def f4(self):
        print("f4")
class C(B,A):
    def __init__(self):
        super().__init__()
        print("in c init")
    def check(self):
        super().f1()
    def f5(self):
        print("f5")
 



# a1=B()
b1=C()
b1.check()


