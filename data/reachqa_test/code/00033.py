import matplotlib.pyplot as plt
import numpy as np

# Define the time period (years)
years = np.arange(2025, 2041)

# Define cumulative contributions of each project (in arbitrary units)
habitat_construction = np.array([5, 12, 20, 30, 45, 60, 75, 90, 110, 130, 150, 175, 200, 230, 260, 300])
water_extraction = np.array([3, 8, 14, 22, 34, 50, 70, 95, 125, 160, 200, 245, 290, 340, 395, 455])
energy_production = np.array([2, 6, 13, 22, 36, 55, 78, 105, 140, 180, 225, 275, 330, 390, 455, 525])

# Calculate annual contributions (not cumulative)
annual_habitat = np.diff(np.insert(habitat_construction, 0, 0))
annual_water = np.diff(np.insert(water_extraction, 0, 0))
annual_energy = np.diff(np.insert(energy_production, 0, 0))

# Set up the figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Create the stacked area chart in the first subplot
ax1.stackplot(years, habitat_construction, water_extraction, energy_production, 
              labels=['Habitat Construction', 'Water Extraction', 'Energy Production'], 
              colors=['#FF5733', '#33C4FF', '#FFC133'], alpha=0.7)

ax1.set_title("Progression of Mars Colonization Efforts:\nA Cumulative Journey to the Red Planet", fontsize=14, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Cumulative Contribution", fontsize=12)
ax1.legend(loc='upper left', frameon=False, fontsize=10)
ax1.set_xticks(years)
ax1.grid(alpha=0.3, linestyle='--', linewidth=0.5)

ax1.annotate('Initial Phase Begins', xy=(2025, 5), xytext=(2027, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.2),
             fontsize=10, color='black')

ax1.annotate('Significant Milestone\nAchieved', xy=(2035, 280), xytext=(2031, 400),
             arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.2),
             fontsize=10, color='black')

# Create a line chart in the second subplot for annual contributions
ax2.plot(years, annual_habitat, label='Habitat Construction', color='#FF5733', marker='o')
ax2.plot(years, annual_water, label='Water Extraction', color='#33C4FF', marker='s')
ax2.plot(years, annual_energy, label='Energy Production', color='#FFC133', marker='^')

ax2.set_title("Annual Contributions to Mars Projects", fontsize=14, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Annual Contribution", fontsize=12)
ax2.legend(loc='upper left', frameon=False, fontsize=10)
ax2.set_xticks(years)
ax2.grid(alpha=0.3, linestyle='--', linewidth=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()