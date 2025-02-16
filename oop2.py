class animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    def eat(self):
        print(f"{self.name} is eating ")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(animal):
    pass

class Cat(animal):
    pass
class Mouse(animal):
    pass

dog=Dog("Kutta");
cat=Cat("Tom")
mouse=Mouse("Jerry")
print(mouse.name)
print(mouse.is_alive)
mouse.eat();
mouse.sleep();
    