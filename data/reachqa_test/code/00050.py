import matplotlib.pyplot as plt
import numpy as np

# Define years and sectoral data
years = np.arange(2025, 2031)
residential = np.array([50, 55, 60, 67, 75, 83])
commercial = np.array([40, 46, 52, 58, 65, 72])
transportation = np.array([30, 37, 45, 54, 64, 75])
industrial = np.array([60, 65, 70, 76, 83, 91])

# Prepare data for stacking
stack_data = np.vstack([residential, commercial, transportation, industrial])

# New derived data: Year-over-year percentage growth
def calculate_growth(data):
    return 100 * (data[1:] - data[:-1]) / data[:-1]

growth_years = years[1:]
residential_growth = calculate_growth(residential)
commercial_growth = calculate_growth(commercial)
transportation_growth = calculate_growth(transportation)
industrial_growth = calculate_growth(industrial)

# Define colors
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']

# Create the figure and subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# First subplot: Area plot
axes[0].stackplot(years, stack_data, labels=['Residential', 'Commercial', 'Transportation', 'Industrial'],
                  colors=colors, alpha=0.7)
axes[0].set_title("Renewable Energy Consumption\nin EcoMetropolis: Sectoral Trends (2025-2030)",
                  fontsize=14, fontweight='bold')
axes[0].set_xlabel("Year", fontsize=12)
axes[0].set_ylabel("Energy Consumption (GWh)", fontsize=12)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)
axes[0].set_xticks(years)
axes[0].set_xticklabels(years, rotation=45)
axes[0].legend(loc='upper left', title='Sectors', fontsize=9, title_fontsize=10)

# Second subplot: Line plot for growth rates
axes[1].plot(growth_years, residential_growth, label='Residential', color=colors[0], marker='o')
axes[1].plot(growth_years, commercial_growth, label='Commercial', color=colors[1], marker='o')
axes[1].plot(growth_years, transportation_growth, label='Transportation', color=colors[2], marker='o')
axes[1].plot(growth_years, industrial_growth, label='Industrial', color=colors[3], marker='o')
axes[1].set_title("Year-over-Year Growth Rate\nof Energy Consumption by Sector", fontsize=14, fontweight='bold')
axes[1].set_xlabel("Year", fontsize=12)
axes[1].set_ylabel("Growth Rate (%)", fontsize=12)
axes[1].grid(axis='y', linestyle='--', alpha=0.7)
axes[1].set_xticks(growth_years)
axes[1].set_xticklabels(growth_years, rotation=45)
axes[1].legend(loc='upper left', title='Sectors', fontsize=9, title_fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()