import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2020)

# Simulated number of stellar events observed by each observatory per year
hubble_events = np.array([102, 110, 115, 123, 131, 140, 145, 150, 160, 165])
chandra_events = np.array([95, 100, 103, 110, 117, 124, 130, 135, 140, 148])
spitzer_events = np.array([88, 92, 98, 105, 112, 120, 125, 130, 137, 145])

# Error associated with each observatory's observations
hubble_errors = np.array([5, 5, 6, 7, 7, 8, 8, 9, 9, 10])
chandra_errors = np.array([6, 6, 6, 7, 7, 8, 8, 8, 9, 10])
spitzer_errors = np.array([7, 7, 7, 8, 8, 9, 9, 9, 10, 11])

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each line with error bars
ax.errorbar(years, hubble_events, yerr=hubble_errors, label='Hubble Observatory',
            fmt='-o', capsize=5, color='blue', alpha=0.8)
ax.errorbar(years, chandra_events, yerr=chandra_errors, label='Chandra Observatory',
            fmt='-s', capsize=5, color='green', alpha=0.8)
ax.errorbar(years, spitzer_events, yerr=spitzer_errors, label='Spitzer Observatory',
            fmt='-^', capsize=5, color='orange', alpha=0.8)

# Customizing the plot
ax.set_title('Annual Stellar Observations by Leading Space Observatories\n(2010-2019)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Observable Stellar Events', fontsize=14)
ax.legend(title='Space Observatory', fontsize=10, loc='upper left')
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Setting x-ticks and labels
ax.set_xticks(years)
ax.set_xticklabels([str(year) for year in years], fontsize=12)

# Set the range for the y-axis
ax.set_ylim(80, 180)

# Adjust layout for better presentation
plt.tight_layout()

# Show the plot
plt.show()