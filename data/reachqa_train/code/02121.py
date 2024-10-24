import matplotlib.pyplot as plt
import numpy as np

# Years for the x-axis
years = np.arange(2013, 2024)

# Data for each renewable energy source (in TWh)
wind_generation = np.array([120, 140, 160, 185, 210, 235, 270, 300, 330, 360, 390])  # Steady growth
solar_generation = np.array([30, 45, 60, 85, 110, 140, 180, 225, 280, 350, 430])    # Rapid growth
hydro_generation = np.array([200, 205, 210, 215, 220, 225, 230, 240, 250, 260, 270])  # Stable growth

# Create the area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Stack the area plots for a better visualization
ax.stackplot(years, wind_generation, solar_generation, hydro_generation, 
             labels=['Wind', 'Solar', 'Hydroelectric'], 
             colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.7)

# Title and labels
ax.set_title('Renewable Energy Generation by Source:\nA Decade of Growth and Change (2013-2023)', 
             fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Generation (TWh)', fontsize=14)

# Grid and legend
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', title='Energy Source', fontsize=12)

# Highlight key milestones
milestones = [(2015, 'Paris Agreement'), (2020, 'Solar Surpasses Hydro')]
for year, event in milestones:
    ax.axvline(x=year, color='grey', linestyle='--', linewidth=1.5, ymin=0.05, ymax=0.9)
    ax.annotate(event, xy=(year, 650), xytext=(year, 700),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1),
                fontsize=10, ha='center', bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='lightgrey', alpha=0.5))

# Annotate significant points in the data
max_solar_year = years[solar_generation.argmax()]
max_solar_value = solar_generation.max()
ax.annotate(f'Max Solar: {max_solar_value} TWh', 
            xy=(max_solar_year, max_solar_value + hydro_generation[solar_generation.argmax()]), 
            xytext=(max_solar_year, max_solar_value + hydro_generation[solar_generation.argmax()] + 50),
            arrowprops=dict(facecolor='orange', shrink=0.05, width=1),
            fontsize=10, color='black', ha='center')

# Adjust x-axis labels for readability
plt.xticks(years, rotation=45)

# Adjust layout to prevent overlapping of labels
plt.tight_layout()

# Display the plot
plt.show()