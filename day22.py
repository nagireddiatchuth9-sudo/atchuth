'''-level 
--------
--> This occure when a class inherits from a child class, create a grandparent--> parent--> child in this
structure.'''

class grandparent:
    def show_grandparent(self):
        print("I'm grandparent")

class parent(grandparent):
    def show_parent(self):
        print("I'm parent")

class child(parent):
    def show_child (self):
        print("I'm child")
'''
any = child()
any.show_grandparent()
any.show_parent()
any.show_child()


class mobile:
    def show_mobile_update(self):
        print("mobile")

class mobile_apps(mobile):
    def show_apps_update(self):
        print("apps")
        
any = mobile_apps()
any.show_mobile_update()
any.show_apps_update()
        
Hierchical
---------
--> This occure when multiple child classes inherit from a single parent class, this process is called
Hierchical


class parent:
    def parent_(self):
        print("I'm parent")

class child_1(parent):
    def child_(self):
        print ("I'm 1st child")

class child_2(parent):
    def _child(self):
        print("I'am 2nd child")

class child_3(child_1, child_2):
    def child(self):
        print("I'm the chaild")


any = child_3()
any.parent_()
any.child_()
any._child()
any.child()

Hybrid inheritance
------------------
--> this is a cimbination of two or maore type of inheritence, such as single muliple, multi- level,
 or hierachilcal all this in a single'''

class parent:
    def parent_(self):
        print("I'm parent")

class child_1(parent):
    def child_(self):
        print ("I'm 1st child")

class child_2(parent):
    def _child(self):
        print("I'am 2nd child")

class child_3(child_1, child_2, grandparent):
    def child(self):
        print("I'm inherited from grandparent class and_1 child_2")


any = child_3()
any.show_grandparent()
any.child_()
any._child()
any.child()






















    


















    
