import matplotlib.pyplot as plt
import numpy as np

# Years from 2025 to 2030
years = np.array([2025, 2026, 2027, 2028, 2029, 2030])

# Energy consumption data for each sector (TWh)
residential = np.array([120, 125, 130, 135, 140, 145])
commercial = np.array([150, 145, 155, 160, 165, 170])
transportation = np.array([100, 95, 90, 85, 80, 75])
industrial = np.array([130, 135, 140, 145, 150, 155])
total_consumption = residential + commercial + transportation + industrial

# Create a figure and axis with a secondary y-axis
fig, ax1 = plt.subplots(figsize=(12, 8))
ax2 = ax1.twinx()

# Create a stacked area chart
ax1.stackplot(years, residential, commercial, transportation, industrial, 
              labels=['Residential', 'Commercial', 'Transportation', 'Industrial'],
              colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], alpha=0.8)

# Plot a line on the secondary y-axis
ax2.plot(years, total_consumption, 'k--', label='Total Consumption (TWh)', linewidth=1.5)

# Add annotations
for i, txt in enumerate(total_consumption):
    ax2.annotate(txt, (years[i], total_consumption[i]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=8)

# Enhance plot with title, labels, and legend
ax1.set_title('Energy Consumption Trends\nin Future Smart Cities (2025-2030)', fontsize=16, weight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Consumption by Sector (TWh)', fontsize=12)
ax2.set_ylabel('Total Energy Consumption (TWh)', fontsize=12, color='k')
ax1.legend(loc='upper left', bbox_to_anchor=(0.1, -0.1), ncol=2, fontsize=10)
ax2.legend(loc='upper left', bbox_to_anchor=(0.5, -0.1), ncol=1, fontsize=10)

# Add gridlines
ax1.grid(visible=True, linestyle='--', linewidth=0.5, color='gray', which='both')

# Add markers on the line plot
ax2.scatter(years, total_consumption, color='k')

# Adjust layout to prevent clipping of labels
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show plot
plt.show()