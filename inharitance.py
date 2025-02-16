class Animal:
    def __init__(self,name):
        self.name=name
    def sleep(self):
        print(f"{self.name} is Sleeping!")
    def eat(self):
        print(f"{self.name} is  eating")
class prey(Animal):
    def flee(self):
        print(f"{self.name} is fleering !")
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is Hunting !")
class Rabbit(prey) :
    pass
class Hawk(Predator):
    pass
class Fish(prey,Predator):
    pass

rabbit=Rabbit("Bugs")
hawk=Hawk("Tony")
fish=Fish("Nemo")
rabbit.eat()
fish.flee()

