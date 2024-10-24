import matplotlib.pyplot as plt
import numpy as np

# Define the years for the data
years = np.arange(2000, 2020)

# Energy contributions in percentage over the years
solar_energy = np.array([2, 3, 5, 8, 12, 18, 24, 30, 35, 42, 48, 54, 60, 65, 68, 70, 72, 73, 74, 75])
wind_energy = np.array([5, 6, 8, 10, 13, 17, 20, 24, 27, 30, 32, 34, 36, 38, 39, 40, 41, 42, 42, 43])
hydro_energy = np.array([15, 16, 17, 18, 20, 21, 22, 23, 23, 24, 24, 25, 26, 26, 27, 28, 28, 29, 30, 31])

# Cumulative data for bar chart subplot
cumulative_energy = solar_energy + wind_energy + hydro_energy

# Create a figure with two subplots side by side
fig, axs = plt.subplots(1, 2, figsize=(18, 7))

# First subplot: Area chart
axs[0].stackplot(years, solar_energy, wind_energy, hydro_energy, labels=['Solar', 'Wind', 'Hydroelectric'],
                 colors=['#FFD700', '#87CEEB', '#3CB371'], alpha=0.8)
axs[0].set_title("Evolution of Renewable Energy Adoption\nin Enchanted Valleys (2000-2019)", fontsize=14, fontweight='bold', pad=20)
axs[0].set_xlabel("Years", fontsize=12)
axs[0].set_ylabel("Percentage of Total Energy Consumption", fontsize=12)
axs[0].set_xlim(years.min(), years.max())
axs[0].set_ylim(0, 100)
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].legend(title="Energy Type", loc="upper left", fontsize=11, frameon=False)
axs[0].annotate('Major Solar Initiative', xy=(2005, 18), xytext=(2003, 30),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
axs[0].annotate('Wind Energy Peaks', xy=(2015, 90), xytext=(2012, 70),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
axs[0].tick_params(axis='x', rotation=45)

# Second subplot: Bar chart
axs[1].bar(years, cumulative_energy, color='lightcoral', alpha=0.7)
axs[1].set_title("Cumulative Renewable Energy Contribution\nin Enchanted Valleys (2000-2019)", fontsize=14, fontweight='bold', pad=20)
axs[1].set_xlabel("Years", fontsize=12)
axs[1].set_ylabel("Cumulative Percentage", fontsize=12)
axs[1].set_xlim(years.min() - 0.5, years.max() + 0.5)
axs[1].set_ylim(0, 150)
axs[1].grid(True, linestyle='--', alpha=0.5)
for index, value in enumerate(cumulative_energy):
    axs[1].text(years[index], value + 2, f'{value}%', ha='center', va='bottom', fontsize=9)
axs[1].tick_params(axis='x', rotation=45)

# Adjust layout to fit everything neatly
plt.tight_layout()

# Show plot
plt.show()