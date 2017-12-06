# The current predict state function
def predict_state_mtx(state, dt):
    ## TODO: Assume that the state passed in is a Matrix object
    ## Using a constant velocity model and a transformation matrix
    ## Create and return the new, predicted state!
    predicted_state = state * matrix.Matrix([[dt]])
    
    return predicted_state