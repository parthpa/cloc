class Car(object):
  # test
  #test
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg

  def display_car(self):
    return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)
  
  def drive_car(self):
    self.condition = "used"
  
  def mileage(self):
    return self.mpg

class ElectricCar(Car):
  def __init__(self, battery_type,model,color,mpg):
    self.battery_type = battery_type
    self.model = model
    self.color = color
    self.mpg = mpg
  
  def drive_car(self):
    self.condition = "like new"

class GasCar(Car):
  def __init__(self, gas_type, model, color, mpg):
    self.gas_type = gas_type
    self.model = model
    self.color = color
    self.mpg = mpg
  
  def drive_car(self):
    self.condition = "Need an oil change"

def initialize_car(engine_type,model,color,mpg):
  if engine_type == "G":
    this_car = GasCar("Petrol",model,color,mpg)
  else:
    this_car = ElectricCar("Electric",model,color,mpg)
  return this_car

print "****If you own two cars, this program tells you which car you should drive for a given trip****"
trip = raw_input("Enter the number of miles you will be driving for this trip: ")
print "Enter information about your first car:"
engine_type = raw_input("Enter car type (G-Gasoline, B-Battery): ")
model = raw_input("Enter the model of your car: ")
color = raw_input("Enter the color of your car: ")
mpg = raw_input("Enter mileage of your car: ")

my_car = initialize_car(engine_type,model,color,mpg)

print "Enter information about your second car:"
engine_type = raw_input("Enter car type (G-Gasoline, B-Battery): ")
model = raw_input("Enter the model of your car: ")
color = raw_input("Enter the color of your car: ")
mpg = raw_input("Enter mileage of your car: ")

my_car2 = initialize_car(engine_type,model,color,mpg)

print my_car.mileage()
print my_car2.mileage()

