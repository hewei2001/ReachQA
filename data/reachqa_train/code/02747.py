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

# Initialize plot
plt.figure(figsize=(12, 8))

# Plot scatter points for each model
plt.scatter(weeks, alpha_speeds, color='red', label='Alpha Model', zorder=5)
plt.scatter(weeks, beta_speeds, color='green', label='Beta Model', zorder=5)
plt.scatter(weeks, gamma_speeds, color='blue', label='Gamma Model', zorder=5)

# Plot smooth fitting curves for each model
plt.plot(xnew, alpha_smooth, color='red', linestyle='--', linewidth=2, alpha=0.7)
plt.plot(xnew, beta_smooth, color='green', linestyle='--', linewidth=2, alpha=0.7)
plt.plot(xnew, gamma_smooth, color='blue', linestyle='--', linewidth=2, alpha=0.7)

# Chart title and labels
plt.title('Trend in Autonomous Vehicle Acceleration:\nEvaluating Speed Over Time for Diverse Models', fontsize=16, fontweight='bold')
plt.xlabel('Weeks', fontsize=12)
plt.ylabel('Speed (kph)', fontsize=12)

# Add a legend to differentiate the data points
plt.legend(title='Vehicle Models', loc='upper left')

# Enable grid for better readability
plt.grid(visible=True, linestyle='--', alpha=0.7)

# Automatically adjust the plot layout
plt.tight_layout()

# Display the plot
plt.show()