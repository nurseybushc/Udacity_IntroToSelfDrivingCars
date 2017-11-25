import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np

def plot_uniform(x_minimum, x_maximum, tick_interval):
    
    x = range(x_minimum, x_maximum + 1)
    #print(x)
    area = 1
    
    y = area/(x_maximum-x_minimum)
    # TODO: Using x_maximum and x_minimum, calculate the height of the
    # rectangle that represents the uniform probability distribution
    # Recall that the rectangle area should be 1 for a uniform continuous
    # distribution 
    #y = 0
    
    plt.bar(x_minimum, y, bottom=0, width= (x_maximum - x_minimum), align='edge', alpha=0.5)
    plt.xlabel('Degrees')
    plt.ylabel('Probability Distribution')
    plt.title('Uniform Probability Distribution \n for a Spinning Bottle')
    plt.xticks(np.arange(min(x), max(x)+1, tick_interval))
    plt.show()