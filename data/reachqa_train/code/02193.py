import matplotlib.pyplot as plt
import numpy as np

# Data for the stacked bar chart
continents = ['Europe', 'Asia', 'North America', 'South America', 'Africa', 'Oceania']
solar_energy = np.array([350, 500, 420, 150, 200, 100])
wind_energy = np.array([400, 300, 600, 100, 150, 200])
hydroelectric_energy = np.array([500, 700, 350, 450, 300, 150])
geothermal_energy = np.array([50, 100, 70, 30, 40, 60])

# Total energy for percentage calculation
total_energy = solar_energy + wind_energy + hydroelectric_energy + geothermal_energy

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(14, 8))

# Bar positions
bar_width = 0.6
x_pos = np.arange(len(continents))

# Create stacked bars with data labels
ax.bar(x_pos, solar_energy, bar_width, label='Solar', color='#FFD700', edgecolor='black')
ax.bar(x_pos, wind_energy, bar_width, bottom=solar_energy, label='Wind', color='#87CEEB', edgecolor='black')
ax.bar(x_pos, hydroelectric_energy, bar_width, bottom=solar_energy + wind_energy, label='Hydroelectric', color='#3CB371', edgecolor='black')
ax.bar(x_pos, geothermal_energy, bar_width, bottom=solar_energy + wind_energy + hydroelectric_energy, label='Geothermal', color='#FFA07A', edgecolor='black')

# Annotate values on bars
for i in range(len(continents)):
    for energy, bottom in zip(
        [solar_energy, wind_energy, hydroelectric_energy, geothermal_energy],
        [np.zeros_like(solar_energy), solar_energy, solar_energy + wind_energy, solar_energy + wind_energy + hydroelectric_energy]
    ):
        y_pos = bottom[i] + energy[i] / 2
        ax.text(x_pos[i], y_pos, f'{energy[i]}\n({energy[i] / total_energy[i] * 100:.1f}%)', ha='center', va='center', fontsize=8)

# Set labels and title
ax.set_xlabel('Continent', fontsize=12, weight='bold')
ax.set_ylabel('Energy Production (TWh)', fontsize=12, weight='bold')
ax.set_title('Global Contributions to Renewable Energy:\nA Continent-Wise Breakdown', fontsize=16, fontweight='bold')
ax.set_xticks(x_pos)
ax.set_xticklabels(continents, fontsize=10, rotation=45, ha='right')

# Add gridlines
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Add legend
ax.legend(loc='upper left', title='Energy Type', fontsize=10)

# Create an inset pie chart
# Calculate total production per energy type
energy_types = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal']
energy_totals = [sum(solar_energy), sum(wind_energy), sum(hydroelectric_energy), sum(geothermal_energy)]

inset_ax = fig.add_axes([0.75, 0.6, 0.2, 0.2], aspect=1)
inset_ax.pie(energy_totals, labels=energy_types, autopct='%1.1f%%', colors=['#FFD700', '#87CEEB', '#3CB371', '#FFA07A'])
inset_ax.set_title('Total Contribution', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()