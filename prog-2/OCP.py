from abc import ABC , abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class triangle(shape):
    def __init__(self , base , height):
        self.base=base
        self.height=height
    def area (self):
        return (1/2 *self.base *self.height)
    
class circle(shape):
    def __init__(self ,radius):
        self.radius=radius
    def area (self):
        return (3.14 *self.radius**2) 

def display(shapes):
    for shape in shapes :
        print(f' Area is : {shape.area()}')
        
        
shapes=[triangle(5, 8), circle(6)]  
display(shapes)