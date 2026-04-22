'''polymorphism
--------------
--> this is allows a object of different classes to be as instance of the same base class, with method
behavimg differntly based on the acture object type
eg....
-----
print(len("python"))
print(len([1,2,3]))


method overloading
-----------------
--> this define multiple method with the same name but differnt perameters(numbers, type , or  order)
in the same class

class calculator:
    def sub(self, a, b=0, c=0):
        return a-b-c

cal = calculator()
print(cal.sub(5))
print(cal.sub(18,14))
print(cal.sub(15,17,18))

mthod overriding
----------------
--> this occure in the child class, redefining a parent class method with the same signature for return. 

class animal:
    def speak(self):
        return "sound"

class hen(animal):
    def speak(self):
      return "coco"

dog = hen()
print(hen.speak())


import pyttsx3
engine= pyttsx3.init()
class friend:
    def speak(self):
        return "sound"

class pavan(friend):
    def speak(self):
        return engine.say(" chetta na kodaka")

pavan = pavan()
print(pavan.speak())
engine.runAndWait()

operator overloading
------------------
--> this is customize operator like +, - for user-define classes by implementing special method..
eg..__add__, __sub__

class someone:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __add__(self, other):
        return someone(self.a +other.a, self.b + other.b)
    def __str__(self):
        return f"((self.a), (self.b))"

any = someone(2,3)
so = someone(5,9)
print(any + so)

data abstraction
----------------
--> this hides complex implementation, exposing only essential
features via abstract class or interface'''
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2

circle = circle(5)
print(circle.area())































































