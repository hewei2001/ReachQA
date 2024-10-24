import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2026)

# Synthetic data for EV adoption in different regions
# Data reflects cumulative percentage of vehicles that are electric
region_a = [2, 3, 5, 8, 12, 18, 25, 35, 45, 60, 70, 80, 88, 92, 95, 97]
region_b = [1, 2, 3, 5, 10, 16, 24, 33, 44, 57, 68, 75, 82, 88, 90, 93]
region_c = [0, 1, 2, 4, 6, 10, 14, 20, 28, 37, 48, 58, 70, 80, 87, 90]
region_d = [3, 5, 7, 9, 15, 22, 30, 40, 50, 62, 72, 82, 90, 94, 96, 98]
region_e = [1, 2, 4, 6, 9, 12, 18, 27, 39, 50, 64, 76, 84, 89, 92, 95]

# Create a figure and axis
plt.figure(figsize=(12, 7))

# Plot the area chart using fill_between to fill areas
plt.fill_between(years, 0, region_a, label='Region A', color='#ff9999', alpha=0.6)
plt.fill_between(years, region_a, np.array(region_a) + np.array(region_b), label='Region B', color='#66b3ff', alpha=0.6)
plt.fill_between(years, np.array(region_a) + np.array(region_b), np.array(region_a) + np.array(region_b) + np.array(region_c), 
                 label='Region C', color='#99ff99', alpha=0.6)
plt.fill_between(years, np.array(region_a) + np.array(region_b) + np.array(region_c), 
                 np.array(region_a) + np.array(region_b) + np.array(region_c) + np.array(region_d), 
                 label='Region D', color='#ffcc99', alpha=0.6)
plt.fill_between(years, np.array(region_a) + np.array(region_b) + np.array(region_c) + np.array(region_d), 
                 np.array(region_a) + np.array(region_b) + np.array(region_c) + np.array(region_d) + np.array(region_e), 
                 label='Region E', color='#c2c2f0', alpha=0.6)

# Add title and labels
plt.title("Electric Vehicle Adoption Trends\nAcross Various Regions (2010-2025)", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Cumulative % of Electric Vehicles", fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(years, rotation=45)

# Add a legend with appropriate title
plt.legend(title="Regions", loc='upper left', fontsize=10)

# Show grid for better readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()