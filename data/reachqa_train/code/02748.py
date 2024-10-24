import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define weeks (time) of the study
weeks = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Define speed data for each autonomous vehicle model
alpha_speeds = np.array([20, 22, 25, 28, 31, 35, 38, 40, 42, 45])
beta_speeds = np.array([18, 21, 23, 26, 30, 32, 35, 37, 39, 43])
gamma_speeds = np.array([15, 18, 20, 24, 27, 30, 33, 36, 38, 41])

# Create new time points for smooth line fitting
xnew = np.linspace(weeks.min(), weeks.max(), 300)

# Calculate smooth fitting lines using B-spline interpolation
alpha_smooth = make_interp_spline(weeks, alpha_speeds)(xnew)
beta_smooth = make_interp_spline(weeks, beta_speeds)(xnew)
gamma_smooth = make_interp_spline(weeks, gamma_speeds)(xnew)

# Calculate a derived quantity: acceleration (simplified example)
alpha_acceleration = np.gradient(alpha_speeds)
beta_acceleration = np.gradient(beta_speeds)
gamma_acceleration = np.gradient(gamma_speeds)

# Initialize plot
plt.figure(figsize=(14, 10))

# Plot scatter points and error bars for each model
plt.errorbar(weeks, alpha_speeds, yerr=1.5, fmt='o', color='red', label='Alpha Model', zorder=5)
plt.errorbar(weeks, beta_speeds, yerr=1.5, fmt='o', color='green', label='Beta Model', zorder=5)
plt.errorbar(weeks, gamma_speeds, yerr=1.5, fmt='o', color='blue', label='Gamma Model', zorder=5)

# Plot smooth fitting curves for each model with gradient color
plt.fill_between(xnew, alpha_smooth - 1.5, alpha_smooth + 1.5, color='red', alpha=0.1)
plt.fill_between(xnew, beta_smooth - 1.5, beta_smooth + 1.5, color='green', alpha=0.1)
plt.fill_between(xnew, gamma_smooth - 1.5, gamma_smooth + 1.5, color='blue', alpha=0.1)

plt.plot(xnew, alpha_smooth, color='red', linestyle='-', linewidth=2, alpha=0.8)
plt.plot(xnew, beta_smooth, color='green', linestyle='-', linewidth=2, alpha=0.8)
plt.plot(xnew, gamma_smooth, color='blue', linestyle='-', linewidth=2, alpha=0.8)

# Subplot for acceleration data
fig, ax1 = plt.subplots(figsize=(14, 10))

ax1.plot(weeks, alpha_acceleration, 'o--', color='darkred', label='Alpha Model Acceleration')
ax1.plot(weeks, beta_acceleration, 'o--', color='darkgreen', label='Beta Model Acceleration')
ax1.plot(weeks, gamma_acceleration, 'o--', color='darkblue', label='Gamma Model Acceleration')

ax1.set_title('Acceleration Analysis for Autonomous Vehicle Models', fontsize=14, fontweight='bold')
ax1.set_xlabel('Weeks', fontsize=12)
ax1.set_ylabel('Acceleration (kph/week)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(title='Vehicle Models Acceleration', loc='upper left')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()