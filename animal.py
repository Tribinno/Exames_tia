class Animal:
	def __init__(self, name, sound):
		self.name = name
		self.sound = sound

	def make_sound(self):
		print(f"{self.name} says: {self.sound}")


dog = Dog("Buddy", "Woof!")
cat = Cat("Mittens", "Meow!")

dog.make_sound()
cat.make_sound()

class Dog(Animal):
	def make_sound(self):
		print(f"{self.name} says: Woof!")


class Cat(Animal):
	def make_sound(self):
		print(f"{self.name} says: Meow!")
