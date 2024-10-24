import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Adventure tourism data (in millions) for different regions over the years
north_america = np.array([15, 16, 18, 19, 21, 23, 24, 26, 28, 30, 32])
europe = np.array([20, 22, 24, 25, 27, 28, 30, 32, 34, 36, 38])
asia = np.array([10, 11, 13, 14, 16, 18, 20, 22, 25, 27, 30])
latin_america = np.array([8, 9, 10, 12, 14, 16, 18, 20, 23, 25, 28])

# Create a figure with a size that balances information and space
plt.figure(figsize=(12, 7))

# Plotting the data with distinct styles for clarity
plt.plot(years, north_america, label='North America', marker='o', color='#e74c3c', linestyle='-', linewidth=2)
plt.plot(years, europe, label='Europe', marker='s', color='#3498db', linestyle='--', linewidth=2)
plt.plot(years, asia, label='Asia', marker='^', color='#2ecc71', linestyle='-.', linewidth=2)
plt.plot(years, latin_america, label='Latin America', marker='d', color='#f1c40f', linestyle=':', linewidth=2)

# Annotate each region's final year data point
for region, color, data in zip(
    ['North America', 'Europe', 'Asia', 'Latin America'],
    ['#e74c3c', '#3498db', '#2ecc71', '#f1c40f'],
    [north_america, europe, asia, latin_america]
):
    plt.text(years[-1] + 0.1, data[-1], f"{region}: {data[-1]}M", color=color, fontsize=9, va='center')

# Title and axis labels
plt.title("The Evolution of Global Adventure Tourism\n(2010-2020)", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Adventure Tourists (Millions)", fontsize=12)

# Configure the legend
plt.legend(loc='upper left', title="Regions", fontsize=10, title_fontsize='12', edgecolor='gray')

# Grid for improved readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Customize the x-ticks
plt.xticks(years, rotation=45, ha='right')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()