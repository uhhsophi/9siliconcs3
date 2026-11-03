class Animal:
  def __init__(self, name: str):
    self.name = name

  def make_sound(self):
    pass
  def eat(self):
    pass
  def feed(self):
    return self.eat()
    
class Lion(Animal):
  def make_sound(self):
    return f"{self.name} roars loudly!"
  def eat(self):
    return f"{self.name} eats fresh meat."

class Elephant(Animal):
  def make_sound(self):
    return f"{self.name} trumpets!"
  def eat(self):
    return f"{self.name} eats grass and fruits."

class Monkey(Animal):
  def make_sound(self):
    return f"{self.name} chatters!"
  def eat(self):
    return f"{self.name} eats bananas."

#Test Driver Code
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.feed())
print("-----")

print(elephant.make_sound())
print(elephant.feed())
print("-----")

print(monkey.make_sound())
print(monkey.feed())
print("-----")
