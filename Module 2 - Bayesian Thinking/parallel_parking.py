# CODE CELL
#
# Write the park function so that it actually parks your vehicle.

from Car import Car
import time

def park(car):
    # TODO: Fix this function!
    #  currently it just drives back and forth
    #  Note that the allowed steering angles are
    #  between -25.0 and 25.0 degrees and the 
    #  allowed values for gas are between -1.0 and 1.0
    
    # back up for 3 seconds
    car.steer(20.0)
    car.gas(-0.4)
    time.sleep(3.5) # note how time.sleep works
    
     # back up for 3 seconds
    car.steer(-20.0)
    car.gas(-0.4)
    time.sleep(2.5) # note how time.sleep works
    
    # forward for 2 seconds
    car.steer(8.0)
    car.gas(0.25)
    time.sleep(2.0)
    
    #car.gas(-0.025)
    #time.sleep(0.1)

    # back again...
    car.gas(-0.1)
    time.sleep(1.5)
    
    car.gas(0)
    
    # forward...
    #car.gas(0.1)
    #time.sleep(1.0)

car = Car()
park(car)