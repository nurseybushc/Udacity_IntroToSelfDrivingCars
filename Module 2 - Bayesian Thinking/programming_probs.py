# The complement function takes in the probability of an event, P(A).
def complement(p_A):
    
    ## TODO: Change the value of complement
    ## So that it calculates the complement of any variable p_A
    complement = 1-p_A
    
    return complement

    
## TODO: Change this test value and test out your code!
p_test = 0.2

# Running your code with the p_test value
complement_test = complement(p_test)
print('Your function returned that the complement of '+str(p_test) +' is: '+str(complement_test))

## Complete this joint function
def joint(p_A, p_B):
    
    ## TODO: Change the value of joint_p
    ## so that it calculates the joint probability of 
    ## any variables p_A, p_B, WHEN THOSE PROBABILITIES
    ## ARE INDEPENDENT (this code wouldn't work 
    ## for probabilities that depend on each other).
    joint = p_A * p_B
    
    return joint

    
## TODO: Test out your code
## Define test probabilities and write print statements to test 
## the output of your function!
p_a_test = 0.2
p_b_test = 0.4
j = joint(p_a_test, p_b_test)

print('Your function returned that the joint probability is: '+str(j))