import matplotlib.pyplot as plt
import numpy as np

# Define years from 2030 to 2040
years = np.arange(2030, 2041)

# Simulated power generation data in GW for different energy sources
solar = np.array([100 + 5*i for i in range(len(years))])
nuclear = np.array([200 + 10*i for i in range(len(years))])
fusion = np.array([50 + 15*i for i in range(len(years))])
antimatter = np.array([10 * (2 ** (i // 2)) for i in range(len(years))])  # Doubling every 2 years

# Create the plot
plt.figure(figsize=(12, 8))

# Plotting each power source with distinct styles
plt.plot(years, solar, label='Solar', color='gold', linewidth=2, marker='o')
plt.plot(years, nuclear, label='Nuclear', color='orange', linewidth=2, linestyle='--', marker='s')
plt.plot(years, fusion, label='Fusion', color='cyan', linewidth=2, linestyle='-.', marker='^')
plt.plot(years, antimatter, label='Antimatter', color='magenta', linewidth=2, linestyle=':', marker='D')

# Set the chart title and axis labels
plt.title("Journey to Deep Space:\nPower Generation Over Time", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Power Generation (GW)", fontsize=12)

# Adding a grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Adding a legend to identify the different power sources
plt.legend(loc='upper left', fontsize=10)

# Customize x and y ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 500, 50))

# Annotating key data points for clarity
for i, year in enumerate(years):
    plt.annotate(f'{solar[i]} GW', (year, solar[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8, color='gold')
    plt.annotate(f'{nuclear[i]} GW', (year, nuclear[i]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8, color='orange')
    plt.annotate(f'{fusion[i]} GW', (year, fusion[i]), textcoords="offset points", xytext=(0, -30), ha='center', fontsize=8, color='cyan')
    plt.annotate(f'{antimatter[i]} GW', (year, antimatter[i]), textcoords="offset points", xytext=(0, -45), ha='center', fontsize=8, color='magenta')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()