import matplotlib.pyplot as plt
import numpy as np

# Years from 2020 to 2030
years = np.arange(2020, 2031)

# Installed capacity data (in GW) for each energy source
solar_capacity = np.array([200, 220, 250, 290, 340, 400, 470, 550, 650, 770, 900])
wind_capacity = np.array([180, 200, 230, 260, 300, 350, 410, 480, 560, 650, 750])
hydro_capacity = np.array([300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400])

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.25  # Width of the bars

# Calculate the positions for the bars
solar_positions = years - bar_width
wind_positions = years
hydro_positions = years + bar_width

# Create bars for each energy source
bars_solar = ax.bar(solar_positions, solar_capacity, width=bar_width, color='gold', label='Solar Energy')
bars_wind = ax.bar(wind_positions, wind_capacity, width=bar_width, color='skyblue', label='Wind Energy')
bars_hydro = ax.bar(hydro_positions, hydro_capacity, width=bar_width, color='green', label='Hydropower')

# Set the title and labels
ax.set_title('The Rise of Renewable Energy Sources\n2020 to 2030', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Installed Capacity (GW)', fontsize=12)

# Set x-ticks and labels
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add legend to identify different energy sources
ax.legend(loc='upper left', fontsize=10)

# Annotate the top of each bar with its height (installed capacity)
for bars in [bars_solar, bars_wind, bars_hydro]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # Offset text by 3 points above the bar
                    textcoords='offset points',
                    ha='center', va='bottom', fontsize=9)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()