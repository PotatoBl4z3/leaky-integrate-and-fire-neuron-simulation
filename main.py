import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# # Variables used in the equation
# V - Membrane Potential of the neuron (initialized to 0)
# V_rec - Array that consists of the membrane potential after each time step
# spikes - Array that consists of the time stamps at which the neuron spiked
# I - Array of input current values at every time step with length of the number of steps
# TAU - The Time Constant
# dt - The time step (the difference between each time stamp we are testing)
# threshold - The threshold that, if the membrane potential reaches, resets the membrane potential to 0


# Function that runs the simulation
def LIF(I, TAU=10, dt=0.1, threshold=1.0, reset=0.0, V_rest=0.5, rm=1):
    num_steps = len(I)
    V_rec = np.zeros(num_steps)
    V_rec[0] = V_rest
    spikes = []
    
    for i in range(num_steps - 1):
        # Differential equation: dV/dt = (-(V - V_rest) + R*I) / Tau
        dV = (-(V_rec[i] - V_rest) + (rm * I[i])) / TAU
        V_rec[i+1] = V_rec[i] + dt * dV 
        
        # Spiking logic
        if V_rec[i+1] >= threshold:
            spikes.append((i+1) * dt) # Record time of spike
            V_rec[i+1] = reset        # Reset voltage
            
    return V_rec, np.array(spikes)


# Main Function
dt = 0.1
TAU = 10
current_Amplitude = 3.0
duration = 100

# Generate the initial time and current arrays
T = np.arange(0, duration, dt)
I = current_Amplitude * np.sin(2 * np.pi * 10 * T)**2

# Setup Plot
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(left=0.1, bottom=0.35) # Make room for sliders at bottom

V_rec, spikes = LIF(I=I, TAU=10, dt=dt)

# Plot the voltage line
line_v, = ax.plot(T, V_rec, label='Membrane Potential (V)', color='blue')

# Plot spikes (we use a collection of vertical lines for efficiency)
# vlines returns a LineCollection, which is easier to remove/update than individual lines
spike_lines = ax.vlines(spikes, ymin=0, ymax=1.2, colors='red', linestyles=':', label='Spikes')

ax.set_xlabel('Time (ms)')
ax.set_ylabel('Voltage (V)')
ax.set_title('LIF Neuron Simulation')
ax.set_ylim(-0.2, 1.5) # Fixed Y-limit so graph doesn't jump around
ax.legend(loc='upper right')

# Add Sliders
# Define axes for sliders [left, bottom, width, height]
ax_dt  = plt.axes([0.20, 0.20, 0.65, 0.03]) # Adjusted left margin slightly for longer labels
ax_tau = plt.axes([0.20, 0.15, 0.65, 0.03])
ax_I   = plt.axes([0.20, 0.10, 0.65, 0.03])

s_dt = Slider(
    ax=ax_dt, 
    label=r'Time Step $dt$ [ms]', 
    valmin=0.01, 
    valmax=1.0, 
    valinit=dt
)

s_tau = Slider(
    ax=ax_tau, 
    label=r'Time Constant $\tau$ [ms]', 
    valmin=1.0, 
    valmax=50.0, 
    valinit=TAU
)

s_I = Slider(
    ax=ax_I, 
    label=r'Input Current $I$ [A]', 
    valmin=0.0, 
    valmax=10.0, 
    valinit=current_Amplitude
)

# Add Reset Button
# Create an axis for the button (bottom right corner)
reset_ax = plt.axes([0.8, 0.025, 0.1, 0.04]) 

# Create the button object
button = Button(reset_ax, 'Reset', color='white', hovercolor='0.9')

# Define the reset function
def reset_sliders(event):
    s_dt.reset()
    s_tau.reset()
    s_I.reset()

# Connect the button to the function
button.on_clicked(reset_sliders)

# Update Function
def update(val):
    # Get current values from sliders
    current_dt = s_dt.val
    current_tau = s_tau.val
    current_amp = s_I.val
    
    # Re-generate time and input current based on new dt/Amp
    # Note: We have to regenerate 't' because changing dt changes the array length
    new_t = np.arange(0, duration, current_dt)
    new_I = current_amp * np.sin(2 * np.pi * 0.05 * new_t)**2
    
    # Re-run Simulation
    new_V, new_spikes = LIF(new_I, TAU=current_tau, dt=current_dt)
    
    # Update the Voltage Line
    line_v.set_data(new_t, new_V) # Must update both X (time) and Y (voltage)
    
    # Update Spikes
    global spike_lines
    spike_lines.remove() # Remove old spikes
    spike_lines = ax.vlines(new_spikes, ymin=0, ymax=1.2, colors='red', linestyles=':')
    
    # Redraw
    fig.canvas.draw_idle()


# Connect sliders to update function
s_dt.on_changed(update)
s_tau.on_changed(update)
s_I.on_changed(update)

plt.show()