import matplotlib.pyplot as plt
import numpy as np

# Time period from 2000 to 2020
years = np.arange(2000, 2021)

# Hypothetical data representing energy consumption in different categories (solar, wind, etc.)
region_data = {
    'Solar': np.array([20, 22, 25, 30, 35, 40, 45, 50, 60, 70, 80, 95, 110, 125, 140, 160, 180, 200, 220, 240, 260]),
    'Wind': np.array([10, 12, 15, 18, 22, 28, 35, 40, 50, 65, 80, 90, 100, 110, 125, 140, 155, 170, 185, 200, 220]),
    'Hydro': np.array([50, 52, 54, 55, 58, 60, 65, 70, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140]),
    'Geothermal': np.array([5, 5, 6, 7, 8, 10, 12, 15, 18, 22, 28, 35, 38, 42, 45, 50, 55, 60, 65, 70, 75]),
    'Biomass': np.array([15, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 68, 72, 78, 80, 85, 90, 95, 100])
}

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot stacked area chart
ax.stackplot(years, region_data.values(), labels=region_data.keys(), colors=['#FFD700', '#87CEEB', '#32CD32', '#FF6347', '#8B4513'], alpha=0.8)

# Title and labels
ax.set_title('Renewable Energy Adoption Over Time\nImaginary Regions from 2000 to 2020', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Consumption (Hypothetical Units)', fontsize=12)

# Add legend
ax.legend(loc='upper left', fontsize=10, title='Energy Sources')

# Add grid for clarity
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()