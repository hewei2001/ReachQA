import matplotlib.pyplot as plt
import numpy as np

# Define the years and sectors
years = np.arange(2020, 2041)
sectors = ['Residential', 'Commercial', 'Industrial', 'Transportation']

# Hypothetical data representing energy consumption trends in terawatt-hours (TWh)
residential = [200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350]
commercial = [150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]
industrial = [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600]
transportation = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200]

# Stack the data for area plotting
data = np.array([residential, commercial, industrial, transportation])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, data, labels=sectors, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], alpha=0.8)

# Title and axis labels
ax.set_title('Energy Consumption Trends Across Sectors\n2020-2040', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Consumption (TWh)', fontsize=14)

# Add legend
ax.legend(title='Sectors', loc='upper left', fontsize=12, bbox_to_anchor=(1.05, 1))

# Configure x and y ticks
ax.set_xticks(np.arange(2020, 2041, 2))
ax.set_yticks(np.arange(0, 1601, 200))
ax.set_xlim(2020, 2040)
ax.set_ylim(0, 1600)

# Add gridlines for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Enhance layout to avoid overlapping elements
plt.tight_layout()

# Show plot
plt.show()