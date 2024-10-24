import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2026)

# Define solar and wind energy capacity data (in gigawatts)
solar_capacity = np.array([15, 25, 40, 60, 90, 130, 180, 250, 350, 480, 600, 750, 900, 1080, 1300, 1550])
wind_capacity = np.array([160, 190, 220, 260, 310, 370, 450, 540, 640, 750, 870, 1000, 1150, 1300, 1470, 1650])

# Create the area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the data with fill_between for area chart
ax.fill_between(years, solar_capacity, label='Solar Energy', color='#FFD700', alpha=0.8, linestyle='-', linewidth=1)
ax.fill_between(years, wind_capacity, label='Wind Energy', color='#87CEEB', alpha=0.6, linestyle='-', linewidth=1)

# Title and labels
ax.set_title('Green Energy Revolution:\nSolar and Wind Power Trends from 2010 to 2025', fontsize=20, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Capacity (Gigawatts)', fontsize=14)

# Ensure x-axis labels are clear
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add grid lines
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend
ax.legend(loc='upper left', fontsize=12)

# Highlight specific years and annotate for clarity
highlight_years = [2015, 2020, 2025]
highlight_solar = solar_capacity[np.isin(years, highlight_years)]
highlight_wind = wind_capacity[np.isin(years, highlight_years)]

for year, solar, wind in zip(highlight_years, highlight_solar, highlight_wind):
    ax.annotate(f'{solar} GW', xy=(year, solar), xytext=(-20, -25), textcoords='offset points', 
                arrowprops=dict(facecolor='black', shrink=0.05, headwidth=8), fontsize=11, color='#FFD700')
    ax.annotate(f'{wind} GW', xy=(year, wind), xytext=(-20, -25), textcoords='offset points', 
                arrowprops=dict(facecolor='black', shrink=0.05, headwidth=8), fontsize=11, color='#87CEEB')

# Adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()