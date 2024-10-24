import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Popularity data for different fashion styles
vintage = np.array([20, 25, 30, 35, 37, 40, 42, 45, 50, 55, 60])
streetwear = np.array([15, 20, 25, 30, 40, 50, 55, 60, 62, 65, 70])
athleisure = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
sustainable_fashion = np.array([1, 2, 4, 6, 9, 13, 18, 25, 33, 42, 52])

# Plot the line chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each line with distinct styles
ax.plot(years, vintage, marker='o', linestyle='-', color='#ff9999', linewidth=2, label='Vintage')
ax.plot(years, streetwear, marker='s', linestyle='-', color='#66b3ff', linewidth=2, label='Streetwear')
ax.plot(years, athleisure, marker='^', linestyle='-', color='#99ff99', linewidth=2, label='Athleisure')
ax.plot(years, sustainable_fashion, marker='x', linestyle='-', color='#ffcc99', linewidth=2, label='Sustainable Fashion')

# Annotate the lines with relevant values
for year, (v, s, a, su) in enumerate(zip(vintage, streetwear, athleisure, sustainable_fashion), start=2010):
    if year in [2015, 2020]:
        ax.annotate(f'{v}', xy=(year, v), xytext=(-10, 10), textcoords='offset points', color='#ff9999', fontsize=9)
        ax.annotate(f'{s}', xy=(year, s), xytext=(-10, 10), textcoords='offset points', color='#66b3ff', fontsize=9)
        ax.annotate(f'{a}', xy=(year, a), xytext=(-10, 10), textcoords='offset points', color='#99ff99', fontsize=9)
        ax.annotate(f'{su}', xy=(year, su), xytext=(-10, 10), textcoords='offset points', color='#ffcc99', fontsize=9)

# Set title and labels
ax.set_title("Decade of Fashion:\nPopularity Trends from 2010 to 2020", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Popularity Index", fontsize=12)

# Add a legend and grid for better readability
ax.legend(loc='upper left', title="Fashion Styles", fontsize='small')
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Rotate x-axis labels for better visibility
plt.xticks(years, rotation=45)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()