# Given three input probabilities, complete this function
# so that it returns the posterior probability

def bayes(p_A, p_B_given_A, p_notB_given_notA):
    
    ## TODO: Calculate the posterior probability
    ## and change this value
    numerator = p_B_given_A * p_A
    p_notB_given_A = 1-p_notB_given_notA
    p_notA = 1-p_A
    denominator =  numerator + (p_notA * p_notB_given_A)
    posterior = numerator/denominator
    
    return posterior


## TODO: Change these values, run your code with them, and use print 
## statements to see the output of your function and get feedback
p_A = 0.3
p_B_given_A = 0.7
p_notB_given_notA = 0.9

posterior = bayes(p_A, p_B_given_A, p_notB_given_notA)
print('Your function returned that the posterior is: ' + str(posterior))