import numpy as np
import matplotlib.pyplot as plt

# Define the years of the missions
years = np.arange(2025, 2040)

# Hypothetical data packets collected per mission (in thousands)
mission_alpha_data = np.array([5, 6, 7, 7.5, 8, 9, 10, 10.5, 11, 12, 12.5, 13, 14, 14.5, 15])
mission_beta_data = np.array([4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11])
mission_gamma_data = np.array([6, 7, 7.5, 8, 9, 9.5, 10, 11, 11.5, 12, 12.5, 13, 13.5, 14, 15])

# Errors in data retrieval due to cosmic interference (in thousands)
alpha_errors = np.array([0.5, 0.6, 0.7, 0.5, 0.8, 0.9, 1, 0.5, 1.1, 0.5, 1.2, 0.7, 0.5, 1.3, 0.6])
beta_errors = np.array([0.4, 0.5, 0.6, 0.4, 0.7, 0.5, 0.8, 0.7, 0.6, 0.5, 0.9, 0.8, 0.4, 1.1, 0.5])
gamma_errors = np.array([0.6, 0.5, 0.7, 0.6, 0.8, 0.9, 0.6, 0.5, 1.0, 0.9, 1.2, 1.1, 0.6, 1.3, 1.2])

# Setup the plot
plt.figure(figsize=(14, 8))

# Plot each mission's data with error bars
plt.errorbar(years, mission_alpha_data, yerr=alpha_errors, fmt='-o', label='Mission Alpha',
             capsize=5, linestyle='--', color='royalblue', alpha=0.8)
plt.errorbar(years, mission_beta_data, yerr=beta_errors, fmt='-s', label='Mission Beta',
             capsize=5, linestyle='-.', color='darkorange', alpha=0.8)
plt.errorbar(years, mission_gamma_data, yerr=gamma_errors, fmt='-d', label='Mission Gamma',
             capsize=5, linestyle='-', color='forestgreen', alpha=0.8)

# Titles and labels
plt.title("Celestial Age:\nTracking Satellite Data Collection Over Time", fontsize=16, fontweight='bold')
plt.xlabel("Mission Year", fontsize=12)
plt.ylabel("Data Packets Collected (thousands)", fontsize=12)

# Grid and Legend
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title='Satellite Missions', fontsize=10, loc='upper left')

# Ensure no elements are occluded
plt.tight_layout()

# Show the plot
plt.show()