import matplotlib.pyplot as plt
import numpy as np

# Define years and emissions data
years = ['2019', '2020', '2021', '2022', '2023']
residential_emissions = [1200, 1250, 1300, 1350, 1400]
commercial_emissions = [800, 850, 900, 950, 1000]
industrial_emissions = [1500, 1600, 1550, 1450, 1400]
transportation_emissions = [2000, 2100, 2200, 2300, 2400]

# Compile data into a stacked format
emissions_data = [residential_emissions, commercial_emissions, industrial_emissions, transportation_emissions]
sectors = ['Residential', 'Commercial', 'Industrial', 'Transportation']

# Create the bar positions
bar_width = 0.5
x = np.arange(len(years))

# Plotting the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Create the stacked bars with new colors and transparency
colors = ['#AEEEEE', '#98FB98', '#FFB6C1', '#FFD700']
ax.bar(x, residential_emissions, width=bar_width, label='Residential', color=colors[0], alpha=0.8)
ax.bar(x, commercial_emissions, width=bar_width, bottom=residential_emissions, label='Commercial', color=colors[1], alpha=0.8)
ax.bar(x, industrial_emissions, width=bar_width, 
       bottom=np.array(residential_emissions) + np.array(commercial_emissions),
       label='Industrial', color=colors[2], alpha=0.8)
ax.bar(x, transportation_emissions, width=bar_width,
       bottom=np.array(residential_emissions) + np.array(commercial_emissions) + np.array(industrial_emissions),
       label='Transportation', color=colors[3], alpha=0.8)

# Adding data labels on top of each bar segment
for i in range(len(years)):
    ax.text(i, residential_emissions[i]/2, str(residential_emissions[i]), ha='center', va='bottom')
    ax.text(i, residential_emissions[i] + commercial_emissions[i]/2, str(commercial_emissions[i]), ha='center', va='bottom')
    ax.text(i, residential_emissions[i] + commercial_emissions[i] + industrial_emissions[i]/2, str(industrial_emissions[i]), ha='center', va='bottom')
    ax.text(i, residential_emissions[i] + commercial_emissions[i] + industrial_emissions[i] + transportation_emissions[i]/2, str(transportation_emissions[i]), ha='center', va='bottom')

# Adding labels and title
ax.set_xlabel("Years", fontsize=12)
ax.set_ylabel("Greenhouse Gas Emissions (metric tons CO2e)", fontsize=12)
ax.set_title("Urban Development's Environmental Impact:\nGreenwood (2019-2023)", fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend(title='Emissions Sources', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Enable gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_ylim(0, 6000)

# Rotating x-tick labels for clarity
plt.xticks(rotation=0)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()