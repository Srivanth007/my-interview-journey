# Parent Class
class Animal:
    def eat(self):
        print("I am eating yum yum!")

# Child Class
class Cat(Animal): # Cat gets the eat() method for free!
    def meow(self):
        print("Meow!")

kitty = Cat()
kitty.eat() # Inherited from Animal!
kitty.meow() # Kitty's own special trick