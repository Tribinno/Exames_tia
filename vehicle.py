Vehicle class:
	def __init__(self, brand, year):
		self.brand = brand
		self.year = year

	def display_info(self):
		print(f"Brand: {self.brand}, Year: {self.year}")


vehicle_one = Vehicle("Toyota", 2020)
vehicle_two = Vehicle("Ford", 2023)

vehicle_one.display_info()
vehicle_two.display_info()


from vehicle import Vehicle


class VehicleYear(Vehicle):
	def display_year_info(self):
		if self.year >= 2020:
			condition="new"
		else:
			condition="old"

		print(f"{self.brand} ({self.year}) is an {condition} vehicle.")


vehicle_one = VehicleYear("Honda", 2018)
vehicle_two = VehicleYear("Tesla", 2024)

vehicle_one.display_year_info()
vehicle_two.display_year_info()

from vehicle import Vehicle


class VehicleBrand(Vehicle):
	def display_brand_info(self):
		print(f"This vehicle is a {self.brand} from {self.year}.")


vehicle_one = VehicleBrand("Toyota", 2020)
vehicle_two = VehicleBrand("Ford", 2023)

vehicle_one.display_brand_info()
vehicle_two.display_brand_info()
