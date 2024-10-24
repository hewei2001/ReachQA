import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Artificial data for percentage contribution of each renewable energy type
solar_power = [5, 6, 8, 12, 15, 19, 25, 30, 40, 45, 50]
wind_energy = [10, 12, 15, 17, 21, 24, 28, 32, 37, 39, 42]
hydroelectric_power = [30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]

# Plot configuration
plt.figure(figsize=(12, 8))

# Plotting the data
plt.plot(years, solar_power, marker='o', linestyle='-', color='#FFA07A', linewidth=2, label='Solar Power')
plt.plot(years, wind_energy, marker='^', linestyle='--', color='#6495ED', linewidth=2, label='Wind Energy')
plt.plot(years, hydroelectric_power, marker='s', linestyle='-.', color='#90EE90', linewidth=2, label='Hydroelectric Power')

# Annotations for key milestones
annotations = {
    2012: ("Solar Surge\nTech Breakthrough", solar_power[2]),
    2016: ("Wind Energy\nMajor Project", wind_energy[6]),
    2020: ("Hydro\nEfficiency Boost", hydroelectric_power[10])
}

for year, (text, y_value) in annotations.items():
    plt.annotate(text, xy=(year, y_value), xytext=(year, y_value + 3),
                 arrowprops=dict(facecolor='gray', shrink=0.05, width=1, headwidth=5),
                 fontsize=9, color='black', ha='center')

# Title and axis labels
plt.title('Growth of Renewable Energy Sources (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage Contribution (%)', fontsize=12)

# Legend
plt.legend(title='Energy Source', loc='upper left', fontsize=10)

# X-ticks customization
plt.xticks(years, rotation=45)

# Grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()