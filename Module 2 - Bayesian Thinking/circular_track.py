from Car import Car
import time

def circle(car):
    car.steer(5)
    car.gas(0.50)
    
car = Car()

circle(car)