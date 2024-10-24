import numpy as np
import matplotlib.pyplot as plt

# Data: Energy production in TWh
years = np.arange(2000, 2021)
solar_energy = np.array([2, 4, 8, 10, 15, 20, 22, 30, 38, 50, 70, 85, 100, 130, 170, 250, 310, 400, 450, 470, 480])
wind_energy = np.array([8, 13, 20, 30, 40, 42, 45, 50, 60, 65, 70, 90, 100, 120, 150, 180, 200, 240, 250, 270, 280])
hydro_energy = np.array([300, 310, 315, 330, 340, 350, 360, 390, 410, 415, 430, 440, 450, 460, 470, 490, 500, 520, 530, 540, 550])

# Plot initialization
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, solar_energy, wind_energy, hydro_energy, labels=['Solar', 'Wind', 'Hydro'], colors=['#ffcc00', '#3388ff', '#99ee99'])

# Accent for Solar with color
ax.plot(years, solar_energy, color='orange', linestyle='--', marker='o', label='Solar - Trend')

# Customizing plot details
ax.set_title('Evolution of Renewable Energy: Solar, Wind, and Hydro (2000-2020)', fontsize=16, fontweight='bold', color='green')
ax.set_xlabel('Year', fontsize=12, color='darkblue')
ax.set_ylabel('Energy Production (TWh)', fontsize=12, color='darkblue')
ax.set_xticks(range(2000, 2021, 2))
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Highlight for breakthrough years
ax.axvline(x=2010, linestyle='--', color='c', linewidth=1.2)
ax.text(2010.5, 300, 'Break-\nthrough', verticalalignment='center', color='red', fontsize=10)

# Annotations
for y, label in zip([100, 300, 600], ['Solar', 'Wind', 'Hydro']):
    ax.text(2020.5, y, label, fontsize=10)

# Mark special points
highlight = [5, 10, 15, 17, 18, 20]
for year in years:
    if year in range(2000, 2022, 4):
        ax.annotate(f'{year}', xy=(year, solar_energy[year - 2000]), textcoords='offset points', xytext=(-30,10), ha='center')

# Setting limits
ax.set_xlim(2000, 2020)
ax.set_ylim(0, 650)

# Customize the plot
legend = ax.legend(loc='upper left', fontsize=10, shadow=True)

# Display the plot
plt.show()