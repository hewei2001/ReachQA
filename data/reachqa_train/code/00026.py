import matplotlib.pyplot as plt
import numpy as np

# Original Data for Scatter Plot
alpha_temp = [3200, 4500, 5000, 5300, 6000, 6700, 7200, 8500, 9100]
alpha_lum = [1.0, 2.3, 3.1, 3.5, 5.1, 5.8, 6.3, 7.9, 9.0]

beta_temp = [3100, 4000, 4900, 5200, 5500, 6200, 6800, 7400, 9000]
beta_lum = [0.9, 2.0, 2.9, 3.3, 4.6, 5.5, 6.0, 7.2, 8.7]

gamma_temp = [3500, 4700, 5100, 5400, 5800, 6300, 6900, 7800, 9200]
gamma_lum = [1.2, 2.5, 3.4, 3.9, 4.8, 5.9, 6.7, 7.5, 8.9]

# New Data for Line Plot (average luminosity over temperature ranges)
temperature_ranges = [3000, 4000, 5000, 6000, 7000, 8000, 9000]
average_lum_alpha = [1.2, 2.4, 3.0, 4.8, 6.2, 8.5]
average_lum_beta = [1.1, 2.3, 3.1, 4.2, 6.1, 8.0]
average_lum_gamma = [1.3, 2.6, 3.6, 4.9, 6.7, 8.8]

# Create a figure with two subplots (1x2 layout)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Scatter Plot
ax1.scatter(alpha_temp, alpha_lum, s=100, color='blue', marker='o', label='Cluster Alpha', alpha=0.7, edgecolor='black')
ax1.scatter(beta_temp, beta_lum, s=100, color='green', marker='^', label='Cluster Beta', alpha=0.7, edgecolor='black')
ax1.scatter(gamma_temp, gamma_lum, s=100, color='red', marker='s', label='Cluster Gamma', alpha=0.7, edgecolor='black')

ax1.set_title('Star Luminosity vs. Surface Temperature\nin Various Galactic Clusters', fontsize=14)
ax1.set_xlabel('Surface Temperature (Kelvin)', fontsize=12)
ax1.set_ylabel('Luminosity (Relative)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(title='Galactic Clusters', loc='upper left', fontsize=10)

# Line Plot
ax2.plot(temperature_ranges[:-1], average_lum_alpha, label='Average Luminosity Alpha', color='blue', marker='o')
ax2.plot(temperature_ranges[:-1], average_lum_beta, label='Average Luminosity Beta', color='green', marker='^')
ax2.plot(temperature_ranges[:-1], average_lum_gamma, label='Average Luminosity Gamma', color='red', marker='s')

ax2.set_title('Average Luminosity Trends\nAcross Temperature Ranges', fontsize=14)
ax2.set_xlabel('Temperature Range Start (Kelvin)', fontsize=12)
ax2.set_ylabel('Average Luminosity (Relative)', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(title='Galactic Clusters', loc='upper left', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()