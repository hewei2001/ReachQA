import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
energy_consumption = np.array([15000, 14500, 13500, 13000, 12500, 11500, 11000, 10800, 10500, 10200, 10000])
renewable_energy_use = np.array([10, 12, 15, 18, 20, 22, 25, 30, 35, 40, 45])  # Percentage of renewable energy use

# Significant events
events = {
    2010: "Energy Codes\nStandardized",
    2012: "Energy-Efficient\nAppliances Introduced",
    2015: "Solar Panels\nAdopted",
    2018: "Green\nCertifications\nImplemented",
    2020: "COVID-19\nFocus on Home\nEfficiency"
}

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Plotting the line chart
ax1.plot(years, energy_consumption, marker='o', linestyle='-', color='green', linewidth=2, label='Avg Energy Consumption (kWh/year)')
for year, event in events.items():
    ax1.annotate(event,
                 xy=(year, energy_consumption[np.where(years == year)]),
                 xytext=(year + 0.2, energy_consumption[np.where(years == year)] + 400),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=9, ha='left', va='bottom')

# Titles and labels for the line chart
ax1.set_title('Energy Efficiency Trends in Sustainable Architecture\n(2010-2020)', fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Average Energy Consumption (kWh/year)', fontsize=12)
ax1.set_xticks(years)
ax1.set_yticks(np.arange(9500, 16001, 1000))
ax1.grid(True)
ax1.legend()

# Plotting the bar chart
ax2.bar(years, renewable_energy_use, color='skyblue', width=0.5, label='Renewable Energy Use (%)')
ax2.set_title('Renewable Energy Adoption Over Time\n(2010-2020)', fontsize=16, fontweight='bold', pad=15)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Percentage of Renewable Energy Use (%)', fontsize=12)
ax2.set_xticks(years)
ax2.set_yticks(np.arange(0, 51, 5))
ax2.grid(axis='y')
ax2.legend()

# Adjust layout
plt.tight_layout()
plt.show()