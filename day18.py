'''opp's
----
--> object-oriented language (oop) is a style of programming where we model
real-world thing object as that contain both data and function()
-->reusable of code
-->and also scalable

class
-----
--> class is a blue-print or template that define wjat kind of data and behavior a certain type of
object will have

object
-----
--> this is Instance of class or an object ios a real instance created from a class . it is the actual
 thing that exists in memory while the program is running.
 
 Attributes
 ---------
 -->these are variable that store data related to a class or object'''


class car:
    def __init__(self, brand, color):
        self.brand =  brand
        self.color = color
car_1 = car("honda","red")
car_2 = car("i20","white")
print(car_1.brand)












