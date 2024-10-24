import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2015, 2024)

# Data: Electric vehicle sales in thousands
# Each row represents a city: New York, London, Tokyo
ev_sales = np.array([
    [5, 8, 12, 16, 22, 29, 35, 42, 50],   # New York
    [4, 7, 10, 15, 20, 28, 38, 45, 55],   # London
    [6, 9, 14, 18, 25, 33, 41, 49, 60]    # Tokyo
])

# Error margins representing variability in predictions
error_margins = np.array([
    [0.5, 0.8, 1.0, 1.3, 2.0, 2.5, 3.0, 3.5, 4.0],  # New York
    [0.4, 0.7, 0.9, 1.2, 1.8, 2.3, 2.8, 3.4, 3.9],  # London
    [0.6, 0.9, 1.1, 1.4, 2.2, 2.7, 3.2, 3.7, 4.2]   # Tokyo
])

# City names for legend
cities = ["New York", "London", "Tokyo"]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Colors and markers for the line plots
styles = [{'color': '#FF5733', 'marker': 'o'}, 
          {'color': '#33FF57', 'marker': 's'}, 
          {'color': '#3357FF', 'marker': '^'}]

# Plot the data with error bars
for idx, city in enumerate(cities):
    ax.errorbar(
        years, ev_sales[idx], yerr=error_margins[idx], label=city, 
        fmt='-', color=styles[idx]['color'], marker=styles[idx]['marker'], 
        capsize=5, elinewidth=2, markeredgewidth=2, alpha=0.8
    )

# Adding titles and labels
ax.set_title("The Rise of Electric Vehicles\nin Major Urban Areas (2015-2023)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("EV Sales (thousands)", fontsize=12)

# Customize x-ticks and rotate for better visibility
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5, axis='y')

# Customize legend
ax.legend(title="City", fontsize=10, loc='upper left', frameon=True)

# Ensure no overlap and better layout
plt.tight_layout()

# Display the plot
plt.show()