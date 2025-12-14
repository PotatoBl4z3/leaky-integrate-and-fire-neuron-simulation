# Leaky Integrate-and-Fire (LIF) Neuron Simulation

This project simulates the dynamics of a Leaky Integrate-and-Fire (LIF) neuron. It implements the differential equation governing membrane potential changes over time, approximates the solution using Euler's method, and visualizes the neuron's spiking behavior given an input current.

## The Mathematical Model

The core of the simulation is based on the linear differential equation for a passive membrane:

$$\tau_m \frac{dV}{dt} = -(V(t) - V_{rest}) + R_m I(t)$$

Where:

  * $V(t)$ is the membrane potential at time $t$.
  * $V_{rest}$ is the resting potential.
  * $\tau_m$ (Tau) is the membrane time constant.
  * $R_m$ is the membrane resistance.
  * $I(t)$ is the input current.

### Spiking Logic

The "Fire" mechanism is implemented as a discrete check after every time step:

1.  **Integration:** The membrane potential $V$ accumulates based on the input current $I$.
2.  **Leak:** The potential decays towards $V_{rest}$ over time (determined by $\tau_m$).
3.  **Fire:** If $V(t) > V_{threshold}$, the neuron records a spike.
4.  **Reset:** Immediately after spiking, $V(t)$ is reset to a defined reset value (typically $0$ or $V_{rest}$).

## Getting Started

### Prerequisites

You will need Python installed along with the following libraries:

```bash
pip install numpy matplotlib
```

## Function Parameters

The `LIF` function accepts the following arguments:

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `I` | `array` | Required | Array of input current values for every time step. |
| `TAU` | `float` | `10` | The time constant ($\tau_m$) in ms. |
| `dt` | `float` | `0.1` | The simulation time step in ms. |
| `threshold`| `float` | `1.0` | The voltage threshold to trigger a spike. |
| `reset` | `float` | `0.0` | The value $V$ resets to after a spike. |
| `V_rest` | `float` | `0.5` | The resting membrane potential. |
| `rm` | `float` | `1` | Membrane resistance ($R_m$). |
