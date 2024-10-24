import matplotlib.pyplot as plt
import numpy as np

# Define the years and innovation impact index for each technological sector
years = np.arange(2000, 2026)
ai_innovation = np.array([20, 22, 24, 26, 30, 34, 40, 48, 60, 75, 95, 120, 150, 185, 230, 280, 350, 430, 525, 630, 750, 880, 1020, 1175, 1350, 1550])
renewable_energy = np.array([10, 12, 15, 18, 22, 28, 35, 44, 56, 70, 86, 105, 127, 153, 183, 218, 260, 308, 364, 428, 502, 586, 682, 790, 912, 1050])
biotechnology = np.array([5, 6, 8, 11, 15, 20, 27, 36, 47, 61, 78, 98, 122, 150, 183, 220, 263, 310, 365, 430, 505, 590, 687, 797, 920, 1060])
space_exploration = np.array([3, 4, 5, 6, 8, 11, 15, 21, 28, 37, 48, 62, 79, 100, 125, 155, 190, 230, 276, 328, 388, 455, 530, 615, 710, 815])

# Plotting the area chart
fig, ax = plt.subplots(figsize=(14, 8))

ax.fill_between(years, ai_innovation, label='Artificial Intelligence', color='#ff9999', alpha=0.7)
ax.fill_between(years, ai_innovation + renewable_energy, ai_innovation, label='Renewable Energy', color='#66b3ff', alpha=0.7)
ax.fill_between(years, ai_innovation + renewable_energy + biotechnology, ai_innovation + renewable_energy, label='Biotechnology', color='#99ff99', alpha=0.7)
ax.fill_between(years, ai_innovation + renewable_energy + biotechnology + space_exploration, ai_innovation + renewable_energy + biotechnology, label='Space Exploration', color='#ffcc99', alpha=0.7)

# Customize the plot
ax.set_title("Technological Evolution: The Rise of Innovations\nfrom 2000 to 2025", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Innovation Impact Index", fontsize=12)
ax.set_xticks(years[::2])  # Show every second year for better readability
ax.tick_params(axis='x', rotation=45)  # Rotate x-ticks for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add a legend
ax.legend(loc='upper left', fontsize=12, title="Technological Sectors")

# Highlight significant innovation years
highlight_years = [2010, 2020]
for year in highlight_years:
    ax.axvline(x=year, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax.text(year, 1400, 'Milestone Year', rotation=90, verticalalignment='bottom', horizontalalignment='right')

# Ensure layout is adjusted
plt.tight_layout()

# Show the plot
plt.show()