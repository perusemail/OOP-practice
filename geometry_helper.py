import math

class Shape():
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width

    def area(self,length,width):
        print("Area = ",int(length)*int(width))

    def perimeter(self, length, width):
        print("Perimeter = ",(int(length)*2)+(2*(int(width))))

class Square(Shape):
    def __init__(self, name, length, width):
        super().__init__(name,length,width)

    def area(self,length):
        print("Area = ",int(length)**2)

    def perimeter(self, length):
        print("Perimeter = ",int(length)*4)

class Rectangle(Shape):
    def __init__(self,name,length,width):
        super().__init__(name,length,width)

class Circle(Shape):
    def __init__(self,name,radius):
        super().__init(name)
        self.radius = radius
    
    def area(self,radius):
        print("Area = ",(int(radius)**2)*3.14)

    def perimeter(self, radius):
        print("Perimeter = ",(int(radius)*2)*3.14)

class Triangle(Shape):
    def __init__(self,name,l1,l2,l3,angle):
        super().__init__(name)
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.angle = angle

    def area(self,l1,l2,angle):
        print("Area = ", 0.5*l1*l2*math.sin(angle))
    
    def perimeter(self, l1,l2,l3):
        print("Perimeter = ", l1+l2+l3)

square1 = Square("Square1",5)


