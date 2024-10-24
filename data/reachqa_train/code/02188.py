import matplotlib.pyplot as plt
import numpy as np

# Define years and crop yields in tons per Martian acre
years = np.array([2050, 2051, 2052, 2053, 2054])
martian_potatoes = np.array([1.2, 1.5, 1.7, 2.0, 2.3])
red_wheat = np.array([0.9, 1.1, 1.4, 1.8, 2.0])
space_carrots = np.array([1.0, 1.2, 1.5, 1.7, 2.1])

# Calculate growth rates (change in yield relative to the previous year)
growth_potatoes = np.diff(martian_potatoes) / martian_potatoes[:-1] * 100
growth_wheat = np.diff(red_wheat) / red_wheat[:-1] * 100
growth_carrots = np.diff(space_carrots) / space_carrots[:-1] * 100

# Define new years array for growth rates (since it has one less element after diff)
growth_years = years[1:]

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot the original line plot
axes[0].plot(years, martian_potatoes, marker='o', linestyle='-', linewidth=2, color='tab:orange', label='Martian Potatoes')
axes[0].plot(years, red_wheat, marker='s', linestyle='-', linewidth=2, color='tab:green', label='Red Wheat')
axes[0].plot(years, space_carrots, marker='^', linestyle='-', linewidth=2, color='tab:blue', label='Space Carrots')

axes[0].set_title('Extraterrestrial Agriculture:\nCrop Yields on Mars (2050-2054)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Yield (tons per Martian acre)', fontsize=12)
axes[0].set_xticks(years)
axes[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[0].legend(loc='upper left', fontsize=10)

# Annotations
axes[0].annotate('Experimentation begins', xy=(2050, 1.2), xytext=(2050, 1.5),
                 arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10, color='gray')
axes[0].annotate('Optimal conditions achieved', xy=(2053, 2.0), xytext=(2052.7, 2.4),
                 arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10, color='gray')

# Plot the growth rates as a bar chart
width = 0.25  # width of the bars
axes[1].bar(growth_years - width, growth_potatoes, width=width, color='tab:orange', align='center', label='Potatoes Growth (%)')
axes[1].bar(growth_years, growth_wheat, width=width, color='tab:green', align='center', label='Wheat Growth (%)')
axes[1].bar(growth_years + width, growth_carrots, width=width, color='tab:blue', align='center', label='Carrots Growth (%)')

axes[1].set_title('Year-over-Year Growth\nof Crop Yields on Mars', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Growth Rate (%)', fontsize=12)
axes[1].set_xticks(growth_years)
axes[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[1].legend(loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()