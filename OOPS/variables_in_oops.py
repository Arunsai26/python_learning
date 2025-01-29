class Car:
    wheels=4
    def __init__(self):
        self.mil=6
        self.com="bmw"

A=Car()
B=Car()
A.mil=5
Car.wheels=5
print(A.mil,A.com,A.wheels)
print(B.mil,B.com,B.wheels)
        