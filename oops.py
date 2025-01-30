#######   OOPS    ######
#Class
#Object
#Inheritance
#Polymorphism
#Encapsulation
#Abstraction






#### Object 2 characteristics
#1. Attributes--name, age, color
#2. Behavior--singing, dancing,calling, browsing, 

#### CLASS--- Blueprint for the object 
#syntax
#class classname():
    #class body


class first1():
    name = "Program" #attributes
    loc = "NYC" #attributes
    def test(self): #method
        print("This is test method")
        print(self.name)
    def details(self):
        print("This is details method")
        print(self.loc)

obj = first1() ##instatiation- object creation, until no memory allocated.
print(obj.name)
print(obj.loc)
obj.test()
obj.details


class mobiles():
    brand_name = "Samsung"
    color = "White"
    storage = "128 GB"
    def calling(self, brand):
        print("you are calling...",brand)
    def camera(self):
        print("capturing photo...")
    def browsing(self):
        print("you are browsing...")
        self.calling("Vivo")


samsung = mobiles()
samsung.calling("samsung")
samsung.browsing()
samsung.camera()
apple = mobiles()
apple.calling("Apple")
oppo = mobiles()
oppo.calling("oppo")


### __init__ Method  #####
#special function, defined by "__"
#used to initialize objects
#SYNTAX
#def __init__(attr1,attr2,...):
#    attr1 = attr1     

class car():
    def __init__(self, b_name, color, model):
        self.brand = b_name
        self.b_color = color
        self.b_model = model
    def driving(self):
        print(f"You are driving {self.brand} {self.b_color} {self.b_model} car")
    def engine(self):
        print("start/off")
    
tata = car("TATA","Black",2024)
tata.driving()





