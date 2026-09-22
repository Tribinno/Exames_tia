class Villain:
	def __init__(self, name, power, characteristics):
		self.name = name
		self.power = power
		self.characteristics = characteristics

	def show(self):
		print(self.name, self.power, self.characteristics)

	def use_power(self):
		print(self.name, "usa", self.power)


villain = Villain("Joker", "crear caos", "astuto y peligroso")
villain.show()
villain.use_power()
