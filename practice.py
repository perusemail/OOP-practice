class Cat:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
    
    def make_sound(self):
        print("meow")

    def play(self, animal):
        print(self.name,"is playing with",animal.name)

    def fight(self, animal):
        print(self.name,"is fighting with",animal.name)

class Dog(Cat):
    def __init__(self,name,colour,breed):
        super().__init__(name, colour)
        self.breed = breed

    def make_sound(self):
        print("woof")
    
    def breed_type(self):
        print(self.name,"is a ",self.breed)

cat1 = Cat("john","black")
dog1 = Dog("Mike","brown","golden retriever")

cat1.fight(dog1)
dog1.breed_type()