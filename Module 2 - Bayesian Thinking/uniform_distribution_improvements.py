def probability_range_improved(low_range, high_range, minimum, maximum):
    
    # TODO: check if any of the inputs are strings.
    # hint: the python function isinstance() will be useful
    if (isinstance(low_range, str) or isinstance(high_range, str) or isinstance(minimum, str) or isinstance(maximum, str)):
        # print a message to the user and return none
        print('Inputs should be numbers not string')
        return None
    
    # TODO check that low_range is between minimum and maximum
    if (low_range >= maximum or low_range <= minimum):
        # print a message to the user and return none
        print('Your low range value must be between minimum and maximum')
        return None
        
    # check that high_range is between min and max
    if (high_range >= maximum or high_range <= minimum):
        # print a message to the user and return none
        print('The high range value must be between minimum and maximum')
        return None

    # TODO: calulate and return the probability 
    # even if low range is greater than high range
    probability = abs(high_range-low_range)/float(maximum-minimum)
    return probability