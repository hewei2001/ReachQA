import matplotlib.pyplot as plt
import numpy as np

# Define the years for which we have data
years = np.arange(2020, 2036)

# Energy consumption data for each sector (in terawatt-hours)
# Adding additional sectors and extending the dataset
residential = np.array([300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150])
commercial = np.array([220, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300])
industrial = np.array([350, 340, 330, 320, 310, 300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200])
transportation = np.array([130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205])
agricultural = np.array([50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80])

# Stack the data to create an area chart
consumption_data = np.vstack([residential, commercial, industrial, transportation, agricultural])

# Define labels and colors for each sector
labels = ['Residential', 'Commercial', 'Industrial', 'Transportation', 'Agricultural']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ffb3e6']  # Colors for each area

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax.stackplot(years, consumption_data, labels=labels, colors=colors, alpha=0.8)

# Overlay a cumulative total line plot
cumulative_total = np.sum(consumption_data, axis=0)
ax.plot(years, cumulative_total, color='black', linewidth=2.5, label='Total Consumption (TWh)')

# Set plot labels and title
ax.set_title("Energy Consumption Trends in TechnoVille (2020-2035)\nIncluding Projections and Cumulative Total", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Consumption (TWh)", fontsize=12)

# Rotate x-axis labels to prevent overlap
plt.xticks(years, rotation=45)

# Add a legend to the chart
ax.legend(loc='upper right', title="Sectors", fontsize=10)

# Enhance grid for readability
ax.grid(True, linestyle='--', alpha=0.5)

# Annotations for significant events
ax.annotate('Tech Regulation Policy', xy=(2028, 900), xytext=(2025, 950),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Use tight layout to adjust elements
plt.tight_layout()

# Display the plot
plt.show()