# Steps to do:
# 0. Understand the equation (τm​dtdV​=−(V(t)−Vrest​)+Rm​I(t))!!! <----- WE ARE HERE
# 1. Figure out how to write the differential equation in python
# 2. Make it such that given a time (t), we can find all the other variables using the equation
# 3. Add the spiking logic to the code (whenever V goes above 1 we need to give a signal and then reset V to 0)
# 4. Use Matplotlib to visualize the working using a range of data

# Sreevatsa's branch for writing code to simulate the LIF differential equation

import numpy as np

# # Variables used in the equation
# V - Membrane Potential of the neuron (initialized to 0)
# V_rec - Array that consists of the membrane potential after each time step
# spikes - Array that consists of the time stamps at which the neuron spiked
# I - Array of input current values at every time step with length of the number of steps
# TAU - The Time Constant
# dt - The time step (the difference between each time stamp we are testing)
# threshold - The threshold that, if the membrane potential reaches, resets the membrane potential to 0


# Function that runs the simulation
# I: input current
# tau: time constant (in ms)
# threshold: threshold value to produce a spike
# reset: reset value after a spike
# dt: simulation time step in ms
def LIF (I, TAU=10, dt=0.1, threshold = 1.0, reset = 0.0):
    num_steps = len(I)
    V_rec = np.zeros(num_steps)
    spikes = np.array
    #Fill in the function
    return V_rec, spikes

print ("LIF")