

'''Encapsulation
---------------
--> the principle of bunding data(Attributes) and method that operate on that data into a singl unit,
which is a class

class BankAC:
    def __init__(self, balance):
        self.__balance = balance
    def deposite(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance

Acc = BankAC(20000)
Acc.deposite(8500)
print(Acc.get_balance())

inheritance
----------
--> this allow a child class(subclass) to acquire the attributes and method of a parent class
(Base class) this is called inheritance
1.single inheritence
------------------
--> Using single methodof the class from is single inheritence
2.mutiple

super()
--> this is used to call method of the parent class from the child class

class parent:
    def display(self):
        print("this is parent method")
class child(parent):
    def display(self):
        super().display()
        print("this is child method")
obj = child()
obj.display()

2.mutiple inheritence
super()
--> this is used to call method of the parent class from the child class'''

class father:
    def skill_1(self):
        print("father: hard working")
class mother:
    def skill_2(self):
        print("mother: cooking")
class child(father, mother):
    def all_skills(self):
        print("child: coding")
any = child()
any.skill_1()
any.skill_2()
any.all_skills()




















