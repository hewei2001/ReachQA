import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Hypothetical data for renewable energy adoption (TWh)
solar_energy = np.array([50, 65, 90, 130, 180, 230, 290, 360, 440, 530, 620])
wind_energy = np.array([100, 120, 160, 210, 270, 330, 400, 480, 570, 670, 780])
hydro_energy = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300])

# Calculate total renewable energy generation
total_energy = solar_energy + wind_energy + hydro_energy

# Calculate the percentage share for each energy type
solar_percentage = (solar_energy / total_energy) * 100
wind_percentage = (wind_energy / total_energy) * 100
hydro_percentage = (hydro_energy / total_energy) * 100

# Calculate annual growth rates
annual_growth_rate = np.gradient(total_energy)

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 9))

# Stack the areas for each energy source
ax1.fill_between(years, 0, solar_percentage, color='#FFD700', alpha=0.6, label='Solar Energy')
ax1.fill_between(years, solar_percentage, solar_percentage + wind_percentage, color='#1E90FF', alpha=0.6, label='Wind Energy')
ax1.fill_between(years, solar_percentage + wind_percentage, solar_percentage + wind_percentage + hydro_percentage, color='#228B22', alpha=0.6, label='Hydro Energy')

# Create a secondary y-axis for the growth rate line plot
ax2 = ax1.twinx()
ax2.plot(years, annual_growth_rate, color='#FF4500', marker='o', linestyle='-', linewidth=2, markersize=6, label='Growth Rate (%)')

# Titles and labels
ax1.set_title("Adoption of Renewable Energy & Growth Rates in Global Cities\n(2010-2020)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Percentage of Total Renewable Energy (%)", fontsize=12)
ax2.set_ylabel("Annual Growth Rate (TWh)", fontsize=12, color='#FF4500')

# Set ticks for both y-axes
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 101, 10))
ax2.set_yticks(np.arange(0, max(annual_growth_rate)+1, 50))

# Legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=12)

# Annotate key points for insights
for i, year in enumerate(years):
    if i % 2 == 0:
        ax1.annotate(f'{solar_percentage[i]:.1f}%', (year, solar_percentage[i]/2), textcoords="offset points", xytext=(0, 0),
                     fontsize=9, color='black', ha='center')
        ax1.annotate(f'{wind_percentage[i]:.1f}%', (year, solar_percentage[i] + wind_percentage[i]/2), textcoords="offset points",
                     xytext=(0, 0), fontsize=9, color='black', ha='center')
        ax1.annotate(f'{hydro_percentage[i]:.1f}%', (year, solar_percentage[i] + wind_percentage[i] + hydro_percentage[i]/2),
                     textcoords="offset points", xytext=(0, 0), fontsize=9, color='black', ha='center')
        ax2.annotate(f'{annual_growth_rate[i]:.1f}', (year, annual_growth_rate[i]), textcoords="offset points", xytext=(0, -10),
                     fontsize=9, color='#FF4500', ha='center')

# Enable grid on the primary axis
ax1.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()