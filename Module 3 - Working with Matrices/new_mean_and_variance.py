# Write a program to update your mean and variance
# when given the mean and variance of your belief
# and the mean and variance of your measurement.
# This program will update the parameters of your
# belief function.
import math
def update(mean1, var1, mean2, var2):
    
    if var1 == var2:
        new_mean = (mean1+mean2+0.0)/2
    else:
        left = 1.0/(var1+var2)
        right = var2*mean1 + var1*mean2
        #print str(left) + " " + str(right)
        new_mean = left * right
    
    new_var = 1.0 / ((1.0/var1) + (1.0/var2))
    return [new_mean, new_var]

print update(10.,8.,13., 2.)