## TODO: Create two cars of different colors and display their different worlds

initial_position2 = [3, 3] # [y, x] (top-left corner)
velocity2 = [0, 1] # [vy, vx] (moving to the right)

carla = car.Car(initial_position, velocity, world)
carlino = car.Car(initial_position2, velocity2, world, 'y')
carla.display_world()
carlino.display_world()