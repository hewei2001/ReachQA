import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Adventure tourism data (in millions) for different regions over the years
north_america = np.array([15, 16, 18, 19, 21, 23, 24, 26, 28, 30, 32])
europe = np.array([20, 22, 24, 25, 27, 28, 30, 32, 34, 36, 38])
asia = np.array([10, 11, 13, 14, 16, 18, 20, 22, 25, 27, 30])
latin_america = np.array([8, 9, 10, 12, 14, 16, 18, 20, 23, 25, 28])

# Calculate the percentage change year over year
percent_change_na = np.diff(north_america) / north_america[:-1] * 100
percent_change_eu = np.diff(europe) / europe[:-1] * 100
percent_change_asia = np.diff(asia) / asia[:-1] * 100
percent_change_la = np.diff(latin_america) / latin_america[:-1] * 100

# Create a figure with two subplots
fig, axs = plt.subplots(2, 1, figsize=(14, 10))

# First subplot: Original line plot with enhancements
axs[0].plot(years, north_america, label='North America', marker='o', color='#e74c3c', linestyle='-', linewidth=2)
axs[0].plot(years, europe, label='Europe', marker='s', color='#3498db', linestyle='--', linewidth=2)
axs[0].plot(years, asia, label='Asia', marker='^', color='#2ecc71', linestyle='-.', linewidth=2)
axs[0].plot(years, latin_america, label='Latin America', marker='d', color='#f1c40f', linestyle=':', linewidth=2)

# Annotate each region's significant data point
for region, color, data in zip(
    ['North America', 'Europe', 'Asia', 'Latin America'],
    ['#e74c3c', '#3498db', '#2ecc71', '#f1c40f'],
    [north_america, europe, asia, latin_america]
):
    turning_point_index = np.argmax(np.diff(data))
    axs[0].annotate(f"{data[turning_point_index + 1]}M",
                    (years[turning_point_index + 1], data[turning_point_index + 1]),
                    textcoords="offset points", xytext=(-15,10), ha='center', color=color)

axs[0].set_title("Evolution of Global Adventure Tourism (2010-2020)", fontsize=14, fontweight='bold')
axs[0].set_ylabel("Number of Adventure Tourists (Millions)", fontsize=12)
axs[0].legend(loc='upper left', fontsize=10, edgecolor='gray')
axs[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axs[0].xaxis.set_major_locator(MaxNLocator(integer=True))

# Second subplot: Year over year percentage change
axs[1].plot(years[1:], percent_change_na, label='North America % Change', marker='o', color='#e74c3c', linestyle='-', linewidth=2)
axs[1].plot(years[1:], percent_change_eu, label='Europe % Change', marker='s', color='#3498db', linestyle='--', linewidth=2)
axs[1].plot(years[1:], percent_change_asia, label='Asia % Change', marker='^', color='#2ecc71', linestyle='-.', linewidth=2)
axs[1].plot(years[1:], percent_change_la, label='Latin America % Change', marker='d', color='#f1c40f', linestyle=':', linewidth=2)

axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Year over Year % Change", fontsize=12)
axs[1].legend(loc='upper right', fontsize=10, edgecolor='gray')
axs[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axs[1].xaxis.set_major_locator(MaxNLocator(integer=True))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()