import matplotlib.pyplot as plt
import numpy as np

def bar_heights(intervals, probabilities, total_probability):

    heights = []
    
    #TODO: sum the relative probabilities
    total_relative_prob = sum(probabilities)
    
    for i in range(0, len(probabilities)):
        
        #TODO: Looping through the probabilities list, 
        #      take one probability at a time and 
        #      calculate the area of each bar. Think about how you can 
        #      calculate the area of a bar knowing the total_probability,
        #      relative probability, and the sum of the relative probabilities
        x = intervals[i+1] - intervals[i]
        bar_area = total_probability * (probabilities[i]/ total_relative_prob)
        
        # TODO: Calculate the height of the bar and append the value to the
        # heights list.Remember that the area of each bar 
        # is the width of the bar times the height of the bar
        heights.append(bar_area/x)
        
    return heights