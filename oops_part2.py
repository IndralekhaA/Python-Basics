###########          INHERITANCE              ###########
'''
__main__ is the name of the environment where top-level code is run. 
“Top-level code” is the first user-specified Python module that starts running. 
It’s “top-level” because it imports all other modules that the program needs. 
Sometimes “top-level code” is called an entry point to the application.


This is where using the if __name__ == '__main__' code block comes in handy.
Code within this block won’t run unless the module is executed in the top-level environment.
'''

print(__name__)#the top-level module's __name__ set to __main__


#SYNTAX of Single Inheritance
#class DerivedClassName(BaseClassName):
    # <statement-1>
    # .
    # .
    # .
    # <statement-N>
#class DerivedClassName(modname.BaseClassName):## when the base class is defined in another module

class father:
    def __init__(self,name):
        self.name = name
    def test(self):
        print("this is base class method")

class child(father):
    def __init__(self,name):
        self.name = name
        super().__init__("India")
    def test2(self):
        print("This is derived class method")
    
obj = child("Indu")
obj.test()
obj.test2()
print(obj.name)

class Gfather:
    def __init__(self):
        pass
    def method1(self):
        print("this is base class method")
    def test1(self):
        print("This is test1 method")

class father(Gfather):
    def __init__(self):
        super().__init__()
    def method2(self,"father"):
        print("this is 1st derived class method",{})
        super().test1()

class child(father):
    def __init__(self, name):
        self.myname = name
        super().__init__()
    def method3(self):
        print(f" My name is {self.myname}")

obj = child("Indulekha")
print(obj.myname)
obj.method1()
obj.method2()
obj.method3()














