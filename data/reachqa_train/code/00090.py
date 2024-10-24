import matplotlib.pyplot as plt
import numpy as np

# Seasons
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# Population sizes for each butterfly species per season
golden_monarch = [150, 300, 250, 200]
azure_wing = [200, 150, 300, 100]
crimson_admiral = [100, 250, 150, 250]

# Prepare data for the stacked area chart
species_data = np.array([golden_monarch, azure_wing, crimson_admiral])

# Additional data for overlay plot (e.g., average temperature)
average_temperature = [15, 25, 20, 10]

# Plot the stacked area chart
fig, ax1 = plt.subplots(figsize=(12, 8))

ax1.stackplot(seasons, species_data, labels=['Golden Monarch', 'Azure Wing', 'Crimson Admiral'],
              colors=['gold', 'skyblue', 'crimson'], alpha=0.8)

# Customizing the area chart
ax1.set_title("Migration Patterns of Butterfly Species\nInfluenced by Seasonal Temperature\nin the Enchanted Forest",
              fontsize=16, pad=20)
ax1.set_xlabel("Seasons", fontsize=12)
ax1.set_ylabel("Population Size", fontsize=12)

# Annotate significant changes
ax1.annotate('Peak Monarch', xy=('Summer', 450), xytext=('Summer', 500),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adding grid lines for better readability
ax1.grid(True, linestyle='--', alpha=0.5)

# Rotate x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Adding secondary y-axis for temperature
ax2 = ax1.twinx()
ax2.plot(seasons, average_temperature, label='Average Temperature', color='orange', marker='o', linestyle='--')
ax2.set_ylabel('Temperature (°C)', fontsize=12)

# Enhanced Legend: Combining legends from both axes
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, title='Legend', loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout for a neat look
plt.tight_layout()

# Show plot
plt.show()