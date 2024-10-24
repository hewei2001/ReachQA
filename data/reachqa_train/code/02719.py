import matplotlib.pyplot as plt
import numpy as np

# Decades from the 1980s to the 2020s
decades = ['1980s', '1990s', '2000s', '2010s', '2020s']

# Data for renewable energy adoption in gigawatts (GW)
solar_power = [2, 4, 18, 200, 600]
wind_power = [10, 25, 100, 400, 700]
hydroelectric_power = [500, 600, 750, 850, 900]

# Calculate the percentage increase per decade for each energy source
def calculate_percentage_increase(data):
    return [((data[i] - data[i - 1]) / data[i - 1]) * 100 if i != 0 else 0 for i in range(len(data))]

solar_growth = calculate_percentage_increase(solar_power)
wind_growth = calculate_percentage_increase(wind_power)
hydro_growth = calculate_percentage_increase(hydroelectric_power)

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each energy source
ax1.plot(decades, solar_power, marker='o', linestyle='-', color='gold', linewidth=2.5, label='Solar Power')
ax1.plot(decades, wind_power, marker='s', linestyle='-', color='skyblue', linewidth=2.5, label='Wind Power')
ax1.plot(decades, hydroelectric_power, marker='^', linestyle='-', color='seagreen', linewidth=2.5, label='Hydroelectric Power')

# Secondary axis for percentage growth
ax2 = ax1.twinx()
width = 0.3  # Bar width
x_indexes = np.arange(len(decades))

# Plot bar graphs for percentage growth
ax2.bar(x_indexes - width, solar_growth, width=width, color='gold', alpha=0.3, label='Solar Growth %')
ax2.bar(x_indexes, wind_growth, width=width, color='skyblue', alpha=0.3, label='Wind Growth %')
ax2.bar(x_indexes + width, hydro_growth, width=width, color='seagreen', alpha=0.3, label='Hydro Growth %')

# Title and labels with adjusted line breaks
ax1.set_title("Renewable Energy Adoption and Growth Over the Decades\nFrom the 1980s to the 2020s", fontsize=16, fontweight='bold')
ax1.set_xlabel("Decade", fontsize=12)
ax1.set_ylabel("Energy Production (Gigawatts)", fontsize=12)
ax2.set_ylabel("Growth Percentage (%)", fontsize=12)

# Adding grid for better readability
ax1.grid(True, linestyle='--', alpha=0.7)

# Legends
ax1.legend(loc='upper left', fontsize=11)
ax2.legend(loc='upper right', fontsize=11)

# Adjust layout
fig.tight_layout()

# Display the plot
plt.show()