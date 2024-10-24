import matplotlib.pyplot as plt
import numpy as np

# Define the years for which we have data
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])

# Energy consumption data for each sector (in terawatt-hours)
residential = np.array([300, 290, 280, 270, 260, 250])
commercial = np.array([220, 230, 235, 240, 245, 250])
industrial = np.array([350, 340, 330, 320, 310, 300])
transportation = np.array([130, 135, 140, 145, 150, 155])

# Stack the data to create an area chart
consumption_data = np.vstack([residential, commercial, industrial, transportation])

# Define labels and colors for each sector
labels = ['Residential', 'Commercial', 'Industrial', 'Transportation']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Colors for each area

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the stacked area chart
ax.stackplot(years, consumption_data, labels=labels, colors=colors, alpha=0.8)

# Set plot labels and title
ax.set_title("Energy Consumption Trends in TechnoVille (2020-2025)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Consumption (TWh)", fontsize=12)

# Rotate x-axis labels to prevent overlap
plt.xticks(years, rotation=45)

# Add a legend to the chart
ax.legend(loc='upper left', title="Sectors")

# Enhance grid for readability
ax.grid(True, linestyle='--', alpha=0.5)

# Use tight layout to adjust elements
plt.tight_layout()

# Display the plot
plt.show()