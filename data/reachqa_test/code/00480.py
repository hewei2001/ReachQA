import matplotlib.pyplot as plt
import numpy as np

# Define the years and carbon emissions data
years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020, 2023])
north_america_emissions = np.array([5000, 4800, 5200, 5500, 5000, 4700, 4500, 4200])
europe_emissions = np.array([4000, 3800, 3600, 3200, 3000, 2800, 2600, 2500])
asia_emissions = np.array([10000, 10500, 11000, 11500, 12000, 13000, 14000, 14500])
africa_emissions = np.array([1000, 1200, 1500, 1800, 2000, 2500, 3000, 3500])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Define colors for regions
colors = {
    'North America': 'lightblue',
    'Europe': 'lightgreen',
    'Asia': 'lightcoral',
    'Africa': 'lightgoldenrodyellow'
}

# Fill the areas for each region
ax.fill_between(years, north_america_emissions, color=colors['North America'], alpha=0.7, label='North America')
ax.fill_between(years, europe_emissions, color=colors['Europe'], alpha=0.7, label='Europe')
ax.fill_between(years, asia_emissions, color=colors['Asia'], alpha=0.7, label='Asia')
ax.fill_between(years, africa_emissions, color=colors['Africa'], alpha=0.7, label='Africa')

# Overlay line plots for clarity
ax.plot(years, north_america_emissions, color='blue', marker='o', linestyle='-', linewidth=2)
ax.plot(years, europe_emissions, color='green', marker='o', linestyle='-', linewidth=2)
ax.plot(years, asia_emissions, color='red', marker='o', linestyle='-', linewidth=2)
ax.plot(years, africa_emissions, color='gold', marker='o', linestyle='-', linewidth=2)

# Add data point annotations
for x, y in zip(years, north_america_emissions):
    ax.text(x, y + 100, str(y), ha='center', fontsize=9, color='blue')
for x, y in zip(years, europe_emissions):
    ax.text(x, y + 100, str(y), ha='center', fontsize=9, color='green')
for x, y in zip(years, asia_emissions):
    ax.text(x, y + 200, str(y), ha='center', fontsize=9, color='red')
for x, y in zip(years, africa_emissions):
    ax.text(x, y + 50, str(y), ha='center', fontsize=9, color='gold')

# Set title and labels
ax.set_title("Carbon Emissions Over Time\nA Global Perspective on Climate Change Initiatives", 
             fontsize=16, weight='bold', pad=15)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Carbon Emissions (Million Metric Tons)", fontsize=14)
ax.legend(loc='upper left', fontsize=12)

# Add grid lines and customize
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.xaxis.grid(True, linestyle='--', alpha=0.5)

# Adjust x-axis labels to avoid overlap
plt.xticks(years, rotation=45, fontsize=12)

# Set y-axis limit for clarity
ax.set_ylim(0, 16000)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()