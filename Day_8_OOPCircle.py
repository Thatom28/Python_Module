class Circle:
    pi = 3.14159 # Class variable

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return f'the area of the circle is {Circle.pi * self.radius **2}'
    
    @staticmethod
    def perimeter(num):

        return 2 * Circle.pi * num

    @classmethod
    def from_diameter(cls, diameter):
        diameter = diameter / 2
        return Circle(diameter)

    
circle1 = Circle(2)
 
print(circle1.calculate_area())
circle_from_dia = Circle.from_diameter(10)  
#you can only access fcalculate average because it is accessable from an instance of the class  
#This indicates that you need to return a class 
print(circle_from_dia.calculate_area())
print(Circle.perimeter(10))

#IINHERITANCE the methods in Animal are aveliable in dog and they can be ovverriden and not the other way around
class Animal:
    def __init__(self, name):
        self.name =  name

    def speak(self):
        return "some sound"
    
class Dog(Animal):

    #if you want the method to take in additional parameters Create a constructor
    def __init__(self, name, speed): 
        super().__init__(name) #pass the name to the constructor of animal
        self.speed = speed

    def run(self):
        return "🐶 wags tail!"
    #POLYMOPHISM: you can change the method
    def speak(self):
        return 'Woof'
    def speed_bonus(self):
        return f"Running at speed {self.speed}km/h"

toby = Animal("toby")
#maxxy = Dog("Maxxy") #wont work because missing arguments
maxxy = Dog("bobby", 20)
print(toby.speak())
print(maxxy.speak())
print(maxxy.run())
print(maxxy.speed_bonus())