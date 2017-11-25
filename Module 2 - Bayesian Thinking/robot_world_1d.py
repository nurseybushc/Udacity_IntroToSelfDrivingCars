#1
import matplotlib.pyplot as plt
import numpy as np

def initialize_robot(grid_size):
    grid = []
    
    for i in range(0, grid_size -1):
    
        grid.append(1/grid_size)
    # TODO: for each space on the map grid, store the initial probability
    # in the grid list. For example, if there are eight spaces on the grid,
    # the grid list should have eight entries where each entry represents
    # the initial probability of the robot being in that space.
    
    return grid

#2
def grid_probability(grid, position):
    
    ##### 
    # TODO: Use an if statement to make sure that the position input
    # does not go beyond the size of the list. Say the list has five elements
    # and your code tries to access grid[5] or grid[6]. That will lead to an 
    # error.If the position input is legitimate, then return the probability
    # stored at that position. If the position input is not legitimate, then
    # return None
    #####
    returnVal = None
    if position < len(grid):
        returnVal = grid[position]
    
    return returnVal

#3
import matplotlib.pyplot as plt
import numpy as np

def output_map(grid):
    
    ###
    # TODO: make a bar chart to plot the probability at each point on the grid.
    # Start by creating a list in the variable x_labels to represent each grid point.
    # For example, if the grid variable has length 5, x_labels would contain
    # a list [0, 1, 2, 3, 4].
    ###
    
    x_labels = range(len(grid))
    plt.bar(x_labels, grid, width=0.7, edgecolor='black')
    ###
    # TODO: output a bar chart of the results. Use
    # plt.bar(x_data, y_data, width=0.7, edgecolor='black') and change
    # x_data and y_data to the appropriate variable names
    # Remember that the grid has the probability values you will need
    
    # Once you have coded plt.bar() correctly, the rest of this code
    # will put axis labels and titles on your visualization.
    plt.xlabel('Grid Space')
    plt.ylabel('Probability')
    plt.title('Probability of the robot being at each space on the grid')
    plt.xticks(np.arange(min(x_labels), max(x_labels)+1, 1))
    plt.show()

#4
def update_probabilities(grid, updates):
    
    
    ###
    # TODO: write a for loop that goes through the updates list and updates
    # the probabilities in the grid variable
    ###
    #print(updates)
    #print(grid)
    #print(len(grid))
    #print(len(updates))
    for i in range(0,len(updates)):
        #print(i)
        #print(gridupdates[i][0])
        grid[updates[i][0]] = updates[i][1]
        ### TODO: update the probabilities inside the grid list
    return grid