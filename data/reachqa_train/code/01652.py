import numpy as np
import matplotlib.pyplot as plt

# Define years from 2000 to 2020
years = np.arange(2000, 2021)

# Energy production data (in TWh) for Solar, Wind, and Hydro
solar_energy = np.array([10, 12, 15, 20, 30, 40, 55, 70, 90, 115, 145, 180, 220, 265, 320, 385, 460, 550, 660, 785, 920])
wind_energy = np.array([20, 25, 30, 40, 60, 80, 110, 140, 180, 230, 290, 360, 440, 530, 630, 750, 880, 1020, 1170, 1330, 1500])
hydro_energy = np.array([300, 305, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490])

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot stacked areas
ax.stackplot(years, solar_energy, wind_energy, hydro_energy,
             labels=['Solar Energy', 'Wind Energy', 'Hydropower'],
             colors=['#FFD700', '#1E90FF', '#32CD32'], alpha=0.8)

# Title and labels
ax.set_title('The Evolution of Green Energy Production\nThe Solar, Wind, and Hydro Blend (2000-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (TWh)', fontsize=12)

# Legend
ax.legend(loc='upper left', fontsize=12, frameon=False)

# Grid lines for readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5, axis='y', alpha=0.7)

# Annotate major growth points
ax.annotate('Major Solar Expansion', xy=(2015, 500), xytext=(2009, 900),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=12, color='darkred')
ax.annotate('Wind Takes the Lead', xy=(2010, 800), xytext=(2003, 1300),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=12, color='darkblue')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()