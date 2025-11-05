# Steps to do:
# 0. Understand the equation (τm​dtdV​=−(V(t)−Vrest​)+Rm​I(t))!!! 
# 1. Figure out how to write the differential equation in python
# 2. Make it such that given a time (t), we can find all the other variables using the equation
# 3. Add the spiking logic to the code (whenever V goes above 1 we need to give a signal and then reset V to 0) <----- WE ARE HERE
# 4. Use Matplotlib to visualize the working using a range of data

# Sreevatsa's branch for writing code to simulate the LIF differential equation

import numpy as np
import matplotlib.pyplot as plt

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
    spikes = []
    
    for i in range(num_steps-1):
        V_rec[i+1] = V_rec[i] + dt*((I[i]-V_rec[i])/TAU) # From Euler's method of approximation
        
        if (V_rec[i+1] > threshold):
            spikes.append(i*dt)
            V_rec[i+1] = reset
    
    return V_rec, np.array(spikes) #I'm not sure about the "leaky" part of this equation as it immediately drops to 0 when it spikes


# There's also another equation used in the documentation for the project 
# (τm​dtdV​=−(V(t)−Vrest​)+Rm​I(t). Define the key parameters: membrane time constant (τm​), membrane resistance (Rm​), resting potential (Vrest​), and input current (I(t)).)
# I was wondering which equation to implement (the project description one seems more correct and it shouldn't be too hard to implement either one)

#Main Function (idk bro this is the testing ground)
dt = 0.1
T = np.arange(1000)*dt*1e-3
V_rec, spikes = LIF(3*np.sin(2*np.pi*10*T)**2, TAU=10, dt=dt)
plt.plot(np.arange(len(V_rec))*dt, V_rec, label='V')
for i, t in enumerate(spikes):
    plt.axvline(t, ls=':', c='r', lw=2, label='Spikes' if i==0 else None)
plt.xlabel('Time (ms)')
plt.ylabel('V')
plt.legend(loc='best')
plt.tight_layout()
plt.show()