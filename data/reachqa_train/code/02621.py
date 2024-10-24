import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define the time period for the x-axis with the correct length
years = np.arange(3000, 3061)  # Now, it has 61 elements

# Energy data in gigawatts (GW) for each civilization
solar_giants_energy = np.array([
    20, 22, 25, 28, 30, 35, 38, 45, 55, 65, 70, 75, 80, 85, 90, 100, 105, 110, 115, 120,
    125, 130, 135, 140, 145, 150, 155, 160, 170, 180, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290,
    300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500
])

quantum_builders_energy = np.array([
    15, 18, 21, 23, 26, 30, 33, 37, 45, 50, 55, 60, 65, 70, 75, 85, 95, 100, 105, 110,
    115, 120, 125, 130, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 220,
    225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325
])

fusion_masters_energy = np.array([
    10, 12, 14, 15, 18, 20, 22, 24, 28, 30, 33, 35, 38, 40, 42, 46, 50, 55, 58, 60,
    63, 65, 67, 70, 73, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145,
    150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250
])

# Total energy by all civilizations
total_energy = solar_giants_energy + quantum_builders_energy + fusion_masters_energy

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(14, 8))

# Distinct colors for the area plot
colors = cm.Paired([0, 2, 4])

# Stack the energy data with transparency
ax.stackplot(years, solar_giants_energy, quantum_builders_energy, fusion_masters_energy,
             labels=['Solar Giants', 'Quantum Builders', 'Fusion Masters'], colors=colors, alpha=0.7)

# Overlay line plot for total energy
ax.plot(years, total_energy, color='black', linewidth=2.5, linestyle='--', label='Total Energy')

# Titles and labels
ax.set_title("Evolution of Galactic Civilizations:\nEnergy Harnessing Across the Cosmos (3000-3060 AD)", 
             fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Harnessed (Gigawatts)", fontsize=12)

# Add a legend
ax.legend(loc='upper left', title='Civilizations', fontsize=10, title_fontsize=12, frameon=True, shadow=True)

# Customize grid and style
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(3000, 3060)
ax.set_ylim(0, 1200)

# Customize the x-axis ticks
plt.xticks(years[::5], rotation=45)

# Annotate significant trends
for year, energy in zip([3030, 3050, 3060], [total_energy[30], total_energy[50], total_energy[60]]):
    ax.annotate(f'{energy:.0f} GW', xy=(year, energy), xytext=(year, energy+50),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()