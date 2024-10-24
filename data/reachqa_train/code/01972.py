import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define the years from 2025 to 2050
years = np.array([2025, 2030, 2035, 2040, 2045, 2050])

# Adoption rates (%) for futuristic transportation in Futurepolis
adoption_rates = np.array([10, 20, 35, 50, 70, 85])

# Average speed (km/h) associated with each adoption rate
average_speeds = np.array([15, 20, 28, 38, 50, 65])

# Define a function to model a smooth trend
def smooth_trend(x, a, b, c):
    return a * np.log(b * x) + c

# Fit the smooth trend line
params, _ = curve_fit(smooth_trend, adoption_rates, average_speeds)

# Create a smooth line for plotting
adoption_fit = np.linspace(5, 90, 400)
speed_fit = smooth_trend(adoption_fit, *params)

# Plotting
plt.figure(figsize=(12, 6))

# Scatter plot for actual data
plt.scatter(adoption_rates, average_speeds, color='darkblue', s=100, edgecolor='black', alpha=0.8, label='Observed Data')

# Smooth line fitting
plt.plot(adoption_fit, speed_fit, color='cyan', linestyle='--', linewidth=2.5, label='Smooth Trend')

# Adding titles and labels
plt.title("Trends in Futuristic Urban Transportation:\nThe Road to Tomorrow", fontsize=16, fontweight='bold')
plt.xlabel("Adoption Rate of Futuristic Vehicles (%)", fontsize=14)
plt.ylabel("Average Speed of Travel (km/h)", fontsize=14)

# Set axis limits to provide adequate space around points and line
plt.xlim(0, 100)
plt.ylim(10, 70)

# Legend
plt.legend(loc='upper left', fontsize=10, frameon=False)

# Grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Ensure layout is adjusted automatically to prevent overlapping of elements
plt.tight_layout()

# Show plot
plt.show()