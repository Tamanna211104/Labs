import numpy as np
import matplotlib.pyplot as plt

# Parameters
R = 100  # Resistance (ohms)
L = 0.1  # Inductance (Henry)
C = 0.001  # Capacitance (Farad)
V0 = 10   # Initial voltage (Volts)

# Time array
t = np.linspace(0, 2, 1000)

# Underdamped response
w0 = 1 / np.sqrt(L * C)
zeta_under = 0.2  # Damping ratio for underdamped
wd_under = w0 * np.sqrt(1 - zeta_under**2)
A_under = V0 / np.sqrt((1 - zeta_under**2)**2 + (2 * zeta_under)**2)
phi_under = np.arctan2(2 * zeta_under * w0, (1 - zeta_under**2))
v_under = A_under * np.exp(-zeta_under * w0 * t) * np.sin(wd_under * t + phi_under)

# Critically damped response
zeta_critical = 1  # Damping ratio for critically damped
wd_critical = w0
A_critical = V0
v_critical = (A_critical * t + V0) * np.exp(-w0 * t)

# Overdamped response
zeta_over = 5  # Damping ratio for overdamped
wd_over = w0 * np.sqrt(zeta_over**2 - 1)
A_over = V0 / (zeta_over * np.sqrt(zeta_over**2 - 1))
v_over = A_over * (np.exp((-zeta_over + np.sqrt(zeta_over**2 - 1)) * w0 * t) - np.exp((-zeta_over - np.sqrt(zeta_over**2 - 1)) * w0 * t))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, v_under, label='Underdamped')
plt.plot(t, v_critical, label='Critically Damped')
plt.plot(t, v_over, label='Overdamped')
plt.title('RLC Circuit Response')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)
plt.show()
