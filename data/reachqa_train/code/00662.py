import numpy as np
import matplotlib.pyplot as plt

# Define the years for the data
years = np.arange(2000, 2021)

# Fictional data for renewable energy adoption (in gigawatts)
solar = np.array([
    5, 10, 15, 20, 30, 45, 60, 85, 110, 140, 
    175, 215, 250, 295, 350, 410, 475, 550, 640, 740, 850
])
wind = np.array([
    10, 15, 20, 30, 45, 60, 75, 90, 110, 130, 
    155, 185, 220, 265, 320, 380, 450, 530, 620, 720, 830
])
hydro = np.array([
    30, 35, 40, 45, 50, 55, 60, 70, 80, 95, 
    115, 135, 160, 190, 225, 265, 310, 360, 420, 490, 570
])

# Construct total energy for line plot
total_energy = solar + wind + hydro

# Use a different, fictive dataset for the percentage adoption overlay
percentage_adoption = (total_energy / (total_energy + 1500)) * 100

# Stack the data for the area plot
energy_data = np.vstack([solar, wind, hydro])

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Define colors and labels
colors = ['#FFD700', '#00BFFF', '#32CD32']
labels = ['Solar Power', 'Wind Power', 'Hydroelectric Power']

# Plot stacked area chart
ax1.stackplot(years, energy_data, labels=labels, colors=colors, alpha=0.85)

# Plot line for total energy
ax1.plot(years, total_energy, color='black', linewidth=2, linestyle='--', label='Total Renewable Energy')

# Create a second y-axis for percentage adoption
ax2 = ax1.twinx()
ax2.plot(years, percentage_adoption, color='darkred', linewidth=2, linestyle='-.', marker='o', label='Percentage Adoption (%)')
ax2.set_ylabel('Adoption (%)', fontsize=14, color='darkred')
ax2.tick_params(axis='y', labelcolor='darkred')

# Customize the plot
ax1.set_title("Renewable Energy Adoption and Percentage Growth\n2000-2020", fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Adoption (Gigawatts)', fontsize=14)

# Add legends
ax1.legend(loc='upper left', fontsize=12, frameon=False)
ax2.legend(loc='upper right', fontsize=12, frameon=False)

# Annotate significant transitions
ax1.annotate('Major Solar Investment', xy=(2015, 200), xytext=(2008, 700),
             arrowprops=dict(facecolor='gold', arrowstyle='->', lw=1.5),
             fontsize=12, color='gold')

ax1.annotate('Wind Power Surge', xy=(2020, 530), xytext=(2013, 1000),
             arrowprops=dict(facecolor='blue', arrowstyle='->', lw=1.5),
             fontsize=12, color='blue')

# Text box for context
props = dict(boxstyle='round', facecolor='lightgray', alpha=0.3)
textstr = ('Continents have significantly\n'
           'increased their renewable\n'
           'energy adoption over 20 years.')
ax1.text(0.02, 0.95, textstr, transform=ax1.transAxes, fontsize=12,
         verticalalignment='top', bbox=props)

# Highlight start and end values for each energy source
for idx, energy in enumerate(labels):
    ax1.annotate(f'{energy_data[idx, 0]}', (2000, energy_data[idx, 0]),
                 textcoords="offset points", xytext=(-15, 5), ha='center')
    ax1.annotate(f'{energy_data[idx, -1]}', (2020, energy_data[idx, -1] + np.sum(energy_data[:idx, -1])),
                 textcoords="offset points", xytext=(-15, -10), ha='center')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()