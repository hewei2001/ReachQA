import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Energy sources contributions (percentage of total renewable energy)
solar = [5, 7, 10, 15, 20, 25, 30, 35, 38, 42, 45]
wind = [30, 28, 27, 25, 22, 20, 18, 17, 17, 16, 15]
hydroelectric = [50, 48, 45, 42, 40, 38, 35, 33, 32, 31, 30]
biomass = [15, 17, 18, 18, 18, 17, 17, 15, 13, 11, 10]

# Hypothetical total renewable energy capacity in MW (arbitrary values for demonstration)
total_capacity_mw = [150, 160, 175, 190, 210, 230, 250, 270, 290, 310, 330]

# Create a figure with two subplots
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Stacked area plot
ax[0].stackplot(years, solar, wind, hydroelectric, biomass, 
                labels=['Solar', 'Wind', 'Hydroelectric', 'Biomass'], 
                colors=['#FFD700', '#87CEEB', '#32CD32', '#8B4513'], alpha=0.8)
ax[0].set_title("Renewable Energy Source Contributions\n(2010-2020)", fontsize=14, fontweight='bold', pad=15)
ax[0].set_xlabel('Year', fontsize=11)
ax[0].set_ylabel('Percentage of Total Renewable Energy', fontsize=11)
ax[0].legend(loc='upper left', title="Energy Sources", fontsize=9, title_fontsize=10)
ax[0].grid(True, linestyle='--', alpha=0.5)
ax[0].set_xticks(years)
ax[0].tick_params(axis='x', rotation=45)

# Bar chart for total renewable energy capacity
ax[1].bar(years, total_capacity_mw, color='#6495ED', alpha=0.7)
ax[1].set_title("Total Renewable Energy Capacity\n(2010-2020)", fontsize=14, fontweight='bold', pad=15)
ax[1].set_xlabel('Year', fontsize=11)
ax[1].set_ylabel('Capacity (MW)', fontsize=11)
for i, value in enumerate(total_capacity_mw):
    ax[1].text(years[i], value + 5, str(value), ha='center', va='bottom', fontsize=9)
ax[1].grid(True, linestyle='--', alpha=0.5)
ax[1].set_xticks(years)
ax[1].tick_params(axis='x', rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()