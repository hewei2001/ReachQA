import matplotlib.pyplot as plt
import numpy as np

# Years from 2018 to 2022
years = np.array([2018, 2019, 2020, 2021, 2022])

# Energy consumption data for each sector (in gigawatt-hours)
gaming_energy = np.array([120, 150, 200, 250, 300])
education_energy = np.array([30, 45, 70, 100, 140])
tourism_energy = np.array([50, 60, 85, 110, 150])

# Calculate yearly growth rate percentage for each sector
gaming_growth = np.diff(gaming_energy) / gaming_energy[:-1] * 100
education_growth = np.diff(education_energy) / education_energy[:-1] * 100
tourism_growth = np.diff(tourism_energy) / tourism_energy[:-1] * 100

# Set up a 1x2 grid for plots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# First subplot: Stacked area chart
axes[0].stackplot(years, gaming_energy, education_energy, tourism_energy, 
                  labels=['Gaming', 'Education', 'Virtual Tourism'], 
                  colors=['#1f78b4', '#33a02c', '#fb9a99'], alpha=0.85)
axes[0].set_title('Evolution of Energy Consumption in\nVirtual Reality Experiences (2018-2022)', fontsize=14, pad=10)
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Energy Consumption\n(Gigawatt-Hours)', fontsize=12)
axes[0].set_xticks(years)
axes[0].set_yticks(np.arange(0, 501, 50))
axes[0].legend(loc='upper left', fontsize=10, title='VR Sector', title_fontsize='12')
axes[0].grid(True, which='major', linestyle='--', linewidth=0.7, alpha=0.7)

# Annotate peak consumption for each sector in the last year
axes[0].annotate(f'{gaming_energy[-1]} GWh', xy=(2022, gaming_energy[-1]-20), 
                 xytext=(2021.8, gaming_energy[-1]+30), fontsize=10, arrowprops=dict(arrowstyle='->'))
axes[0].annotate(f'{education_energy[-1]} GWh', xy=(2022, sum(gaming_energy[-1:] + education_energy[-1:])), 
                 xytext=(2021.8, sum(gaming_energy[-1:]+education_energy[-1:])+30), fontsize=10, arrowprops=dict(arrowstyle='->'))
axes[0].annotate(f'{tourism_energy[-1]} GWh', xy=(2022, sum(gaming_energy[-1:]+education_energy[-1:]+tourism_energy[-1:])), 
                 xytext=(2021.8, sum(gaming_energy[-1:]+education_energy[-1:]+tourism_energy[-1:])-50), fontsize=10, arrowprops=dict(arrowstyle='->'))

# Second subplot: Line plot of growth rates
axes[1].plot(years[1:], gaming_growth, marker='o', label='Gaming Growth', color='#1f78b4')
axes[1].plot(years[1:], education_growth, marker='o', label='Education Growth', color='#33a02c')
axes[1].plot(years[1:], tourism_growth, marker='o', label='Tourism Growth', color='#fb9a99')
axes[1].set_title('Year-over-Year Growth Rate in Energy Consumption\n(2019-2022)', fontsize=14, pad=10)
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Growth Rate (%)', fontsize=12)
axes[1].set_xticks(years[1:])
axes[1].legend(loc='upper right', fontsize=10, title='Growth Rate', title_fontsize='12')
axes[1].grid(True, which='major', linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust layout for better fit
plt.tight_layout()

# Show plot
plt.show()