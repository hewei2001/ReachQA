import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Electric vehicle adoption data (in thousands) over the years for each category
solar_ev = np.array([5, 10, 20, 40, 80, 150, 230, 300, 380, 460, 550])
wind_ev = np.array([3, 6, 13, 30, 65, 130, 210, 280, 360, 420, 500])
hydropower_ev = np.array([2, 5, 12, 25, 50, 100, 170, 240, 310, 370, 430])
biofuel_ev = np.array([1, 4, 9, 20, 45, 95, 160, 220, 290, 340, 400])

# Calculate the total number of EVs for market share data
total_ev = solar_ev + wind_ev + hydropower_ev + biofuel_ev

# Constructing a synthetic data for annual growth rate of total EVs in percentage
growth_rate = np.array([np.nan] + list(np.diff(total_ev) / total_ev[:-1] * 100))

# Create the figure and primary axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Stack the areas for each category with distinct colors
ax1.stackplot(years, solar_ev, wind_ev, hydropower_ev, biofuel_ev,
              labels=['Solar', 'Wind', 'Hydropower', 'Biofuel'],
              colors=['#f39c12', '#3498db', '#2ecc71', '#9b59b6'], alpha=0.8)

# Titles and labels for primary axis
ax1.set_title("Rise of Electric Vehicles:\nA Decade of Market Growth in Renewable Adoption (2010-2020)",
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Number of EVs (in thousands)", fontsize=12)
ax1.set_xticks(years)
ax1.tick_params(axis='x', rotation=45)

# Add a grid
ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Create a secondary y-axis for the growth rate
ax2 = ax1.twinx()
ax2.plot(years, growth_rate, color='black', linestyle='--', marker='o', label='Growth Rate (%)', linewidth=2)
ax2.set_ylabel("Annual Growth Rate (%)", fontsize=12)

# Add legends for both axes
lines_labels = [ax.get_legend_handles_labels() for ax in [ax1, ax2]]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
ax1.legend(lines, labels, loc='upper left', fontsize=10, title="Energy Sources & Growth")

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()