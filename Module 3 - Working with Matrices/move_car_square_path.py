
def turn_right(car):
    car.turn_left()
    car.turn_left()
    car.turn_left()

def move_x_spaces(car,x):
    for i in range(x):
        car.move()

## TODO: Make carla traverse a 4x4 square path
## Display the result
print('Carla\'s state is: ' + str(carla.state))
move_x_spaces(carla,2)
print('Carla\'s state is: ' + str(carla.state))
turn_right(carla)
print('Carla\'s state is: ' + str(carla.state))
move_x_spaces(carla,3)
print('Carla\'s state is: ' + str(carla.state))
turn_right(carla)
print('Carla\'s state is: ' + str(carla.state))
move_x_spaces(carla,3)
print('Carla\'s state is: ' + str(carla.state))
turn_right(carla)
print('Carla\'s state is: ' + str(carla.state))
move_x_spaces(carla,3)
print('Carla\'s state is: ' + str(carla.state))
carla.display_world()