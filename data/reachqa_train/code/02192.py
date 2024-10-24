import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2013, 2024)

# Percentage contributions of energy sources over the years (constructed)
fossil_fuels = np.array([70, 68, 65, 60, 55, 50, 45, 40, 35, 30, 25])
nuclear = np.array([15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15])
solar = np.array([2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20])
wind = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
hydro = np.array([10, 10, 11, 13, 15, 17, 19, 21, 23, 25, 27])

# Stack the data for plotting
energy_sources = np.vstack([fossil_fuels, nuclear, solar, wind, hydro])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, energy_sources, labels=['Fossil Fuels', 'Nuclear', 'Solar', 'Wind', 'Hydro'], colors=['#ffcc99', '#99ccff', '#ff9999', '#66b3ff', '#99ff99'], alpha=0.85)

# Set title and labels
ax.set_title("Energy Transition in Manufacturing:\nSectoral Contribution Over a Decade", fontsize=16, weight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Percentage Contribution", fontsize=12)

# Add grid and legend
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper left', title="Energy Sources", bbox_to_anchor=(1, 0.5))

# Adjust layout to prevent overlap and improve appearance
plt.xticks(years, rotation=45)
plt.tight_layout()

# Display the plot
plt.show()