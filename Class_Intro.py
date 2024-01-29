"""Classes_Objects"""

""" Python is object-oriented programming, same as C++, JAVA, e.g.,,
    - OOP is easy to be reused, saves computing storage
    - class is the blue print, and the objects are the realizations (instances) of the class
    - class defines the data attributes (variable) and procedures (methods) of the objects
"""

#Demo example
class Customer: # creating a class for customer (the name we created for this class)
    pass #creating an empty class with pass statement

def cust_instance():
    cust = Customer() #empty class can still be instantiated, instance_name = Customer()
    return cust

cust_instance()
#Creating the Dog Class
class Dog: #Capitalized name for classes in Python
    
    def __init__(self, name, age): #Initializing name and age attributes for Dog.
        """ __init__ is an initializer method because it initializes the objects data; it is always executed when a class is created. 
        self parameter is REQUIRED as the first argument in each member method in the class. 
        self is a stand-in for object reference.
        """
        self.name = name  
        self.age = age
        self.treats = "Dental Chews" #set a default value for an attribute

    def sit(self): 
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} is rolling over!")

    def update_treats(self, new_treat):
        self.treats = new_treat


def one_instance(): #Making an instance from a Class
    my_dog = Dog("Ollie", 4)  #self does not need an argument when it is called.
    print(f"My dog's name is {my_dog.name}")
    print(f"My dog's age is {my_dog.age}")
    """
    Notably, .treat doesn't exit in this instance, given update_treats() has not been called.
    """

def second_instance():
    dog_name = input("What's your dog's name?")
    dog_age = int(input("How old is your dog?")) 
    your_dog = Dog(dog_name, dog_age) #creating an instance of Dog class by calling the class
    your_dog.sit()#sit(), roll_over(), are optional actions that are related to a specific dog
    your_dog.roll_over()

#To update an attribute's default value, either through a method or direct assignment
def third_instance():
    my_dog = Dog("Ollie", 4)
    my_dog.update_treats("Apple") #through a method
    print(f"{my_dog.name} loves {my_dog.treats}")

""" Design Classes 
    - Class
    - Data Attributes - nouns
    - Methods - actions
    
In the Dog class case: 
    - Dog
    - Name, AGE
    - sit(), roll_over()
"""

# In-class exercises: 
"""
Make a class called Restaurant with two attributes, restaurant_name and cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of information,
and another method called open_restaurant() that prints a message indicating that the 
restaurant is open.

Make 3 instances of the class, print two attributes individually and then call the two methods.
"""

#creating class restaurant
class Restaurant:

    def __init__(self, name, cuisine_type):
        
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} makes {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is open!")

def instance_one():
    first_restaurant = Restaurant("Bartaco", "Mexican")
    print(f"{first_restaurant.name}")
    print(f"{first_restaurant.cuisine_type}")
  

def instance_two():
    second_restaurant = Restaurant("Koto", "Sushi")
    second_restaurant.describe_restaurant()
    second_restaurant.open_restaurant()

def instace_three():
    third_restaurant = Restaurant("Fresh Kitchen", "American")

instance_one()
instance_two()