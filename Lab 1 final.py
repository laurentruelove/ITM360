import random

class Pet:
    cleanliness_max = 10
    food_reduce = 2
    food_max = 10
    food_warning = 3
    boredom_reduce = 2
    boredom_max = 10
    sounds = ['Tomagotchi!', 'Grrr...']

    def __init__(self, name):
        self.name = name
        self.hygiene = random.randrange(0, self.cleanliness_max + 1)
        self.food = random.randrange(0, self.food_max + 1)
        self.boredom = random.randrange(0, self.boredom_max + 1)
        self.sounds = self.sounds[:]  

    def bathe(self):
        if self.hygiene <= (self.cleanliness_max) - 3:
            self.hygiene += 3
        else:
            self.hygiene = 10
            print("Pet is annoyed given the unnecessary bathe")

    def clock_tick(self):
        self.boredom = min(self.boredom + 1, self.boredom_max)
        self.food = max(self.food - 1, 0)

    def teach(self):
        self.sounds.append('Hello')
        self.reduce_boredom()

    def greet(self):
        print(random.choice(self.sounds))
        self.reduce_boredom()

    def reduce_boredom(self):
        self.boredom = max(self.boredom - self.boredom_reduce, 0)

    def feed(self):
        meal = random.randint(0, min(self.food, self.food_max))
        self.food = min(self.food + meal, self.food_max)

    def mood(self):
        if self.food >= self.food_warning and self.boredom <= self.boredom_max:
            return "Happy"
        elif self.food < self.food_warning:
            return "Hungry"
        else:
            return "Bored"

    def __str__(self):
        return f"{self.name} is {self.mood()}"

class Cat(Pet):
    sounds = ["Meow", 'Grrr...']

    def rat(self): 
        chase = input("Is Cat chasing a rat?: ").lower()
        if chase == "yes":
            print("The cat is chasing a rat!")
        else:
            print("The cat is not chasing a rat!")

    def mood(self):
        if self.food >= self.food_warning and 0 <= self.boredom < 3:
            return "Happy"
        elif self.boredom >= 3:
            return "{self.name} is Absolutely bored!"
        else:
            return "{self.name} is Feeling grumpy" if random.randint(0, 1) else "{self.name} isRandomly annoyed"
        
class Fish(Pet):
    def __init__(self, name, water_type): #added water type for its unique attribute
        super().__init__(name)
        self.water_type = water_type 

    def swim(self): #swin is the unique method as only fish can swim.
        print(f"{self.name} is swimming fast!")


def instance_one():
    Tomagotchi = Pet("Harry")
    print(Tomagotchi)
    Tomagotchi.greet()
    Tomagotchi.clock_tick()

def cat_instance():
    cat = Cat("meredith")
    cat.rat()
    print(cat.mood()) # -1, Given the returned object is already a string in the mood() function, print() will return a none {self.name} in the output.

def fish_instance():
    fishy = Fish("Blue", "Fresh Water")
    fishy.swim()

instance_one()
cat_instance()
fish_instance()
