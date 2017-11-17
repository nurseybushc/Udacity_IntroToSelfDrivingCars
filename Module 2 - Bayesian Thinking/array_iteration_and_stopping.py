# This function takes in the road and determines where to stop
def find_stop_index(road):
    ## TODO: Iterate through the road array
    ## TODO: Check if a stop sign ('s') is found in the array
    ## If one is, break out of your iteration
    ## and return the value of the index that is *right before* the stop sign
    ## Change the stop_index value
    stop_index = 0

    for item in road:
        if item == 's':
            break
        else:
            stop_index+=1
    
    return stop_index -1
