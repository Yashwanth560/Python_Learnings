<<<<<<< HEAD
class Animal:
    def __init__(self,a,b):
        self.height=a
        self.weight=b

    def display(self):
        print(self.height,self.weight)
    def speak(self):
        print("speak")

class Dog(Animal):
    def speak(self):
        print("Bow Bow!")

class Cat(Animal):
    def speak(self):
         super().speak()
         print("meow Meow!")

obj1=Cat(1,22)
obj2=Dog(3,35)
print(obj2.height)
obj1.display()
obj2.speak()
obj1.speak()



=======
class Animal:
    def __init__(self,a,b):
        self.height=a
        self.weight=b

    def display(self):
        print(self.height,self.weight)
    def speak(self):
        print("speak")

class Dog(Animal):
    def speak(self):
        print("Bow Bow!")

class Cat(Animal):
    def speak(self):
         super().speak()
         print("meow Meow!")

obj1=Cat(1,22)
obj2=Dog(3,35)
print(obj2.height)
obj1.display()
obj2.speak()
obj1.speak()



>>>>>>> 660398a33cdefc808b42d59417f38bdd65932db8
