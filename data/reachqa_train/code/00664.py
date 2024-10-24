import matplotlib.pyplot as plt
import numpy as np

# Define months
months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

# Monthly energy generation data (in GWh) for each renewable source
solar_energy = np.array([50, 60, 75, 85, 100, 120, 135, 130, 115, 95, 75, 55])
wind_energy = np.array([80, 85, 90, 95, 105, 110, 120, 125, 130, 125, 100, 90])
hydro_energy = np.array([110, 100, 115, 135, 145, 140, 150, 155, 145, 130, 115, 110])
biomass_energy = np.array([35, 37, 40, 42, 45, 47, 50, 48, 45, 42, 38, 35])

# Stack the data for area plotting
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, biomass_energy])

# Calculate the total for line overlay
total_energy = energy_data.sum(axis=0)

# Plotting the area chart
fig, ax = plt.subplots(figsize=(16, 10))

ax.stackplot(months, energy_data, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], 
             colors=['#f1c40f', '#3498db', '#1abc9c', '#e67e22'], alpha=0.85)

# Overlay line for total energy generation
ax.plot(months, total_energy, color='black', linestyle='--', linewidth=2, label='Total Energy')

# Annotate peak values
peak_month = np.argmax(total_energy)
ax.annotate(f'Peak: {total_energy[peak_month]} GWh', 
            xy=(months[peak_month], total_energy[peak_month]), 
            xytext=(months[peak_month], total_energy[peak_month] + 20), 
            arrowprops=dict(facecolor='black', arrowstyle='->'), 
            fontsize=12, fontweight='bold', color='black')

# Adding horizontal line for average energy generation
average_energy = total_energy.mean()
ax.axhline(y=average_energy, color='gray', linestyle='-.', linewidth=1.5, label=f'Average: {average_energy:.1f} GWh')

# Titles and labels
ax.set_title('Emerging Trends in Renewable Energy Generation:\nTracking Monthly Output in 2023', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Energy Generation (GWh)', fontsize=14)

# Rotate x-axis labels for better readability
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, rotation=45, ha='right')

# Add legend with improved readability
ax.legend(loc='upper left', fontsize=12)

# Enhanced grid lines for clarity
ax.grid(alpha=0.5, linestyle='--', linewidth=0.7)

# Adjust layout to prevent overlapping elements
fig.tight_layout()

# Display the plot
plt.show()