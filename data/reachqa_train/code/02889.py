import matplotlib.pyplot as plt
import numpy as np

# Years from 2020 to 2030
years = np.arange(2020, 2031)

# Installed capacity data (in GW) for each energy source
solar_capacity = np.array([200, 220, 250, 290, 340, 400, 470, 550, 650, 770, 900])
wind_capacity = np.array([180, 200, 230, 260, 300, 350, 410, 480, 560, 650, 750])
hydro_capacity = np.array([300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400])

# Calculate cumulative installed capacity
cumulative_capacity = solar_capacity + wind_capacity + hydro_capacity

# Plotting the chart
fig, ax1 = plt.subplots(figsize=(14, 8))

bar_width = 0.25

# Calculate the positions for the bars
solar_positions = years - bar_width
wind_positions = years
hydro_positions = years + bar_width

# Create bars for each energy source
bars_solar = ax1.bar(solar_positions, solar_capacity, width=bar_width, color='gold', label='Solar Energy')
bars_wind = ax1.bar(wind_positions, wind_capacity, width=bar_width, color='skyblue', label='Wind Energy')
bars_hydro = ax1.bar(hydro_positions, hydro_capacity, width=bar_width, color='green', label='Hydropower')

# Secondary y-axis for the cumulative line plot
ax2 = ax1.twinx()
ax2.plot(years, cumulative_capacity, color='purple', marker='o', linestyle='dashed', linewidth=2, label='Cumulative Capacity')

# Titles and labels
ax1.set_title('The Rise of Renewable Energy Sources (2020 to 2030)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Installed Capacity (GW)', fontsize=12)
ax2.set_ylabel('Cumulative Capacity (GW)', fontsize=12)

# Set x-ticks and labels
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right')

# Grid and legends
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Annotate the top of each bar with its height
for bars in [bars_solar, bars_wind, bars_hydro]:
    for bar in bars:
        height = bar.get_height()
        ax1.annotate(f'{height}',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),
                     textcoords='offset points',
                     ha='center', va='bottom', fontsize=9)

# Annotate the cumulative line plot
for year, value in zip(years, cumulative_capacity):
    ax2.annotate(f'{value}', 
                 xy=(year, value), 
                 xytext=(0, -12), 
                 textcoords='offset points', 
                 ha='center', va='top', fontsize=9, color='purple')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()