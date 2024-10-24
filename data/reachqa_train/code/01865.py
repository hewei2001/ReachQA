import matplotlib.pyplot as plt
import numpy as np

# Define the decades for the x-axis
decades = ['1990s', '2000s', '2010s', '2020s']

# Contribution of each renewable source (in arbitrary units)
solar_energy = [5, 15, 50, 120]    # Exponential growth
wind_energy = [10, 25, 60, 150]    # Rapid growth
hydroelectric = [100, 120, 150, 160] # Stable growth
biomass_energy = [20, 30, 40, 55]  # Steady growth

# Total renewable energy as percentage of total energy consumption
total_renewable_percent = [10, 15, 30, 45]  # Hypothetical data for overlay

# Stack these contributions for the area chart
energy_data = np.array([solar_energy, wind_energy, hydroelectric, biomass_energy])

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 7))

# Define colors for each energy source
colors = ['#FFA07A', '#20B2AA', '#87CEEB', '#FFD700']

# Create stacked area chart
ax1.stackplot(decades, energy_data, labels=['Solar', 'Wind', 'Hydroelectric', 'Biomass'], colors=colors, alpha=0.8)

# Overlay a line plot for total renewable energy percentage
ax2 = ax1.twinx()  # Create a secondary y-axis
ax2.plot(decades, total_renewable_percent, color='#8B008B', linestyle='--', marker='o', label='Total Renewable %')

# Title and labels
ax1.set_title('Contribution of Renewable Energy Sources Over Decades\nand Total Renewable Energy Percentage', 
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Decade', fontsize=12)
ax1.set_ylabel('Energy Contribution\n(Arbitrary Units)', fontsize=12)
ax2.set_ylabel('Total Renewable Energy (%)', fontsize=12)

# Legends
ax1.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), title='Energy Type')
ax2.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 0.9))

# Annotate significant points
for i, txt in enumerate(total_renewable_percent):
    ax2.annotate(f'{txt}%', (decades[i], total_renewable_percent[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Add grid to the primary axis
ax1.grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()