import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Electric vehicle adoption data (in thousands) over the years for each category
solar_ev = np.array([5, 10, 20, 40, 80, 150, 230, 300, 380, 460, 550])
wind_ev = np.array([3, 6, 13, 30, 65, 130, 210, 280, 360, 420, 500])
hydropower_ev = np.array([2, 5, 12, 25, 50, 100, 170, 240, 310, 370, 430])
biofuel_ev = np.array([1, 4, 9, 20, 45, 95, 160, 220, 290, 340, 400])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Stack the areas for each category with distinct colors
ax.stackplot(years, solar_ev, wind_ev, hydropower_ev, biofuel_ev,
             labels=['Solar', 'Wind', 'Hydropower', 'Biofuel'],
             colors=['#f39c12', '#3498db', '#2ecc71', '#9b59b6'], alpha=0.8)

# Titles and labels
ax.set_title("Rise of Electric Vehicles:\nA Decade of Market Growth in Renewable Adoption (2010-2020)",
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of EVs (in thousands)", fontsize=12)

# Customize x-ticks and y-ticks for better readability
plt.xticks(years, fontsize=10, rotation=45)
plt.yticks(fontsize=10)

# Add gridlines to enhance readability
ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

# Add a legend to differentiate energy sources
ax.legend(loc='upper left', fontsize=10, title="Energy Sources")

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()