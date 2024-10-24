import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data setup for Quantum Volume
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])
quantum_volume = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048])

# Hypothetical "Technology Advancement Index"
tech_advancement = 50 / (1 + np.exp(-0.5 * (years - 2018))) + 5  # Logistic growth

# Create a smooth line for Quantum Volume
x_smooth = np.linspace(years.min(), years.max(), 300)
spl_qv = make_interp_spline(years, quantum_volume, k=3)
y_smooth_qv = spl_qv(x_smooth)

# Plot creation
fig, ax1 = plt.subplots(figsize=(12, 8))

# Primary plot - Quantum Volume
ax1.scatter(years, quantum_volume, color='royalblue', label='Quantum Volume', alpha=0.8, edgecolors='k', s=100)
ax1.plot(x_smooth, y_smooth_qv, color='crimson', linewidth=2, linestyle='-', label='Exponential Fit')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Quantum Volume", fontsize=12, color='crimson')
ax1.set_yscale('log')
ax1.set_xlim(years.min() - 1, years.max() + 1)
ax1.set_ylim(1, max(quantum_volume) * 1.1)
ax1.tick_params(axis='y', labelcolor='crimson')

# Secondary plot - Technology Advancement Index
ax2 = ax1.twinx()
ax2.plot(years, tech_advancement, color='forestgreen', linewidth=2, linestyle='--', label='Tech Advancement Index')
ax2.set_ylabel("Tech Advancement Index", fontsize=12, color='forestgreen')
ax2.set_ylim(0, max(tech_advancement) * 1.1)
ax2.tick_params(axis='y', labelcolor='forestgreen')

# Titles and grid
plt.title("The Rise of Quantum Computing Performance\nQuantum Volume Growth & Tech Advancement (2015-2025)", 
          fontsize=16, fontweight='bold', pad=20)
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.xticks(years, rotation=45)

# Legends
fig.legend(loc='upper left', bbox_to_anchor=(0.15, 0.95), fontsize=10)

# Layout adjustment
plt.tight_layout()

# Display the plot
plt.show()