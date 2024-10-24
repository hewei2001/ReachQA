import matplotlib.pyplot as plt
import numpy as np

# Years from 2018 to 2022
years = np.array([2018, 2019, 2020, 2021, 2022])

# Energy consumption data for each sector (in gigawatt-hours)
gaming_energy = np.array([120, 150, 200, 250, 300])
education_energy = np.array([30, 45, 70, 100, 140])
tourism_energy = np.array([50, 60, 85, 110, 150])

# Plot setup
plt.figure(figsize=(12, 8))

# Stacked area chart
plt.stackplot(years, gaming_energy, education_energy, tourism_energy, 
              labels=['Gaming', 'Education', 'Virtual Tourism'], 
              colors=['#1f78b4', '#33a02c', '#fb9a99'], alpha=0.85)

# Chart details
plt.title('Evolution of Energy Consumption in\nVirtual Reality Experiences (2018-2022)', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Consumption\n(Gigawatt-Hours)', fontsize=12)
plt.xticks(years, fontsize=10)
plt.yticks(np.arange(0, 501, 50), fontsize=10)
plt.legend(loc='upper left', fontsize=10, title='VR Sector', title_fontsize='12')

# Add gridlines for better readability
plt.grid(True, which='major', linestyle='--', linewidth=0.7, alpha=0.7)
plt.grid(True, which='minor', linestyle=':', linewidth=0.5, alpha=0.5)

# Annotate peak consumption for each sector in the last year
plt.annotate(f'{gaming_energy[-1]} GWh', xy=(2022, gaming_energy[-1]-20), 
             xytext=(2021.8, gaming_energy[-1]+30), fontsize=10, arrowprops=dict(arrowstyle='->'))
plt.annotate(f'{education_energy[-1]} GWh', xy=(2022, sum(gaming_energy[-1:] + education_energy[-1:])), 
             xytext=(2021.8, sum(gaming_energy[-1:]+education_energy[-1:])+30), fontsize=10, arrowprops=dict(arrowstyle='->'))
plt.annotate(f'{tourism_energy[-1]} GWh', xy=(2022, sum(gaming_energy[-1:]+education_energy[-1:]+tourism_energy[-1:])), 
             xytext=(2021.8, sum(gaming_energy[-1:]+education_energy[-1:]+tourism_energy[-1:])-50), fontsize=10, arrowprops=dict(arrowstyle='->'))

# Automatically adjust layout for better fit
plt.tight_layout()

# Show plot
plt.show()