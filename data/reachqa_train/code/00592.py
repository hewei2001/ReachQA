import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Renewable energy consumption (% of total energy) by region
north_america = [2, 3, 4, 5, 5, 6, 7, 8, 10, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 25, 27]
europe = [5, 6, 7, 9, 10, 12, 14, 16, 19, 21, 23, 26, 29, 31, 34, 36, 39, 41, 44, 47, 50]
asia = [1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 19, 21, 23, 26, 28, 30, 33, 35, 38]

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot lines for each region
ax.plot(years, north_america, marker='o', linestyle='-', linewidth=2, color='#1f77b4', label='North America')
ax.plot(years, europe, marker='s', linestyle='-', linewidth=2, color='#ff7f0e', label='Europe')
ax.plot(years, asia, marker='^', linestyle='-', linewidth=2, color='#2ca02c', label='Asia')

# Adding titles and labels
ax.set_title("Trends in Renewable Energy Adoption\n(2000-2020)", fontsize=14, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Renewable Energy Consumption (%)", fontsize=12)

# Set grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add a legend to describe which line represents which region
ax.legend(loc='upper left', fontsize=10)

# Annotate specific years of interest
ax.annotate('Global Initiatives', xy=(2015, 40), xytext=(2012, 45),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', color='black')

# Ensuring a good fit for the plot within the figure
plt.tight_layout()

# Display the plot
plt.show()