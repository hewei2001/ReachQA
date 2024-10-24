import matplotlib.pyplot as plt
import numpy as np

# Define the years and components of emission reductions
years = ["2020", "2021", "2022", "2023", "2024", "2025"]
reductions = [50, 75, 120, 160, 200, 250]  # Total reduction for each year
categories = ['Fuel Savings', 'Cleaner Energy', 'Tech Advancements']

# Breakdown of reductions into categories
components = np.array([
    [20, 15, 15],  # 2020
    [30, 25, 20],  # 2021
    [40, 45, 35],  # 2022
    [50, 60, 50],  # 2023
    [70, 80, 50],  # 2024
    [100, 90, 60],  # 2025
])

# Calculate starting points for waterfall plot
starts = np.zeros_like(reductions)
for i in range(1, len(reductions)):
    starts[i] = starts[i - 1] + reductions[i - 1]

# Colors for each component
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, Orange, Green

# Initialize plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each component as a segment of the waterfall
cumulative_reduction = np.zeros(len(years))
for i in range(len(categories)):
    ax.bar(years, components[:, i], bottom=starts, color=colors[i], edgecolor='grey', label=categories[i])
    starts += components[:, i]  # Update the start for the next component

# Plot the net reduction line for visibility
net_reductions = np.cumsum(reductions)
ax.plot(years, net_reductions, marker='o', color='black', linewidth=2, label='Net Reduction')

# Add values on bars
for x, val, net_val in zip(years, reductions, net_reductions):
    ax.text(x, val + 5, f'{val}', ha='center', va='bottom', fontsize=9)
    ax.text(x, net_val - 15, f'{net_val} tons', ha='center', va='top', fontsize=9, fontweight='bold')

# Add baseline to show start
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')

# Titles and labels
ax.set_title('Electric Vehicle Adoption Impact\non Emissions Reduction (2020-2025)', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('CO2 Emission Reduction (Metric Tons)', fontsize=12)
ax.set_xlabel('Year', fontsize=12)

# Customize legend
ax.legend(title="Reduction Contributors", title_fontsize='12', fontsize=10)

# Beautify the plot
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Ensure x-axis labels are not overlapping
plt.xticks(rotation=45, ha='right')

# Tidy layout
plt.tight_layout()

# Display the plot
plt.show()