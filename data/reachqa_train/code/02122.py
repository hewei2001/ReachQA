import matplotlib.pyplot as plt
import numpy as np

# Extended data for monthly readings over 10 years
months = np.arange(2013, 2023.75, 0.25)  # Every 3 months

# Generate extended data with realistic variation (in TWh)
wind_generation = np.interp(months, np.arange(2013, 2024), 
                            np.array([120, 140, 160, 185, 210, 235, 270, 300, 330, 360, 390]))
solar_generation = np.interp(months, np.arange(2013, 2024), 
                             np.array([30, 45, 60, 85, 110, 140, 180, 225, 280, 350, 430]))
hydro_generation = np.interp(months, np.arange(2013, 2024), 
                             np.array([200, 205, 210, 215, 220, 225, 230, 240, 250, 260, 270]))
geothermal_generation = np.linspace(15, 45, len(months)) + 5 * np.sin(np.linspace(0, 10, len(months)))

# Non-renewable comparative data
coal_generation = np.linspace(500, 400, len(months))  # Decreasing trend
gas_generation = np.linspace(300, 280, len(months))   # Slightly decreasing

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Stack plot with additional renewable source
ax.stackplot(months, wind_generation, solar_generation, hydro_generation, geothermal_generation,
             labels=['Wind', 'Solar', 'Hydroelectric', 'Geothermal'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.7)

# Line plot for non-renewables
ax.plot(months, coal_generation + gas_generation, label='Total Non-Renewable', color='gray', linestyle='-', linewidth=2, alpha=0.7)

# Title and labels
ax.set_title('Renewable and Non-Renewable Energy Generation (2013-2023)\nMonthly Data with Comparative Analysis',
             fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Generation (TWh)', fontsize=14)

# Milestones
milestones = [(2015, 'Paris Agreement'), (2020, 'Solar Surpasses Hydro')]
for year, event in milestones:
    ax.axvline(x=year, color='grey', linestyle='--', linewidth=1.5, ymin=0.05, ymax=0.9)
    ax.annotate(event, xy=(year, 750), xytext=(year, 800),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1),
                fontsize=10, ha='center', bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='lightgrey', alpha=0.5))

# Highlight significant growth points
max_solar_index = solar_generation.argmax()
ax.annotate(f'Max Solar: {solar_generation[max_solar_index]:.0f} TWh', 
            xy=(months[max_solar_index], solar_generation[max_solar_index] + hydro_generation[max_solar_index]), 
            xytext=(months[max_solar_index], solar_generation[max_solar_index] + hydro_generation[max_solar_index] + 60),
            arrowprops=dict(facecolor='orange', shrink=0.05, width=1),
            fontsize=10, color='black', ha='center')

# Grid, legend, and layout adjustments
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', title='Energy Source', fontsize=12)
plt.xticks(np.arange(2013, 2024, 1), rotation=45)
plt.tight_layout()

# Display plot
plt.show()